# WellTrack Sprint 1 Documentation
## Daily Mood Check-In Feature

---

## 📋 Sprint Overview

**Sprint Goal:** Implement core user authentication and daily mood logging functionality

**Sprint Duration:** Sprint 1

**Completed User Stories:**
- US-01: User Account Creation
- US-02: Daily Mood Logging

---

## ✅ Implemented Features

### 1. User Registration & Authentication (US-01)
**Description:** Students can create secure accounts to store their wellness data privately.

**Functionality:**
- User registration with username/password
- Secure password hashing (SHA-256)
- Login with token-based authentication
- Session persistence using localStorage

**Acceptance Criteria Met:**
- ✅ User can create an account
- ✅ Credentials are validated
- ✅ Data is stored securely in SQLite database

---

### 2. Daily Mood Logging (US-02)
**Description:** Students can log their daily emotional state using a 5-point scale with optional tags and notes.

**Functionality:**
- Visual mood selector (1-5 scale with emojis)
- Optional mood tags (e.g., "stressed", "happy")
- Optional notes for reflection
- One mood entry per day constraint
- Mood history view showing past entries

**Acceptance Criteria Met:**
- ✅ User can log one mood per day
- ✅ Entry is saved to database
- ✅ Entry is retrievable and displayed in history

---

## 🏗️ Technical Architecture

### Backend (Flask API)
**File:** `backend/app.py`

**Endpoints:**
1. `POST /api/register` - Create new user account
2. `POST /api/login` - Authenticate user and receive token
3. `POST /api/mood` - Log daily mood (requires authentication)
4. `GET /api/mood/history` - Retrieve user's mood history

**Database Schema (SQLite):**
```sql
users:
  - id (PRIMARY KEY)
  - username (UNIQUE)
  - password_hash
  - token

mood_entries:
  - id (PRIMARY KEY)
  - user_id (FOREIGN KEY)
  - mood_level (1-5)
  - mood_tags (TEXT)
  - notes (TEXT)
  - entry_date (DATE, UNIQUE per user)
```

### Frontend (HTML/CSS/JavaScript)
**File:** `frontend/index.html`

**Components:**
- Login form
- Registration form
- Mood selector interface (5 emoji buttons)
- Mood history display
- Client-side authentication state management

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions

1. **Install Backend Dependencies:**
```bash
cd backend
pip install -r requirements.txt
```

2. **Start Backend Server:**
```bash
python app.py
```
Server will run on `http://localhost:5000`

3. **Open Frontend:**
- Open `frontend/index.html` in a web browser
- Or use a simple HTTP server:
```bash
cd frontend
python -m http.server 8000
```
Then navigate to `http://localhost:8000`

---

## 🧪 Testing Instructions

### Manual Test Cases

#### Test Case 1: User Registration
1. Open the application
2. Click "Don't have an account? Register"
3. Enter username: `testuser`
4. Enter password: `testpass123`
5. Click "Create Account"
6. **Expected:** Success message appears, redirects to login

#### Test Case 2: User Login
1. On login screen, enter registered credentials
2. Click "Login"
3. **Expected:** Redirected to mood logging interface

#### Test Case 3: Log Daily Mood
1. After logging in, select a mood emoji (e.g., 😄 Great)
2. Add tags: `happy, productive`
3. Add notes: `Had a great day studying!`
4. Click "Log Mood"
5. **Expected:** Success message, mood appears in history below

#### Test Case 4: One Mood Per Day Constraint
1. Try logging another mood on the same day
2. **Expected:** Error message: "Mood already logged for today"

#### Test Case 5: View Mood History
1. Log moods on different days (change system date for testing)
2. **Expected:** All entries displayed in chronological order with date, mood level, tags, and notes

#### Test Case 6: Authentication Required
1. Logout
2. Try accessing mood logging without logging in
3. **Expected:** Redirected to login screen

---

## 📊 Sprint Metrics

**Story Points Completed:** 8
- US-01: 3 points
- US-02: 5 points

**Velocity:** 8 points/sprint

**Code Statistics:**
- Backend: ~130 lines (Python)
- Frontend: ~250 lines (HTML/CSS/JS)
- Total: ~380 lines

---

## 🔒 Security Considerations

1. **Password Security:**
   - Passwords hashed using SHA-256
   - Plain text passwords never stored

2. **Authentication:**
   - Token-based authentication for API requests
   - Tokens stored securely in localStorage

3. **Data Privacy:**
   - Each user can only access their own mood data
   - User ID validation on all authenticated endpoints

---

## 🎯 Definition of Done

- [x] Code is written and functional
- [x] Feature runs successfully locally
- [x] Acceptance criteria for US-01 met
- [x] Acceptance criteria for US-02 met
- [x] Manual testing completed
- [x] Documentation created
- [x] Code follows minimal implementation principle

---

## 🔮 Next Sprint Considerations

**Potential Features for Sprint 2:**
- US-03: Personal Reflection Journal
- US-04: AI Wellness Companion
- US-06: Mood Trends Visualization
- Enhanced UI/UX improvements
- Input validation improvements
- Error handling enhancements

---

## 📝 Notes

**Design Decisions:**
- SQLite chosen for simplicity (no external database setup required)
- Token-based auth instead of JWT for minimal implementation
- Single HTML file for frontend to reduce complexity
- One mood per day enforced at database level (UNIQUE constraint)

**Known Limitations:**
- Basic password hashing (production would use bcrypt/argon2)
- No password strength validation
- No email verification
- No password reset functionality
- Simple token system (production would use JWT with expiration)

**Alignment with Project Goals:**
This feature provides the foundation for WellTrack's core value proposition: enabling students to track their emotional well-being over time. The mood logging system is intentionally simple and non-clinical, focusing on self-awareness rather than diagnosis.

---

## 📧 Contact
For questions about this sprint, contact the development team.

**Sprint Completed:** [Current Date]
**Next Sprint Planning:** [TBD]
