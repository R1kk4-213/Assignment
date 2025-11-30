@echo off
echo Starting TutorHub Application...
echo.

REM Activate virtual environment if exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Run the application
python app.py

pause
