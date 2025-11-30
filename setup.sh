#!/bin/bash

echo "===================================="
echo "TutorHub Quick Setup Script"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed!"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/4] Python found!"
python3 --version
echo ""

# Create virtual environment
echo "[2/4] Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created!"
else
    echo "Virtual environment already exists."
fi
echo ""

# Activate virtual environment
echo "[3/4] Activating virtual environment..."
source venv/bin/activate
echo ""

# Install dependencies
echo "[4/4] Installing dependencies..."
pip install -r requirements.txt
echo ""

# Check for .env file
if [ ! -f ".env" ]; then
    echo "[WARNING] .env file not found!"
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "===================================="
    echo "IMPORTANT: Configure your API key!"
    echo "===================================="
    echo "1. Open .env file"
    echo "2. Get API key from: https://makersuite.google.com/app/apikey"
    echo "3. Replace 'your_api_key_here' with your actual key"
    echo ""
    echo "Note: App will run without API key but AI Chat won't work."
    echo ""
fi

echo "===================================="
echo "Setup Complete!"
echo "===================================="
echo ""
echo "To run the application:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run: python app.py"
echo "  3. Open browser: http://127.0.0.1:5000"
echo ""
echo "Demo accounts:"
echo "  Admin - username: admin, password: admin123"
echo "  User  - username: hcmut_user, password: user123"
echo ""
