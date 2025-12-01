@echo off
REM MediGuard Quick Start Script for Windows

echo ======================================================
echo MediGuard - Personal Health Management System
echo ======================================================
echo.

REM Check Python version
echo Checking Python version...
python --version
echo.

REM Create virtual environment
echo Setting up virtual environment...
if not exist ".venv" (
    python -m venv .venv
    echo Virtual environment created
) else (
    echo Virtual environment exists
)
echo.

REM Install dependencies
echo Installing dependencies...
echo This may take a few minutes (especially EasyOCR download)...
pip install -r requirements.txt -q
echo Dependencies installed
echo.

REM Seed database
echo Initializing database with test data...
python seed.py
echo.

echo ======================================================
echo Setup Complete!
echo ======================================================
echo.
echo Next Steps:
echo 1. Activate virtual environment:
echo    .venv\Scripts\activate
echo.
echo 2. Run the application:
echo    python app.py
echo.
echo 3. Open browser:
echo    http://localhost:5000
echo.
echo Test Credentials:
echo    Username: johndoe
echo    Password: password123
echo.
echo ======================================================
pause
