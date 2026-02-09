@echo off
echo ========================================
echo    Buddhist Era Calendar - PWA Local Test Server
echo ========================================
echo.
echo Starting server...
echo.
echo Server address: http://localhost:8080
echo.
echo Please visit in your mobile browser:
echo http://your-computer-IP:8080/Offline-Buddhist-Lunar-Calendar-Tool.html
echo.
echo To view your computer's IP address, please input ipconfig in the command line:
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Check if Node.js is installed
where node >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    REM Use Node.js's http-server
    where http-server >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        http-server -p 8080 -c-1
    ) else (
        echo http-server is not installed, installing...
        npm install -g http-server
        http-server -p 8080 -c-1
    )
) else (
    echo.
    echo Error: Node.js not detected
    echo.
    echo Please install Node.js first: https://nodejs.org/
    echo.
    echo or open the HTML file directly with a mobile browser
    echo.
    pause
)
