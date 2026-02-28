"""Script to seed database with initial data for testing"""
import sqlite3
from datetime import date, timedelta
import random
import bcrypt
DB_NAME = 'welltrack.db'


def main():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create test user
    hashed_password = bcrypt.hashpw('secret'.encode('utf-8'), bcrypt.gensalt())
    c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', ('bob', hashed_password.decode('utf-8')))
    user_id = c.lastrowid

    # Arrays for varied test data
    mood_levels = [5, 2, 4, 1, 3, 5, 2, 4, 1, 3]
    mood_tags_options = [
        'happy, productive',
        'stressed, overwhelmed',
        'calm, peaceful',
        'excited, motivated',
        'tired, drained',
        'anxious, worried',
        'grateful, content',
        'frustrated, angry',
        'energetic, focused',
        'sad, down',
        'hopeful, optimistic',
        'confused, uncertain'
    ]

    mood_notes = [
        'Had a great day!',
        'Feeling overwhelmed with work.',
        'Really peaceful morning meditation.',
        'Excited about new opportunities.',
        'Very tired today, need more sleep.',
        'Worried about upcoming deadlines.',
        'Grateful for family and friends.',
        'Frustrated with traffic delays.',
        'Very focused and productive today.',
        'Feeling a bit down lately.',
        'Hopeful about the future.',
        'Uncertain about some decisions.',
        'Good workout this morning!',
        'Challenging day but manageable.',
        'Beautiful weather lifted my spirits.',
        'Long day but accomplished a lot.',
        'Feeling creative and inspired.',
        'Need to practice more self-care.',
        'Great conversation with a friend.',
        'Feeling balanced and centered.'
    ]

    journal_entries_text = [
        'Today was a productive day! Completed several tasks and felt accomplished.',
        'Had a challenging morning but the afternoon was much better. Learning to manage stress.',
        'Went for a walk in the park today. Nature always helps me feel more grounded.',
        'Tried a new recipe for dinner. Cooking is becoming a therapeutic hobby.',
        'Feeling grateful for the support of my friends and family during tough times.',
        'Work was stressful today, but I managed to stay focused. Need to remember to take breaks.',
        'Had a good conversation with my therapist. Working through some old patterns.',
        'Exercise routine is really helping with my mood. Consistency is key.',
        'Feeling creative today - spent time writing and drawing. Art is healing.',
        'Had trouble sleeping last night. Need to work on my evening routine.',
        'Celebrated a small win today. Important to acknowledge progress.',
        'Feeling overwhelmed with responsibilities. Need to prioritize better.',
        'Beautiful sunrise this morning reminded me to appreciate small moments.',
        'Practiced mindfulness meditation for 20 minutes. Feeling more centered.',
        'Had coffee with an old friend. Connection is so important for wellbeing.',
        'Challenging day at work but learned something new. Growth mindset in action.',
        'Spent time in the garden today. There\'s something peaceful about plants.',
        'Reading a good book before bed. Looking forward to continuing tomorrow.',
        'Feeling proud of how I handled a difficult situation. Personal growth is real.',
        'Cooked a healthy meal and took time to enjoy it mindfully.',
        'Had a lazy Sunday and that\'s okay. Rest is productive too.',
        'Feeling inspired after watching a documentary about resilience.',
        'Practice gratitude daily - today grateful for good health.',
        'Worked on a creative project. Flow state feels amazing.',
        'Difficult conversation but necessary. Communication is getting easier.',
        'Spent time outdoors hiking. Fresh air and movement boost mood.',
        'Feeling accomplished after organizing my living space.',
        'Had a good laugh with friends. Humor is such good medicine.',
        'Reflecting on personal growth over the past month. Proud of progress.',
        'Tomorrow is a new day full of possibilities. Staying optimistic.'
    ]

    for i, mood_level in enumerate(mood_levels):  # Repeat mood levels to fill 30 days
        entry_date = (date.today() - timedelta(days=i)).isoformat()

        mood_tags = mood_tags_options[i]
        mood_note = mood_notes[i]
        print(f"Seeding mood entry for {entry_date}: Level {mood_level}, Tags: {mood_tags}, Note: {mood_note}")

        c.execute('INSERT INTO mood_entries (user_id, mood_level, mood_tags, notes, entry_date) VALUES (?, ?, ?, ?, ?)',
                  (user_id, mood_level, mood_tags, mood_note, entry_date))

        # Create journal entry for this day (80% chance to have a journal entry)
    for i, journal_text in enumerate(journal_entries_text):
        entry_date = (date.today() - timedelta(days=i)).isoformat()
        c.execute('INSERT INTO journal_entries (user_id, journal_text, entry_date) VALUES (?, ?, ?)', (user_id, journal_text, entry_date))
        print(f"Seeding journal entry for {entry_date}: {journal_text}")

    conn.commit()
    conn.close()
    print("Database seeded with 30 days of test data.")


if __name__ == '__main__':
    main()
