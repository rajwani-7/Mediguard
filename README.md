# MediGuard - Full-Stack Personal Health Management System

A comprehensive web application for prescription tracking, medicine authenticity verification, and automated medicine reminders.

## 🎯 Key Features

✅ **Complete Authentication System**
- Secure signup and login with hashed passwords
- Session-based user management
- Password validation

✅ **Smart Prescription Reader**
- OCR extraction using EasyOCR or Tesseract
- Extract medicine name, dosage, timing, duration
- Editable medicine table for corrections
- Save to database with automatic reminders

✅ **Medicine Authenticity Verification**
- Barcode/QR code scanning (Pyzbar + OpenCV)
- Fake pattern detection rules
- Manufacturer, batch, and expiry verification
- Verification history tracking

✅ **Automatic Reminder System**
- APScheduler for background job scheduling
- Reminders based on medicine timing
- Mark reminders as taken/skipped
- Dashboard shows upcoming reminders

✅ **Dashboard & Analytics**
- Upcoming reminders (next 24 hours)
- Recent prescriptions list
- Medicine verification statistics
- Quick action buttons

✅ **Complete CRUD Operations**
- Create, read, update, delete prescriptions
- Manage medicines
- Track verification history
- Full prescription management

✅ **Beautiful UI/UX**
- Tailwind CSS responsive design
- Medical-themed color palette
- Hover animations
- Mobile responsive
- Heroicons integration

## 📊 Database Structure

```
Users: id, name, email, username, password_hash, phone, created_at, updated_at
Prescriptions: id, user_id, filename, image_path, raw_text, uploaded_on
Medicines: id, prescription_id, user_id, name, dosage, timing, duration, verified, created_at, updated_at
AuthenticityLog: id, user_id, medicine_id, batch, expiry, manufacturer, verified_status, scanned_on, details
Reminders: id, medicine_id, user_id, reminder_time, status, created_at
```

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML5, Tailwind CSS, Vanilla JavaScript |
| **Backend** | Python Flask |
| **Database** | SQLite with SQLAlchemy ORM |
| **OCR** | EasyOCR or Tesseract (pytesseract) |
| **QR/Barcode** | Pyzbar + OpenCV |
| **Scheduler** | APScheduler |
| **Security** | Werkzeug hashing |

## 📁 Project Structure

```
MediGuard/
├── app.py                          # Main Flask application (500+ lines)
├── database.py                     # SQLAlchemy models (5 tables)
├── scheduler.py                    # APScheduler setup
├── seed.py                         # Test data seeding
├── requirements.txt                # Dependencies
├── templates/
│   ├── layout.html                 # Base template with sidebar
│   ├── index.html                  # Dashboard
│   ├── auth/login.html             # Login page
│   ├── auth/signup.html            # Signup page
│   ├── prescriptions/upload.html   # OCR prescription reader
│   ├── prescriptions/list.html     # Prescription list with pagination
│   ├── prescriptions/view.html     # Prescription details & edit
│   ├── verify/verify.html          # Medicine verification scanner
│   ├── reminders/list.html         # Reminders management
│   └── medicines/list.html         # Medicine categorized view
├── uploaded_prescriptions/         # Image storage (auto-created)
├── mediaguard.db                   # SQLite database (auto-created)
└── README.md                       # This file
```

## 🚀 Quick Start

### 1. Prerequisites
```bash
Python 3.10+, pip
```

### 2. Clone & Setup
```bash
cd MediGuard
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize with Test Data
```bash
python seed.py
```

### 5. Run Application
```bash
python app.py
```

Access at: **http://localhost:5000**

**Test Credentials:**
- Username: `johndoe`
- Password: `password123`

## 📋 API Routes (30+ Endpoints)

### Authentication (3 routes)
- `GET/POST /auth/signup` - Register account
- `GET/POST /auth/login` - Login
- `GET /auth/logout` - Logout

### Dashboard (1 route)
- `GET /` - Home dashboard with stats

### Prescriptions (7 routes)
- `GET /prescriptions` - List prescriptions (paginated)
- `GET/POST /upload-prescription` - Upload & extract OCR
- `POST /upload-prescription/save` - Save medicines
- `GET /prescriptions/<id>` - View prescription
- `POST /prescriptions/<id>/edit-medicine` - Edit medicine
- `POST /prescriptions/<id>/delete` - Delete prescription
- `POST /medicines/<id>/delete` - Delete medicine

### Medicine Verification (1 route)
- `GET/POST /verify-medicine` - Scan & verify authenticity

### Reminders (4 routes)
- `GET /reminders` - View all reminders (paginated)
- `POST /reminder/<id>/mark-taken` - Mark reminder taken
- `POST /reminder/<id>/skip` - Skip reminder

### Additional Routes (2 routes)
- `GET /api/authenticity-history` - JSON API
- `GET /medicines` - View medicines by status

## 🎨 UI Features

- **Responsive Design**: Desktop, tablet, mobile
- **Tailwind CSS**: Beautiful utility-first styling
- **Medical Theme**: Blue, green, red, yellow color coding
- **Smooth Animations**: Hover effects and transitions
- **Flash Messages**: Success/danger/warning alerts
- **Pagination**: Efficient data browsing
- **Status Indicators**: Visual verification status

## 🧪 Seed Data

Run `python seed.py` to populate:
- 1 test user (johndoe)
- 1 prescription with 4 medicines
- 12 pending reminders
- 2 authenticity logs (valid + fake)

## 📖 Features Implemented

✅ User signup/login/logout with password hashing
✅ Dashboard with statistics and upcoming reminders
✅ Prescription upload with OCR extraction
✅ Medicine CRUD operations
✅ Edit medicines with inline validation
✅ QR/barcode scanning and verification
✅ Fake medicine detection rules
✅ Verification history tracking
✅ Automatic reminder generation
✅ Mark reminders as taken/skipped
✅ Prescriptions list with pagination
✅ Medicines grouped by verification status
✅ Responsive Tailwind CSS UI
✅ Session-based authentication
✅ Database models with relationships
✅ Error handling and flash messages
✅ Image upload validation
✅ File storage management
✅ Reminder scheduling (APScheduler)
✅ API endpoints for frontend

## 🔑 Test Scenarios

### Upload Prescription
1. Login with test account
2. Click "Upload Prescription"
3. Upload any image (JPG, PNG, GIF, BMP)
4. Review extracted medicines
5. Click "Confirm & Save"
6. Check dashboard for new reminders

### Verify Medicine
1. Click "Verify Medicine"
2. Upload barcode image (test codes below)
3. View verification result
4. Result saved to history

**Test QR/Barcode Codes:**
- `MG-VALID-ABC123` → Valid ✓
- `FAKE-MEDICINE` → Fake ✗
- `BATCH123` → Suspicious ⚠

### Manage Reminders
1. Go to Reminders page
2. Click "Mark Taken" on any reminder
3. See status change in real-time
4. Verify in database

### Edit Medicines
1. Go to Prescriptions → View Prescription
2. Click edit icon on any medicine
3. Change fields
4. Click save button
5. Changes persist

## ⚙️ Installation Details

### Install Tesseract (Optional, if not using EasyOCR)

**Windows:**
1. Download: https://github.com/UB-Mannheim/tesseract/wiki
2. Install to `C:\Program Files\Tesseract-OCR`
3. App auto-detects on startup

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

### Troubleshoot Dependencies

**OCR Issues:**
```bash
pip install --upgrade easyocr pytesseract pillow
```

**OpenCV Issues:**
```bash
pip install --upgrade opencv-python
```

**Pyzbar Issues:**
```bash
# Windows
pip install --upgrade pyzbar

# Linux
sudo apt-get install libzbar0 libzbar-dev
pip install pyzbar
```

## 🔐 Security

- Passwords hashed with werkzeug.security
- Session-based authentication
- SQLAlchemy ORM prevents SQL injection
- User data isolation
- File upload validation
- CORS ready for production

**For Production:**
```bash
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
export FLASK_ENV="production"
python app.py
```

Use Gunicorn for production:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 in use | Change port: `python app.py --port 5001` |
| Database locked | Delete `mediaguard.db` and run `python seed.py` |
| Module not found | Run `pip install -r requirements.txt --upgrade` |
| OCR not working | Install EasyOCR: `pip install easyocr` |
| QR scan not working | Install pyzbar: `pip install pyzbar` |

## 📱 Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🚀 Performance

- SQLite optimized queries
- Pagination for large datasets
- Lazy loading for OCR models
- Async job scheduling with APScheduler
- Efficient medicine filtering

## 📝 Code Statistics

- **Total Lines**: 1000+
- **Python Code**: 700+ lines (app.py, database.py, scheduler.py)
- **HTML Templates**: 300+ lines
- **JavaScript**: 100+ lines
- **CSS Classes**: 50+ Tailwind utilities

## 🎓 Educational Value

Learn:
- Full-stack Flask development
- Database design with SQLAlchemy
- OCR integration (EasyOCR/Tesseract)
- Image processing (OpenCV)
- Background job scheduling (APScheduler)
- Frontend design with Tailwind CSS
- Session management
- RESTful API design
- File upload handling
- Authentication & security

## 📞 Support

1. Check error logs in terminal
2. Verify Python 3.10+: `python --version`
3. List installed packages: `pip list`
4. Reseed database: `python seed.py`
5. Delete cache: `rm mediaguard.db`

## 🎯 Future Enhancements

- Email notifications for reminders
- SMS reminders integration
- Mobile app (Flutter/React Native)
- Advanced analytics dashboard
- Medicine interaction checker
- Insurance coverage lookup
- Doctor appointment scheduling
- Prescription refill tracking

## 📄 License

Open source for educational use.

---

**Made with ❤️ for better health management**

**Happy using MediGuard! 💊**
