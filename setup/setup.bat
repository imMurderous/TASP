@echo off
title TASP Setup
echo ===============================
echo  Tyla's Auto Self Promo (TASP)
echo ===============================
echo.
echo Installing required dependencies...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.6+ and try again.
    pause
    exit /b
)

:: Install required packages
pip install -r requirements.txt

:: Check if installation was successful
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b
)

echo.
echo [INFO] Setup complete! You can now run the bot.
echo.
pause
