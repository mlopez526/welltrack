from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, date
import sqlite3
import hashlib
import secrets

app = Flask(__name__)
CORS(app)

DB_NAME = 'welltrack.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT, token TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS mood_entries
                 (id INTEGER PRIMARY KEY, user_id INTEGER, mood_level INTEGER, 
                  mood_tags TEXT, notes TEXT, entry_date DATE UNIQUE,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

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
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id, password_hash FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    
    if user and user[1] == hash_password(password):
        token = secrets.token_hex(16)
        c.execute('UPDATE users SET token = ? WHERE id = ?', (token, user[0]))
        conn.commit()
        conn.close()
        return jsonify({'token': token, 'username': username}), 200
    
    conn.close()
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/mood', methods=['POST'])
def log_mood():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Unauthorized'}), 401
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id FROM users WHERE token = ?', (token,))
    user = c.fetchone()
    
    if not user:
        conn.close()
        return jsonify({'error': 'Invalid token'}), 401
    
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
                  (user[0], mood_level, mood_tags, notes, entry_date))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Mood logged successfully', 'date': entry_date}), 201
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'Mood already logged for today'}), 400

@app.route('/api/mood/history', methods=['GET'])
def get_mood_history():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Unauthorized'}), 401
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id FROM users WHERE token = ?', (token,))
    user = c.fetchone()
    
    if not user:
        conn.close()
        return jsonify({'error': 'Invalid token'}), 401
    
    c.execute('''SELECT mood_level, mood_tags, notes, entry_date 
                 FROM mood_entries WHERE user_id = ? ORDER BY entry_date DESC''',
              (user[0],))
    entries = c.fetchall()
    conn.close()
    
    return jsonify({
        'entries': [
            {'mood_level': e[0], 'mood_tags': e[1], 'notes': e[2], 'date': e[3]}
            for e in entries
        ]
    }), 200

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
    moods = [{'id': m[0], 'username': m[1], 'mood_level': m[2], 
              'tags': m[3], 'notes': m[4], 'date': m[5]} for m in c.fetchall()]
    
    conn.close()
    return jsonify({'users': users, 'mood_entries': moods}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
