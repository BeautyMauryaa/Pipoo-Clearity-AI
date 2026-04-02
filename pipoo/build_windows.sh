#!/bin/bash

echo "========================================"
echo "   Pipoo Windows Build Script"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[ERROR] Virtual environment not found!"
    echo "Please create one first: python -m venv venv"
    exit 1
fi

# Activate virtual environment
echo "[1/6] Activating virtual environment..."
source venv/Scripts/activate

# Install PyInstaller if not installed
echo "[2/6] Checking PyInstaller..."
if ! pip show pyinstaller > /dev/null 2>&1; then
    echo "Installing PyInstaller..."
    pip install pyinstaller
fi

# Clean previous builds
echo "[3/6] Cleaning previous builds..."
rm -rf build dist

# Build executable
echo "[4/6] Building Windows executable..."
echo "This may take 5-10 minutes..."
echo ""
pyinstaller pipoo.spec

# Check if build succeeded
if [ -f "dist/Pipoo/Pipoo.exe" ]; then
    echo ""
    echo "========================================"
    echo "   BUILD SUCCESSFUL!"
    echo "========================================"
    echo ""
    echo "Executable location: dist/Pipoo/Pipoo.exe"
    echo ""
    echo "To run the app:"
    echo "  cd dist/Pipoo"
    echo "  ./Pipoo.exe"
    echo ""
    echo "To create installer, see README_WINDOWS.md"
    echo ""
else
    echo ""
    echo "========================================"
    echo "   BUILD FAILED!"
    echo "========================================"
    echo ""
    echo "Check the output above for errors."
    echo ""
fi