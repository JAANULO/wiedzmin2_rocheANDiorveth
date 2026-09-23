@echo off
title Uruchamianie gry Wiedźmin 2 (-uncooked)
chcp 65001 >nul
pushd "%~dp0"

echo ===================================================
echo Uruchamianie gry Wiedźmin 2 w trybie -uncooked...
echo ===================================================

python uruchom_gre.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [BŁĄD] Uruchomienie gry przez skrypt Python nie powiodło się.
    echo Sprawdź powiadomienia wyżej i upewnij się, że gra jest zainstalowana.
)

pause

