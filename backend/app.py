from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import date
import sqlite3
# import hashlib
import secrets
from flask_bcrypt import Bcrypt
import os
from functools import wraps


app = Flask(__name__, static_folder='../frontend', static_url_path='')


# ------------------------------ Configuration ---------------------------------
if os.environ.get("FLASK_ENV") != "production":
    app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "super_secret_key")
else:
    # Fail if FLASK_SECRET_KEY is not set in production
    app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]
DB_NAME = os.environ.get("DB_NAME", "welltrack.db")

# Fix static folder path for Render deployment
if not os.path.exists(app.static_folder):
    app.static_folder = 'frontend'  # Render deployment


bcrypt = Bcrypt(app)
CORS(app)


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT, token TEXT)''')

    # Unique constraint needs to be a composite on (user_id, entry_date)
    c.execute('''CREATE TABLE IF NOT EXISTS mood_entries
                 (id INTEGER PRIMARY KEY, user_id INTEGER, mood_level INTEGER, 
                  mood_tags TEXT, notes TEXT, entry_date DATE,
                    UNIQUE(user_id, entry_date),
                  FOREIGN KEY(user_id) REFERENCES users(id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS journal_entries
                 (id INTEGER PRIMARY KEY, user_id INTEGER, journal_text TEXT,
                    entry_date DATE,
                    UNIQUE(user_id, entry_date),
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()


def hash_password(password):
    # Industry standard password hashing using bcrypt
    return bcrypt.generate_password_hash(password).decode('utf-8')


def login_required(f):
    # This creates a decorator that can be used for any routes that need
    # user to be authenticated.
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT id FROM users WHERE token = ?', (token,))
        user = c.fetchone()
        conn.close()

        if not user:
            return jsonify({'error': 'Invalid token'}), 401

        return f(user[0], *args, **kwargs)
    return decorated_function


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                  (username, hash_password(password)))
        conn.commit()
        return jsonify({'message': 'Account created successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400
    finally:
        conn.close()


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('SELECT id, password_hash FROM users WHERE username = ?', (username,))
        user = c.fetchone()

        if user and bcrypt.check_password_hash(user[1], password):
            # TODO: Replace with JWTs to avoid needing databse lookups for
            #       each request.  A JWT would also eliminate risk of token collisions.
            # NOTE: token_hex is not guaranteed to be unique, but the
            #       probability of collision is negligible.
            token = secrets.token_hex(32)  # 32 bytes is current best practice
            c.execute('UPDATE users SET token = ? WHERE id = ?', (token, user[0]))
            conn.commit()
            return jsonify({'token': token, 'username': username}), 200

    return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/api/mood', methods=['POST'])
@login_required
def log_mood(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    data = request.json
    mood_level = data.get('mood_level')
    mood_tags = data.get('mood_tags', '')
    notes = data.get('notes', '')
    entry_date = date.today().isoformat()

    if mood_level is None or mood_level < 1 or mood_level > 5:
        conn.close()
        return jsonify({'error': 'Mood level must be between 1 and 5'}), 400

    try:
        c.execute('''INSERT INTO mood_entries (user_id, mood_level, mood_tags, notes, entry_date)
                     VALUES (?, ?, ?, ?, ?)''',
                  (user_id, mood_level, mood_tags, notes, entry_date))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Mood logged successfully', 'date': entry_date}), 201
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'Mood already logged for today'}), 400


@app.route('/api/mood/history', methods=['GET'])
@login_required
def get_mood_history(user_id):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''SELECT mood_level, mood_tags, notes, entry_date 
                 FROM mood_entries WHERE user_id = ? ORDER BY entry_date DESC''',
              (user_id,))
    entries = c.fetchall()
    conn.close()

    return jsonify({
        'entries': [
            {'mood_level': e[0], 'mood_tags': e[1], 'notes': e[2], 'date': e[3]}
            for e in entries
        ]
    }), 200


@app.route('/api/journal', methods=['POST'])
@login_required
def journal_entry(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    data = request.json
    journal_text = data.get('journal_text', '')
    entry_date = date.today().isoformat()

    if not journal_text:
        conn.close()
        return jsonify({'error': 'Journal text is required'}), 400

    # Get existing entry for the day
    c.execute('''SELECT journal_text, entry_date
                 FROM journal_entries WHERE user_id = ? and entry_date = ?''',
              (user_id, entry_date))
    entries = c.fetchall()
    if entries:
        # Update existing entry
        c.execute('''
            UPDATE journal_entries
            SET journal_text = ?
            WHERE user_id = ? AND entry_date = ?
        ''', (journal_text, user_id, entry_date))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Journal entry updated successfully', 'date': entry_date}), 200
    else:
        c.execute('''
            INSERT INTO journal_entries (user_id, journal_text, entry_date)
            VALUES (?, ?, ?)
        ''', (user_id, journal_text, entry_date))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Journal entry logged successfully', 'date': entry_date}), 201


@app.route('/api/journal/history', methods=['GET'])
@login_required
def get_journal_history(user_id):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''SELECT journal_text, entry_date 
                 FROM journal_entries WHERE user_id = ? ORDER BY entry_date DESC''',
              (user_id,))
    entries = c.fetchall()
    conn.close()

    return jsonify({
        'entries': [
            {'journal_text': e[0], 'date': e[1]}
            for e in entries
        ]
    }), 200


@app.route('/')
def index():
    assert app.static_folder is not None
    return send_from_directory(app.static_folder, 'newindex.html')


if os.environ.get("FLASK_ENV") != "production":
    @app.route('/api/debug/db', methods=['GET'])
    def debug_db():
        """Development only - view database contents"""
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        c.execute('SELECT id, username FROM users')
        users = [{'id': u[0], 'username': u[1]} for u in c.fetchall()]

        c.execute('''SELECT m.id, u.username, m.mood_level, m.mood_tags, m.notes, m.entry_date 
                    FROM mood_entries m
                    JOIN users u ON m.user_id = u.id
                    ORDER BY m.entry_date DESC''')
        moods = [
            {'id': m[0], 'username': m[1], 'mood_level': m[2], 'tags': m[3], 'notes': m[4], 'date': m[5]}
            for m in c.fetchall()
        ]

        conn.close()
        return jsonify({'users': users, 'mood_entries': moods}), 200


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
