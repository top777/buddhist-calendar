@echo off
title 打包佛历万年历为EXE
echo ========================================
echo    Buddhist Calendar - Packaged as EXE file
echo ========================================
echo.
echo This script will pack Python programs into standalone EXE files
echo Packaged EXE files can run on computers without Python
echo.
pause

REM CheckPython
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python not detected
    pause
    exit /b
)

REM CheckPyInstaller
python -c "import PyInstaller" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing PyInstaller...
    pip install pyinstaller
    echo.
)

REM Check zhdate
python -c "import zhdate" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing dependency packages...
    pip install zhdate
    echo.
)

echo Start packing...
echo.

REM Pack command
pyinstaller --onefile --windowed --name="佛历万年历" --icon=NONE 佛历万年历.py

echo.
echo ========================================
echo Packaging completed!
echo.
echo EXE file location: dist\Buddhist Era Calendar.exe
echo.
echo You can copy EXE files to use anywhere
echo ========================================
echo.
pause
