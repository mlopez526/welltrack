# WellTrack Architecture Diagram

## System Architecture (Sprint 1)

```
┌─────────────────────────────────────────────────────────────┐
│                         FRONTEND                            │
│                    (frontend/index.html)                    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Register   │  │    Login     │  │  Mood Logger │       │
│  │    Form      │  │     Form     │  │  Interface   │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                             │
│  ┌────────────────────────────────────────────────────┐     │
│  │           Mood History Display                     │     │
│  └────────────────────────────────────────────────────┘     │
│                                                             │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/JSON
                         │ (CORS enabled)
                         ▼
┌────────────────────────────────────────────────────────────┐
│                      BACKEND API                           │
│                    (backend/app.py)                        │
│                      Flask Server                          │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              API Endpoints                           │  │
│  │                                                      │  │
│  │  POST /api/register         - Create new user        │  │
│  │  POST /api/login            - Authenticate user      │  │
│  │  POST /api/mood             - Log daily mood         │  │
│  │  GET  /api/mood/history     - Get mood entries       │  │
│  │  POST /api/journal          - Create or Update entry │  │
│  │  GET  /api/journal/history  - Get journal entries    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Authentication Layer                       │  │
│  │  - Password hashing (bcrypt)                         │  │
│  │  - Token generation                                  │  │
│  │  - Token validation                                  │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
└────────────────────────┬───────────────────────────────────┘
                         │ SQL Queries
                         ▼
┌────────────────────────────────────────────────────────────┐
│                       DATABASE                             │
│                   (welltrack.db - SQLite)                  │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  users                                               │  │
│  │  ├─ id (PRIMARY KEY)                                 │  │
│  │  ├─ username (UNIQUE)                                │  │
│  │  ├─ password_hash                                    │  │
│  │  └─ token                                            │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  mood_entries                                        │  │
│  │  ├─ id (PRIMARY KEY)                                 │  │
│  │  ├─ user_id (FOREIGN KEY → users.id)                 │  │
│  │  ├─ mood_level (1-5)                                 │  │
│  │  ├─ mood_tags (TEXT)                                 │  │
│  │  ├─ notes (TEXT)                                     │  │
│  │  └─ entry_date (DATE, UNIQUE per user)               │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  journal_entries                                     │  │
│  │  ├─ id (PRIMARY KEY)                                 │  │
│  │  ├─ user_id (FOREIGN KEY → users.id)                 │  │
│  │  ├─ journal_text (TEXT)                              │  │
│  │  └─ entry_date (DATE, UNIQUE per user)               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagrams

### 1. User Registration Flow

```
User                Frontend              Backend              Database
 │                     │                     │                     │
 │  Enter credentials  │                     │                     │
 ├────────────────────>│                     │                     │
 │                     │  POST /api/register │                     │
 │                     ├────────────────────>│                     │
 │                     │                     │  Hash password      │
 │                     │                     │  INSERT user        │
 │                     │                     ├────────────────────>│
 │                     │                     │<────────────────────┤
 │                     │  Success response   │  User created       │
 │                     │<────────────────────┤                     │
 │  "Account created"  │                     │                     │
 │<────────────────────┤                     │                     │
 │                     │                     │                     │
```

### 2. Login Flow

```
User                Frontend              Backend              Database
 │                     │                     │                     │
 │  Enter credentials  │                     │                     │
 ├────────────────────>│                     │                     │
 │                     │  POST /api/login    │                     │
 │                     ├────────────────────>│                     │
 │                     │                     │  Verify credentials │
 │                     │                     ├────────────────────>│
 │                     │                     │<────────────────────┤
 │                     │                     │  Generate token     │
 │                     │                     │  UPDATE user.token  │
 │                     │                     ├────────────────────>│
 │                     │  Token response     │                     │
 │                     │<────────────────────┤                     │
 │  Store token        │                     │                     │
 │  Show mood UI       │                     │                     │
 │<────────────────────┤                     │                     │
 │                     │                     │                     │
```

### 3. Mood Logging Flow

```
User                Frontend              Backend              Database
 │                     │                     │                     │
 │  Select mood        │                     │                     │
 │  Add tags/notes     │                     │                     │
 ├────────────────────>│                     │                     │
 │                     │  POST /api/mood     │                     │
 │                     │  (with token)       │                     │
 │                     ├────────────────────>│                     │
 │                     │                     │  Validate token     │
 │                     │                     ├────────────────────>│
 │                     │                     │<────────────────────┤
 │                     │                     │  INSERT mood_entry  │
 │                     │                     ├────────────────────>│
 │                     │                     │<────────────────────┤
 │                     │  Success response   │  Entry saved        │
 │                     │<────────────────────┤                     │
 │  "Mood logged!"     │                     │                     │
 │  Refresh history    │                     │                     │
 │<────────────────────┤                     │                     │
 │                     │                     │                     │
```

### 4. Mood History Retrieval Flow

```
User                Frontend              Backend              Database
 │                     │                     │                     │
 │  View history       │                     │                     │
 ├────────────────────>│                     │                     │
 │                     │  GET /api/mood/history                    │
 │                     │  (with token)       │                     │
 │                     ├────────────────────>│                     │
 │                     │                     │  Validate token     │
 │                     │                     ├────────────────────>│
 │                     │                     │<────────────────────┤
 │                     │                     │  SELECT mood_entries│
 │                     │                     ├────────────────────>│
 │                     │                     │<────────────────────┤
 │                     │  Entries array      │  Return results     │
 │                     │<────────────────────┤                     │
 │  Display entries    │                     │                     │
 │<────────────────────┤                     │                     │
 │                     │                     │                     │
```

### 5. Journal Entry Flow

```
User                Frontend              Backend                 Database
 │                     │                     │                        │
 │  Select journal     │                     │                        │
 │  Add tags/notes     │                     │                        │
 ├────────────────────>│                     │                        │
 │                     │  POST /api/journal  │                        │
 │                     │  (with token)       │                        │
 │                     ├────────────────────>│                        │
 │                     │                     │  Validate token        │
 │                     │                     ├───────────────────────>│
 │                     │                     │<───────────────────────┤
 │                     │                     │  UPSERT journal_entry  │
 │                     │                     ├───────────────────────>│
 │                     │                     │<───────────────────────┤
 │                     │  Success response   │  Entry saved           │
 │                     │<────────────────────┤                        │
 │  "journal logged!"  │                     │                        │
 │  Refresh history    │                     │                        │
 │<────────────────────┤                     │                        │
 │                     │                     │                        │
```

### 6. Journal History Retrieval Flow

```
User                Frontend              Backend                  Database
 │                     │                     │                         │
 │  View history       │                     │                         │
 ├────────────────────>│                     │                         │
 │                     │  GET /api/journal/history                     │
 │                     │  (with token)       │                         │
 │                     ├────────────────────>│                         │
 │                     │                     │  Validate token         │
 │                     │                     ├────────────────────────>│
 │                     │                     │<────────────────────────┤
 │                     │                     │  SELECT journal_entries │
 │                     │                     ├────────────────────────>│
 │                     │                     │<────────────────────────┤
 │                     │  Entries array      │  Return results         │
 │                     │<────────────────────┤                         │
 │  Display entries    │                     │                         │
 │<────────────────────┤                     │                         │
 │                     │                     │                         │
```

---

## Security Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Security Layers                           │
└─────────────────────────────────────────────────────────────┘

Layer 1: Frontend Validation
├─ Input validation (username, password, mood level)
├─ Token storage in localStorage
└─ Automatic logout on invalid token

Layer 2: Backend Authentication
├─ Password hashing (bcrypt)
├─ Token-based authentication
├─ Token validation on protected routes
└─ User isolation (can only access own data)

Layer 3: Database Security
├─ Parameterized queries (SQL injection prevention)
├─ Foreign key constraints
├─ Unique constraints (username, daily mood)
└─ Data isolation per user

Layer 4: API Security
├─ CORS enabled for localhost
├─ Authorization header required
├─ Input validation on all endpoints
└─ Error messages don't leak sensitive info
```

---

## Component Interaction Map

```
┌──────────────┐
│   Browser    │
│  (Client)    │
└──────┬───────┘
       │
       │ 1. User interacts with UI
       ▼
┌──────────────┐
│  index.html  │
│  JavaScript  │
└──────┬───────┘
       │
       │ 2. Makes API calls (fetch)
       ▼
┌──────────────┐
│  Flask API   │
│   (app.py)   │
└──────┬───────┘
       │
       │ 3. Processes request
       │    Validates auth
       ▼
┌──────────────┐
│   SQLite     │
│  Database    │
└──────┬───────┘
       │
       │ 4. Returns data
       ▼
┌──────────────┐
│  Flask API   │
│  (response)  │
└──────┬───────┘
       │
       │ 5. Sends JSON response
       ▼
┌──────────────┐
│  JavaScript  │
│  (updates UI)│
└──────┬───────┘
       │
       │ 6. User sees result
       ▼
┌──────────────┐
│   Browser    │
│   Display    │
└──────────────┘
```

---

## File Dependencies

```
welltrack/
│
├── backend/
│   ├── app.py
│   │   ├── Imports: flask, flask_cors, sqlite3, flask-bcrypt, secrets
│   │   ├── Creates: welltrack.db (auto)
│   │   └── Serves: API endpoints on port 5000
│   │
│   └── requirements.txt
│       └── Specifies: Flask, flask-cors, requests
│
├── frontend/
│   └── newindex.html
│       ├── Connects to: http://localhost:5000/api
│       ├── Uses: localStorage for token
│       └── Imports VueJS from CDN
│
├── frontend/
│   └── index.html
│       ├── Connects to: http://localhost:5000/api
│       ├── Uses: localStorage for token
│       └── Standalone (no external dependencies)
│
└── test_api.py
    ├── Imports: requests, json, datetime
    └── Tests: All API endpoints
```

---

## Technology Stack

```
┌─────────────────────────────────────────┐
│           Frontend Stack                │
├─────────────────────────────────────────┤
│  HTML5        - Structure               │
│  CSS3         - Styling                 │
│  JavaScript   - Logic & API calls       │
│  Fetch API    - HTTP requests           │
│  localStorage - Token persistence       │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│           Backend Stack                 │
├─────────────────────────────────────────┤
│  Python 3.8+  - Language                │
│  Flask 3.0    - Web framework           │
│  flask-cors   - CORS handling           │
│  sqlite3      - Database driver         │
│  flask-bcrypt - Password hashing        │
│  secrets      - Token generation        │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│           Database Stack                │
├─────────────────────────────────────────┤
│  SQLite 3     - Relational database     │
│  File-based   - No server needed        │
│  ACID         - Transaction support     │
└─────────────────────────────────────────┘
```

---

## Deployment Architecture (Current: Local)

```
┌────────────────────────────────────────────────┐
│         Local Development Environment          │
│                                                │
│  ┌──────────────────────────────────────────┐  │
│  │  Frontend: file:///path/to/index.html    │  │
│  │  Port: N/A (file protocol)               │  │
│  └──────────────────────────────────────────┘  │
│                      │                         │
│                      │ HTTP                    │
│                      ▼                         │
│  ┌──────────────────────────────────────────┐  │
│  │  Backend: http://localhost:5000          │  │
│  │  Process: python app.py                  │  │
│  └──────────────────────────────────────────┘  │
│                      │                         │
│                      │ SQL                     │
│                      ▼                         │
│  ┌──────────────────────────────────────────┐  │
│  │  Database: ./welltrack.db                │  │
│  │  File-based SQLite                       │  │
│  └──────────────────────────────────────────┘  │
│                                                │
└────────────────────────────────────────────────┘
```

---

## Future Architecture (Stretch Goals)

```
┌────────────────────────────────────────────────┐
│              Production Environment            │
│                                                │
│  ┌──────────────────────────────────────────┐  │
│  │  Frontend: Hosted on AWS S3/CloudFront   │  │
│  │  HTTPS enabled                           │  │
│  └──────────────────────────────────────────┘  │
│                      │                         │
│                      │ HTTPS/REST              │
│                      ▼                         │
│  ┌──────────────────────────────────────────┐  │
│  │  Backend: AWS Lambda + API Gateway       │  │
│  │  or EC2 with Gunicorn                    │  │
│  └──────────────────────────────────────────┘  │
│                      │                         │
│                      │ SQL                     │
│                      ▼                         │
│  ┌──────────────────────────────────────────┐  │
│  │  Database: AWS RDS (PostgreSQL)          │  │
│  │  or DynamoDB                             │  │
│  └──────────────────────────────────────────┘  │
│                      │                         │
│                      │ API Call                │
│                      ▼                         │
│  ┌──────────────────────────────────────────┐  │
│  │  AI Service: AWS Bedrock / OpenAI API    │  │
│  │  (for US-04: AI Wellness Companion)      │  │
│  └──────────────────────────────────────────┘  │
│                                                │
└────────────────────────────────────────────────┘
```
