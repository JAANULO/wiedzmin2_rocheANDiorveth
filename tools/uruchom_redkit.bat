@echo off
title Uruchamianie REDkit - Wiedźmin 2 Modding

:: Wymuszenie praw Administratora
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Wykryto brak uprawnień Administratora! Przekazuję wywołanie do PowerShell...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit /B
)

:gotAdmin
pushd "%~dp0"
chcp 65001 >nul

echo ===================================================
echo Uruchamianie REDkit (The Witcher 2 Modding Tools)...
echo ===================================================

python uruchom_redkit.py
if %ERRORLEVEL% NEQ 0 (
    echo [INFORMACJA] Próba bezpośredniego wywołania editor.exe...
    cd /d "C:\SteamLibrary\steamapps\common\the witcher 2\bin"
    start "" "editor.exe"
)

pause
