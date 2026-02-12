# 🌟 WellTrack - Daily Mood Check-In Feature

An AI-Assisted Non-Clinical Wellness Check-In Platform for Students

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Run Backend
```bash
python app.py
```
Backend runs on `http://localhost:5000`

### 3. Open Frontend
Open `frontend/index.html` in your browser

## ✨ Current Features

- ✅ User Registration & Login (US-01)
- ✅ Daily Mood Logging (US-02)
- ✅ Mood History View
- ✅ Secure Data Storage

## 📖 Documentation

See `docs/SPRINT_1_DOCUMENTATION.md` for complete sprint documentation.

## 🧪 Quick Test

1. Register a new account
2. Login with your credentials
3. Select a mood emoji (1-5 scale)
4. Add optional tags and notes
5. Click "Log Mood"
6. View your mood history below

## 🏗️ Project Structure

```
welltrack/
├── backend/
│   ├── app.py              # Flask API
│   ├── requirements.txt    # Python dependencies
│   └── welltrack.db        # SQLite database (auto-created)
├── frontend/
│   └── index.html          # Web interface
└── docs/
    └── SPRINT_1_DOCUMENTATION.md
```

## 📋 User Stories Implemented

- **US-01:** As a student, I want to create an account, so that my wellness data is stored securely.
- **US-02:** As a student, I want to log my daily mood, so that I can track how I feel over time.

## 🔜 Coming Soon

- Personal Reflection Journal (US-03)
- AI Wellness Companion (US-04)
- Mood Trends Visualization (US-06)
- Wellness Resource Library (US-07)
