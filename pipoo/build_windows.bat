@echo off
echo ========================================
echo    Pipoo Windows Build Script
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo [ERROR] Virtual environment not found!
    echo Please create one first: python -m venv venv
    pause
    exit /b 1
)

REM Activate virtual environment
echo [1/6] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install PyInstaller if not installed
echo [2/6] Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Clean previous builds
echo [3/6] Cleaning previous builds...
if exist "build\" rmdir /s /q build
if exist "dist\" rmdir /s /q dist

REM Build executable
echo [4/6] Building Windows executable...
echo This may take 5-10 minutes...
echo.
pyinstaller pipoo.spec

REM Check if build succeeded
if exist "dist\Pipoo\Pipoo.exe" (
    echo.
    echo ========================================
    echo    BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo Executable location: dist\Pipoo\Pipoo.exe
    echo.
    echo To run the app:
    echo   cd dist\Pipoo
    echo   Pipoo.exe
    echo.
    echo To create installer, see README_WINDOWS.md
    echo.
) else (
    echo.
    echo ========================================
    echo    BUILD FAILED!
    echo ========================================
    echo.
    echo Check the output above for errors.
    echo Common issues:
    echo   - Missing dependencies
    echo   - Incorrect file paths
    echo   - Antivirus blocking
    echo.
)

pause