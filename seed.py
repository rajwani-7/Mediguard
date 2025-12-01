"""
Seed script to populate MediGuard database with test data
Run with: python seed.py
"""
from datetime import datetime, timedelta
from app import app, db
from database import User, Prescription, Medicine, Reminder, AuthenticityLog
from werkzeug.security import generate_password_hash
import os

def seed_database():
    """Populate database with test data."""
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Clear existing data (optional)
        print("Clearing existing data...")
        db.session.query(Reminder).delete()
        db.session.query(AuthenticityLog).delete()
        db.session.query(Medicine).delete()
        db.session.query(Prescription).delete()
        db.session.query(User).delete()
        db.session.commit()
        
        print("Creating test user...")
        # Create test user
        user = User(
            name='John Doe',
            username='johndoe',
            email='john@example.com',
            password_hash=generate_password_hash('password123'),
            phone='+1-555-0123'
        )
        db.session.add(user)
        db.session.flush()
        
        print("Creating test prescription...")
        # Create test prescription
        prescription = Prescription(
            user_id=user.id,
            filename='test_prescription_001.jpg',
            image_path='uploaded_prescriptions/test_prescription_001.jpg',
            raw_text='Aspirin 500mg\nAmoxicillin 250mg\nVitamin D 1000IU'
        )
        db.session.add(prescription)
        db.session.flush()
        
        print("Creating test medicines...")
        # Create test medicines
        medicines_data = [
            {
                'name': 'Aspirin',
                'dosage': '500mg',
                'timing': '2x/day',
                'duration': 10,
                'verified': 'valid'
            },
            {
                'name': 'Amoxicillin',
                'dosage': '250mg',
                'timing': '3x/day',
                'duration': 7,
                'verified': 'valid'
            },
            {
                'name': 'Vitamin D',
                'dosage': '1000 IU',
                'timing': '1x/day',
                'duration': 30,
                'verified': 'unverified'
            },
            {
                'name': 'Metformin',
                'dosage': '500mg',
                'timing': '2x/day',
                'duration': 90,
                'verified': 'suspicious'
            }
        ]
        
        medicine_ids = []
        for med_data in medicines_data:
            medicine = Medicine(
                prescription_id=prescription.id if medicine_ids == [] else None,
                user_id=user.id,
                name=med_data['name'],
                dosage=med_data['dosage'],
                timing=med_data['timing'],
                duration=med_data['duration'],
                verified=med_data['verified']
            )
            db.session.add(medicine)
            db.session.flush()
            medicine_ids.append(medicine.id)
        
        print("Creating test reminders...")
        # Create test reminders
        now = datetime.utcnow()
        for i, med_id in enumerate(medicine_ids[:2]):
            for day in range(3):
                for time_slot in range(2):
                    reminder_time = now + timedelta(days=day, hours=6 + time_slot*12)
                    reminder = Reminder(
                        medicine_id=med_id,
                        user_id=user.id,
                        reminder_time=reminder_time,
                        status='pending'
                    )
                    db.session.add(reminder)
        
        print("Creating test authenticity logs...")
        # Create test authenticity logs
        auth_log_1 = AuthenticityLog(
            user_id=user.id,
            medicine_id=medicine_ids[0],
            batch='BATCH2024001',
            expiry='2026-12-31',
            manufacturer='MediCorp Pharma',
            verified_status='valid',
            details='Valid MediGuard barcode detected\nBatch number format valid: BATCH2024001\nExpiry valid until 2026-12-31\nManufacturer: MediCorp Pharma'
        )
        
        auth_log_2 = AuthenticityLog(
            user_id=user.id,
            medicine_id=medicine_ids[3],
            batch='BATCH2023999',
            expiry='2023-06-15',
            manufacturer='Unknown',
            verified_status='fake',
            details='Medicine already expired on 2023-06-15'
        )
        
        db.session.add_all([auth_log_1, auth_log_2])
        db.session.commit()
        
        print("\n" + "="*60)
        print("✅ Database seeded successfully!")
        print("="*60)
        print("\nTest User Credentials:")
        print(f"  Username: johndoe")
        print(f"  Password: password123")
        print(f"  Email: john@example.com")
        print("\nTest Data Created:")
        print(f"  - 1 User")
        print(f"  - 1 Prescription with OCR text")
        print(f"  - 4 Medicines (various verification statuses)")
        print(f"  - 12 Reminders")
        print(f"  - 2 Authenticity Logs")
        print("="*60 + "\n")

if __name__ == '__main__':
    seed_database()
