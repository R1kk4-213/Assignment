@echo off
echo ====================================
echo TutorHub Quick Setup Script
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Python found!
python --version
echo.

REM Create virtual environment (optional)
echo [2/4] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created!
) else (
    echo Virtual environment already exists.
)
echo.

REM Activate virtual environment
echo [3/4] Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install dependencies
echo [4/4] Installing dependencies...
pip install -r requirements.txt
echo.

REM Check for .env file
if not exist .env (
    echo [WARNING] .env file not found!
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo ====================================
    echo IMPORTANT: Configure your API key!
    echo ====================================
    echo 1. Open .env file
    echo 2. Get API key from: https://makersuite.google.com/app/apikey
    echo 3. Replace 'your_api_key_here' with your actual key
    echo.
    echo Note: App will run without API key but AI Chat won't work.
    echo.
)

echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo To run the application:
echo   1. Make sure virtual environment is activated
echo   2. Run: python app.py
echo   3. Open browser: http://127.0.0.1:5000
echo.
echo Demo accounts:
echo   Admin    - username: admin, password: admin123
echo   User     - username: hcmut_user, password: user123
echo.
pause
