#!/bin/bash
# MediGuard Quick Start Script

echo "======================================================"
echo "MediGuard - Personal Health Management System"
echo "======================================================"
echo ""

# Check Python version
echo "✓ Checking Python version..."
python_version=$(python --version 2>&1)
if [[ $python_version == *"3.10"* ]] || [[ $python_version == *"3.11"* ]] || [[ $python_version == *"3.12"* ]]; then
    echo "  $python_version ✓"
else
    echo "  WARNING: Python 3.10+ required. Found: $python_version"
fi

# Create virtual environment
echo ""
echo "✓ Setting up virtual environment..."
if [ ! -d ".venv" ]; then
    python -m venv .venv
    echo "  Virtual environment created"
else
    echo "  Virtual environment exists"
fi

# Activate venv (for display purposes)
echo ""
echo "✓ Installing dependencies..."
echo "  This may take a few minutes (especially EasyOCR download)..."
pip install -r requirements.txt -q
echo "  Dependencies installed ✓"

# Seed database
echo ""
echo "✓ Initializing database with test data..."
python seed.py
echo ""

echo "======================================================"
echo "✅ Setup Complete!"
echo "======================================================"
echo ""
echo "Next Steps:"
echo "1. Activate virtual environment:"
echo "   - Windows (CMD): .venv\Scripts\activate"
echo "   - Windows (PowerShell): .venv\Scripts\Activate.ps1"
echo "   - macOS/Linux: source .venv/bin/activate"
echo ""
echo "2. Run the application:"
echo "   python app.py"
echo ""
echo "3. Open browser:"
echo "   http://localhost:5000"
echo ""
echo "Test Credentials:"
echo "   Username: johndoe"
echo "   Password: password123"
echo ""
echo "======================================================"
