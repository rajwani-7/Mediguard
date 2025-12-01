"""
APScheduler setup and notification logic for MediGuard.
Manages background scheduling of medicine reminders.
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()


def notify_user(reminder_id, medicine_name, user_id, scheduled_time):
    """
    Notify user about a scheduled medicine reminder.
    Currently logs to stdout; can be extended for email/SMS in future.
    
    Args:
        reminder_id: ID of the reminder
        medicine_name: Name of the medicine
        user_id: ID of the user
        scheduled_time: Scheduled time for the reminder
    """
    log_message = (
        f"[REMINDER] User {user_id}: Time to take {medicine_name} "
        f"(Reminder ID: {reminder_id}, Scheduled: {scheduled_time})"
    )
    logger.info(log_message)
    print(log_message)


def schedule_reminder(reminder_id, medicine_name, user_id, scheduled_time):
    """
    Schedule a new reminder job.
    
    Args:
        reminder_id: ID of the reminder
        medicine_name: Name of the medicine
        user_id: ID of the user
        scheduled_time: DateTime object for when to trigger
    """
    try:
        job_id = f"reminder_{reminder_id}"
        trigger = DateTrigger(run_date=scheduled_time)
        scheduler.add_job(
            notify_user,
            trigger=trigger,
            args=[reminder_id, medicine_name, user_id, scheduled_time],
            id=job_id,
            replace_existing=True
        )
        logger.info(f"Scheduled job: {job_id} for {scheduled_time}")
    except Exception as e:
        logger.error(f"Error scheduling reminder {reminder_id}: {str(e)}")


def unschedule_reminder(reminder_id):
    """
    Remove a scheduled reminder job.
    
    Args:
        reminder_id: ID of the reminder to unschedule
    """
    job_id = f"reminder_{reminder_id}"
    try:
        scheduler.remove_job(job_id)
        logger.info(f"Unscheduled job: {job_id}")
    except Exception as e:
        logger.warning(f"Job not found or error removing {job_id}: {str(e)}")


def start_scheduler():
    """Start the background scheduler."""
    if not scheduler.running:
        scheduler.start()
        logger.info("Scheduler started")


def stop_scheduler():
    """Stop the background scheduler."""
    if scheduler.running:
        scheduler.shutdown()
        logger.info("Scheduler stopped")


def reschedule_existing_reminders(db_session, Reminder, Medicine):
    """
    On app startup, reschedule all pending reminders from the database.
    
    Args:
        db_session: SQLAlchemy session
        Reminder: Reminder model class
        Medicine: Medicine model class
    """
    try:
        now = datetime.utcnow()
        pending_reminders = db_session.query(Reminder).filter(
            Reminder.status == 'pending',
            Reminder.reminder_time > now
        ).all()
        
        for reminder in pending_reminders:
            medicine = reminder.medicine
            schedule_reminder(
                reminder.id,
                medicine.name,
                reminder.user_id,
                reminder.reminder_time
            )
        logger.info(f"Rescheduled {len(pending_reminders)} pending reminders from database")
    except Exception as e:
        logger.error(f"Error rescheduling existing reminders: {str(e)}")
