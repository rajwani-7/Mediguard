"""
SQLAlchemy ORM models for MediGuard application.
Complete database schema with all required tables.
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User model for authentication and account management."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow(), onupdate=lambda: datetime.utcnow())
    
    # Relationships
    prescriptions = db.relationship('Prescription', backref='user', lazy=True, cascade='all, delete-orphan')
    medicines = db.relationship('Medicine', backref='user', lazy=True, cascade='all, delete-orphan')
    reminders = db.relationship('Reminder', backref='user', lazy=True, cascade='all, delete-orphan')
    authenticity_logs = db.relationship('AuthenticityLog', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'


class Prescription(db.Model):
    """Prescription model for storing uploaded prescriptions."""
    __tablename__ = 'prescriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    image_path = db.Column(db.String(500), nullable=False)
    raw_text = db.Column(db.Text, nullable=True)
    uploaded_on = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())
    
    # Relationships
    medicines = db.relationship('Medicine', backref='prescription', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Prescription {self.id} by User {self.user_id}>'


class Medicine(db.Model):
    """Medicine model for tracking medicines from prescriptions."""
    __tablename__ = 'medicines'
    
    id = db.Column(db.Integer, primary_key=True)
    prescription_id = db.Column(db.Integer, db.ForeignKey('prescriptions.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    dosage = db.Column(db.String(128), nullable=False)
    timing = db.Column(db.String(128), nullable=False)  # e.g., "2x/day", "morning, evening"
    duration = db.Column(db.Integer, nullable=False)  # in days
    verified = db.Column(db.String(50), default="unverified")  # valid, fake, suspicious, unverified
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow(), onupdate=lambda: datetime.utcnow())
    
    # Relationships
    reminders = db.relationship('Reminder', backref='medicine', lazy=True, cascade='all, delete-orphan')
    authenticity_logs = db.relationship('AuthenticityLog', backref='medicine', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Medicine {self.name}>'


class AuthenticityLog(db.Model):
    """AuthenticityLog model for tracking medicine verification scans."""
    __tablename__ = 'authenticity_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=True)
    batch = db.Column(db.String(255), nullable=True)  # batch number
    expiry = db.Column(db.String(50), nullable=True)  # expiry date
    manufacturer = db.Column(db.String(255), nullable=True)  # manufacturer info
    verified_status = db.Column(db.String(50), nullable=False)  # valid, fake, suspicious
    scanned_on = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())
    details = db.Column(db.Text, nullable=True)  # Additional verification details
    
    def __repr__(self):
        return f'<AuthenticityLog {self.id}: {self.verified_status}>'


class Reminder(db.Model):
    """Reminder model for scheduled medicine reminders."""
    __tablename__ = 'reminders'
    
    id = db.Column(db.Integer, primary_key=True)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reminder_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default="pending")  # pending, taken, skipped, completed
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())
    
    def __repr__(self):
        return f'<Reminder {self.id} at {self.reminder_time}>'
