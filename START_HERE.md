# 🚀 START HERE - WellTrack Sprint 1 Submission

## Welcome! 👋

This is the **Daily Mood Check-In Feature** for WellTrack - an executable implementation of User Stories US-01 and US-02.

---

## ⚡ Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
python app.py
```
You should see: `Running on http://127.0.0.1:5000`

### Step 3: Open the App
Open `frontend/index.html` in your web browser

**That's it!** You're ready to test the feature.

---

## 🎯 What to Test

1. **Register** a new account (e.g., username: `demo`, password: `test123`)
2. **Login** with your credentials
3. **Select a mood** by clicking an emoji (😢 😕 😐 🙂 😄)
4. **Add tags** like "stressed, tired" (optional)
5. **Add notes** about your day (optional)
6. **Click "Log Mood"** to save
7. **View your history** displayed below
8. **Try logging again** - you'll see "already logged for today" error
9. **Logout** and login again - your data persists

---

## 📚 Documentation Guide

### For Quick Overview
- **[QUICK_SUMMARY.md](QUICK_SUMMARY.md)** - 2-minute overview of everything

### For Running the Feature
- **[README.md](README.md)** - Setup and feature list

### For Understanding the Sprint
- **[docs/SPRINT_1_DOCUMENTATION.md](docs/SPRINT_1_DOCUMENTATION.md)** - Complete sprint documentation
  - User stories implemented
  - Acceptance criteria
  - Technical architecture
  - Testing procedures
  - Sprint metrics

### For Demonstrating the Feature
- **[docs/DEMO_GUIDE.md](docs/DEMO_GUIDE.md)** - Step-by-step demo script

### For Technical Details
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System architecture diagrams

### For Verification
- **[SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)** - Requirements verification

---

## 🧪 Automated Testing

Run the API test suite:
```bash
python test_api.py
```

This will test all endpoints automatically.

---

## 📁 Project Structure

```
welltrack/
├── backend/
│   ├── app.py              # Flask API (4 endpoints)
│   ├── requirements.txt    # Python dependencies
│   └── welltrack.db        # SQLite database (auto-created)
│
├── frontend/
│   └── index.html          # Complete web interface
│
├── docs/
│   ├── SPRINT_1_DOCUMENTATION.md  # Full sprint docs
│   ├── DEMO_GUIDE.md              # Demo instructions
│   └── ARCHITECTURE.md            # Technical diagrams
│
├── README.md                      # Quick start guide
├── QUICK_SUMMARY.md               # 2-minute overview
├── SUBMISSION_CHECKLIST.md        # Requirements checklist
├── test_api.py                    # Automated tests
└── START_HERE.md                  # This file
```

---

## ✅ What Was Delivered

### User Stories Completed
- ✅ **US-01:** User Account Creation (High Priority)
  - Secure registration
  - Password hashing
  - Token-based authentication
  
- ✅ **US-02:** Daily Mood Logging (High Priority)
  - 5-point mood scale
  - Optional tags and notes
  - One entry per day
  - Mood history view

### Technical Deliverables
- ✅ Working Flask API (4 endpoints)
- ✅ SQLite database (2 tables)
- ✅ Complete web interface
- ✅ Authentication system
- ✅ Automated tests
- ✅ Comprehensive documentation

### Story Points
- **8 points** delivered in Sprint 1

---

## 🎯 Assignment Requirements

| Requirement | Status | Evidence |
|------------|--------|----------|
| Executable feature | ✅ | Run `python backend/app.py` + open `frontend/index.html` |
| Runs successfully | ✅ | Follow Quick Start above |
| Real functionality | ✅ | Complete registration → login → mood logging flow |
| Connected to user story | ✅ | US-01 and US-02 fully implemented |
| Supporting documentation | ✅ | 7 documentation files included |

---

## 🔍 Key Features to Highlight

1. **Fully Functional** - Complete end-to-end flow
2. **Secure** - Password hashing, token auth, data isolation
3. **User-Friendly** - Intuitive emoji-based interface
4. **Testable** - All acceptance criteria met
5. **Documented** - Comprehensive docs for setup, testing, demo
6. **Minimal** - ~380 lines of code, no bloat
7. **Foundation** - Enables future features (trends, AI, journal)

---

## 🎬 Quick Demo Script (60 seconds)

"This is WellTrack's Daily Mood Check-In feature implementing US-01 and US-02. 

[Register] I'll create an account - credentials are securely hashed and stored. 

[Login] Now I'll login - the system generates an authentication token. 

[Select mood] I can select my mood using this intuitive 1-5 scale with emojis. 

[Add context] I can add tags and notes for deeper reflection. 

[Submit] When I log my mood, it's immediately saved and appears in my history below. 

[Try duplicate] The system enforces one entry per day to maintain data integrity. 

This provides students with a simple, non-clinical way to track their emotional well-being over time, forming the foundation for future features like trend visualization and AI-powered wellness support."

---

## 💡 Troubleshooting

### Backend won't start
- Ensure Python 3.8+ is installed: `python --version`
- Install dependencies: `pip install -r backend/requirements.txt`
- Check if port 5000 is available

### Frontend can't connect
- Verify backend is running on `http://localhost:5000`
- Check browser console for errors (F12)
- Ensure CORS is enabled (it's included in the Flask app)

### Database issues
- Delete `backend/welltrack.db` to reset
- Database auto-creates on first run

### Need fresh start
```bash
# Delete database
rm backend/welltrack.db  # or delete manually on Windows

# Restart backend
cd backend
python app.py
```

---

## 📊 By The Numbers

- **2** User Stories (US-01, US-02)
- **8** Story Points
- **4** API Endpoints
- **2** Database Tables
- **~380** Lines of Code
- **6** Manual Test Cases
- **4** Automated Tests
- **100%** Acceptance Criteria Met

---

## 🎓 Agile Principles Demonstrated

✅ Working software delivered  
✅ Incremental value  
✅ User story driven  
✅ Definition of Done met  
✅ Sprint goal achieved  
✅ Testable and demonstrable  
✅ Ready for next iteration  

---

## 🔮 Next Sprint Preview

Future features planned:
- **US-03:** Personal Reflection Journal
- **US-04:** AI Wellness Companion
- **US-05:** AI Safety Boundaries
- **US-06:** Mood Trends Visualization
- **US-10:** Crisis Resource Detection

---

## 📞 Need Help?

1. Check [QUICK_SUMMARY.md](QUICK_SUMMARY.md) for overview
2. Check [README.md](README.md) for setup
3. Check [docs/SPRINT_1_DOCUMENTATION.md](docs/SPRINT_1_DOCUMENTATION.md) for details
4. Check [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) for verification

---

## ✨ Ready to Go!

Everything is set up and ready to run. Follow the **Quick Start** at the top of this file and you'll be testing the feature in under a minute.

**Enjoy exploring WellTrack!** 🌟

---

**Sprint:** Sprint 1  
**Feature:** Daily Mood Check-In System  
**Status:** ✅ Complete and Ready for Submission  
**User Stories:** US-01 (Account Creation) + US-02 (Mood Logging)  
**Story Points:** 8 points
