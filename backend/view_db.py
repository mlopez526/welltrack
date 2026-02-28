import os
import sqlite3


DB_NAME = os.environ.get("DB_NAME", "welltrack.db")


def view_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    print("\n" + "="*60)
    print("WELLTRACK DATABASE VIEWER")
    print("="*60)

    # View users
    print("\n📊 USERS TABLE:")
    print("-" * 60)
    c.execute('SELECT id, username, token FROM users')
    users = c.fetchall()
    if users:
        print(f"{'ID':<5} {'Username':<20} {'Token':<35}")
        print("-" * 60)
        for user in users:
            token_display = user[2][:20] + "..." if user[2] else "None"
            print(f"{user[0]:<5} {user[1]:<20} {token_display:<35}")
    else:
        print("No users found.")

    # View mood entries
    print("\n😊 MOOD ENTRIES TABLE:")
    print("-" * 60)
    c.execute('''SELECT m.id, u.username, m.mood_level, m.mood_tags, m.notes, m.entry_date
                 FROM mood_entries m
                 JOIN users u ON m.user_id = u.id
                 ORDER BY m.entry_date DESC''')
    moods = c.fetchall()
    if moods:
        for mood in moods:
            print(f"\nEntry ID: {mood[0]}")
            print(f"  User: {mood[1]}")
            print(f"  Mood Level: {mood[2]}/5")
            print(f"  Tags: {mood[3] or 'None'}")
            print(f"  Notes: {mood[4] or 'None'}")
            print(f"  Date: {mood[5]}")
            print("-" * 60)
    else:
        print("No mood entries found.")

    # Statistics
    print("\n📈 STATISTICS:")
    print("-" * 60)
    c.execute('SELECT COUNT(*) FROM users')
    user_count = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM mood_entries')
    mood_count = c.fetchone()[0]
    print(f"Total Users: {user_count}")
    print(f"Total Mood Entries: {mood_count}")
    print("="*60 + "\n")

    conn.close()


if __name__ == '__main__':
    view_database()
