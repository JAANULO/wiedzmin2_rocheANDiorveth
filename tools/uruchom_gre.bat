@echo off
title Uruchamianie gry Wiedźmin 2 (-uncooked)
chcp 65001 >nul
pushd "%~dp0"

echo ===================================================
echo Uruchamianie gry Wiedźmin 2 w trybie -uncooked...
echo ===================================================

python uruchom_gre.py
if %ERRORLEVEL% NEQ 0 (
    echo [INFORMACJA] Próba uruchomienia bez pośrednictwa Pythona...
    cd /d "C:\SteamLibrary\steamapps\common\the witcher 2\bin"
    start "" "witcher2.exe" -uncooked -novideos
)

pause
