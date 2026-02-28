# WellTrack

A web-based wellness platform for tracking daily mood and emotional well-being.

---

### Local Setup

**Prerequisites:**
- Python 3.8+
- pip

**Steps:**
```bash
# 1. Install dependencies
cd backend
pip install -r requirements.txt

# 2. Run the application
python3 app.py

# 3. Open in browser
# Visit http://localhost:5000
```

### Docker Compose
**Prerequisites:**
- Docker Desktop

**Steps:**
```bash
# Start the application
docker-compose up --build

# Access at http://localhost:5000
```

### Docker CLI

```bash
# Build image
docker build -t welltrack .

# Run container
docker run -p 5000:5000 welltrack

# Access at http://localhost:5000
```

---

## 📖 About

WellTrack helps users track their daily emotional state through:
- Secure user accounts
- Daily mood logging with 5-point emoji scale
- Optional tags and notes for reflection
- Mood history tracking
- One entry per day to encourage consistent habits

---

## 🏗️ Technical Overview

**Stack:**
- Backend: Flask (Python)
- Frontend: HTML/CSS/JavaScript
- Database: SQLite
- Authentication: Token-based

**API Endpoints:**
- `POST /api/register` - Create account
- `POST /api/login` - Authenticate
- `POST /api/mood` - Log mood
- `GET /api/mood/history` - Get history
- `POST /api/journal` - Create/Update journal entry
- `GET /api/journal/history` - Get history

**Database:**
```sql
users: id, username, password_hash, token
mood_entries: id, user_id, mood_level, mood_tags, notes, entry_date
journal_entries: id, user_id, journal_text, entry_date
```

---

## 📁 Project Structure

```
welltrack/
├── backend/
│   ├── app.py              # Flask API
│   ├── requirements.txt    # Dependencies
│   └── welltrack.db        # SQLite database (auto-created)
├── frontend/
│   ├── newindex.html       # SPA Web interface
│   └── index.html          # Web interface
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Usage

1. **Register** - Create a new account
2. **Login** - Sign in with credentials
3. **Select mood** - Choose from 😢 😕 😐 🙂 😄
4. **Add context** - Optional tags and notes
5. **Log mood** - Save your entry
6. **View history** - See past entries
7. **Journal Entry** - Save your entry
8. **View Journal history** - See past entries

---

## 🧪 Testing

**Manual Testing:**
1. Register account (username: `demo`, password: `test123`)
2. Login and log a mood
3. Try logging again (should show "already logged for today")
4. Logout and login - data persists

**Automated Testing:**
```bash
python test_api.py
```

**View Database:**
```bash
# Browser or curl
http://localhost:5000/api/debug/db
```
---

### US-01: User Account Creation (High Priority)
- ✅ Secure registration with password hashing
- ✅ Token-based authentication
- ✅ Session persistence
- ✅ Secure data storage

### US-02: Daily Mood Logging (High Priority)
- ✅ 5-point mood scale with emojis
- ✅ Optional tags and notes
- ✅ One entry per day enforcement
- ✅ Mood history view
- ✅ Real-time updates

## ✨ Features Implemented
- ✅ Secure user registration and login
- ✅ Password hashing
- ✅ Token-based authentication
- ✅ Daily mood logging (1-5 scale)
- ✅ Emoji-based mood selection
- ✅ Optional tags and notes
- ✅ Mood history view
- ✅ One entry per day enforcement
- ✅ Journal Entry
- ✅ Journal history view


---