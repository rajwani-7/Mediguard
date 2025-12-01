"""
WSGI entry point for production deployment with Gunicorn.
"""
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import app after logging is configured
from app import app

if __name__ == "__main__":
    logger.info("Starting MediGuard WSGI application")
    app.run()
