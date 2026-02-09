@echo off
title 佛历万年历
echo ========================================
echo    Buddhist Calendar - Python Version
echo ========================================
echo.
echo Starting program...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python not detected
    echo.
    echo Please install Python first: https://www.python.org/
    echo.
    echo Install and check "Add Python to PATH"
    echo.
    pause
    exit /b
)

REM Check if zhdate is installed
python -c "import zhdate" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing dependency packages...
    echo.
    pip install zhdate
    echo.
    if %ERRORLEVEL% NEQ 0 (
        echo Dependency installation failed please manually execute: pip install zhdate
        echo.
        pause
        exit /b
    )
)

REM Start program
echo Starting...
python 佛历万年历.py 2>&1

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Program run error
    pause
)
