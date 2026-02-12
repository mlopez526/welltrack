# 🎬 WellTrack Demo Guide

## Feature Demonstration: Daily Mood Check-In System

---

## 📱 Demo Flow

### Step 1: Account Creation (US-01)
**What to show:**
1. Open `frontend/index.html` in browser
2. Click "Don't have an account? Register"
3. Enter username: `demo_student`
4. Enter password: `wellness2024`
5. Click "Create Account"

**Expected Result:**
- ✅ Success message: "Account created! Please login."
- ✅ Automatic redirect to login screen

**Demonstrates:**
- User registration functionality
- Input validation
- Secure account creation

---

### Step 2: User Login (US-01)
**What to show:**
1. Enter the credentials from Step 1
2. Click "Login"

**Expected Result:**
- ✅ Successful authentication
- ✅ Redirect to mood logging interface
- ✅ Session persists (refresh page, still logged in)

**Demonstrates:**
- Authentication system
- Token-based session management
- Secure login process

---

### Step 3: First Mood Entry (US-02)
**What to show:**
1. Read the prompt: "How are you feeling today?"
2. Click on the 😄 (Great) emoji button
3. Notice the button highlights (visual feedback)
4. Add tags: `motivated, focused, energetic`
5. Add notes: `Finished my project milestone today! Feeling accomplished.`
6. Click "Log Mood"

**Expected Result:**
- ✅ Success message: "Mood logged successfully!"
- ✅ Entry appears in "Your Recent Moods" section below
- ✅ Shows: date, mood level with emoji, tags, and notes

**Demonstrates:**
- Intuitive mood selection interface
- Optional metadata (tags and notes)
- Immediate feedback and confirmation
- Data persistence

---

### Step 4: View Mood History (US-02)
**What to show:**
1. Scroll down to "Your Recent Moods" section
2. Point out the displayed information:
   - Date of entry
   - Mood level with emoji
   - Tags
   - Notes

**Expected Result:**
- ✅ All logged moods displayed chronologically
- ✅ Most recent entry at the top
- ✅ Clean, readable format

**Demonstrates:**
- Mood history tracking
- Data retrieval functionality
- Foundation for future trend analysis (US-06)

---

### Step 5: One Entry Per Day Rule (US-02)
**What to show:**
1. Try to log another mood on the same day
2. Select a different emoji (e.g., 😐 Okay)
3. Click "Log Mood"

**Expected Result:**
- ❌ Error message: "Mood already logged for today"
- ✅ Previous entry remains unchanged

**Demonstrates:**
- Business rule enforcement
- Data integrity
- Prevents duplicate entries

---

### Step 6: Session Persistence
**What to show:**
1. Refresh the browser page
2. Notice you're still logged in
3. Mood history still visible

**Expected Result:**
- ✅ User remains authenticated
- ✅ No need to login again
- ✅ Data persists across sessions

**Demonstrates:**
- Token-based authentication
- LocalStorage usage
- Seamless user experience

---

### Step 7: Logout
**What to show:**
1. Scroll down and click "Logout" button
2. Redirected to login screen
3. Try to access mood logging (refresh page)

**Expected Result:**
- ✅ Successfully logged out
- ✅ Redirected to login
- ✅ Cannot access mood data without authentication

**Demonstrates:**
- Secure logout functionality
- Session termination
- Protected routes

---

## 🎯 Key Points to Emphasize

### 1. User Story Alignment
- **US-01 Fulfilled:** Secure account creation and authentication
- **US-02 Fulfilled:** Daily mood logging with history tracking

### 2. Non-Clinical Focus
- Simple 1-5 scale (not diagnostic)
- Encourages self-reflection
- No medical terminology
- Aligns with project's wellness (not therapy) approach

### 3. Privacy & Security
- Password hashing
- Token-based authentication
- User data isolation
- Secure storage

### 4. Foundation for Future Features
- Mood data enables US-06 (Trend Visualization)
- Authentication enables US-03 (Journal)
- User system enables US-04 (AI Companion)

---

## 🧪 Alternative Demo Scenarios

### Scenario A: Error Handling
1. Try registering with existing username → Shows error
2. Try logging in with wrong password → Shows error
3. Try logging mood without selection → Shows error

### Scenario B: Multiple Days
1. Log mood for today
2. Change system date (or wait until tomorrow)
3. Log different mood
4. Show history with multiple entries

### Scenario C: API Testing
1. Run `python test_api.py`
2. Show automated API tests
3. Demonstrate backend functionality

---

## 📊 Talking Points

**Why This Feature First?**
- Core functionality for the platform
- Foundation for all other features
- Demonstrates full-stack capability
- Meets high-priority user stories

**Technical Highlights:**
- RESTful API design
- Secure authentication
- Database normalization
- Responsive UI
- Minimal but complete implementation

**Agile Alignment:**
- Delivers working software
- Meets Definition of Done
- Testable and demonstrable
- Incremental value delivery

---

## 🎤 Demo Script (2-3 minutes)

"Today I'm demonstrating WellTrack's Daily Mood Check-In feature, which implements two high-priority user stories from our backlog.

First, I'll create a student account [register]. The system securely stores credentials and confirms account creation [show success].

Now I'll log in [login], and we're taken to the mood logging interface. As a student, I can select how I'm feeling today using this intuitive 1-5 scale [select emoji]. I can add optional tags and notes for deeper reflection [add data], then log my mood [submit].

Notice the entry immediately appears in my history below [scroll to history], showing the date, mood level, and my notes. This gives students a simple way to track their emotional patterns over time.

The system enforces one entry per day [try duplicate], preventing data inconsistency. And if I refresh the page [refresh], my session persists - no need to log in again.

This feature provides the foundation for future capabilities like trend visualization and AI-powered wellness support, while maintaining our non-clinical, privacy-focused approach."

---

## ✅ Demo Checklist

Before demo:
- [ ] Backend server running (`python backend/app.py`)
- [ ] Browser open to `frontend/index.html`
- [ ] Database cleared (delete `welltrack.db` for fresh demo)
- [ ] Test credentials ready
- [ ] Documentation accessible

During demo:
- [ ] Show registration
- [ ] Show login
- [ ] Log mood with all fields
- [ ] Show history
- [ ] Demonstrate one-per-day rule
- [ ] Show logout

After demo:
- [ ] Answer questions
- [ ] Show code if requested
- [ ] Reference documentation
- [ ] Discuss next sprint features
