@echo off
title Uruchamianie REDkit - Wiedźmin 2 Modding

:: Wymuszenie praw Administratora, zapobiegajace bledom disk I/O
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Wykryto brak uprawnien Administratora! Przekazuje wywolanie do PowerShell...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit /B
)

:gotAdmin
    :: Skrypt uzyskał juz uprawnienia. Zmieniamy folder roboczy na folder skryptu
    pushd "%~dp0"

:: Wymuszenie kodowania UTF-8 dla polskich znakow
chcp 65001 >nul

:: ==========================================
:: TU ZMIEN SCIEZKE JESLI MASZ GRE GDZIES INDZIEJ
set "GAME_DIR=D:\SteamLibrary\steamapps\common\the witcher 2\bin"
:: ==========================================

echo ===================================================
echo Uruchamianie REDkit (The Witcher 2 Modding Tools)...
echo ===================================================
echo Ścieżka: %GAME_DIR%\editor.exe
echo.

cd /d "%GAME_DIR%" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [BLAD] Nie znaleziono podanej sciezki gry: %GAME_DIR%
    echo Zmien sciezke wewnatrz tego pliku .bat (zmienna GAME_DIR).
    pause
    exit /B
)

if not exist "editor.exe" (
    echo [BLAD] W folderze bin nie odnaleziono pliku 'editor.exe'. Prawdopodobnie brak zainstalowanych narzedzi REDkit.
    pause
    exit /B
)

start "" "editor.exe"
if %ERRORLEVEL% NEQ 0 (
    echo [BLAD] Odmowa dostepu lub błąd podczas wywoływania editor.exe!
    pause
    exit /B
)

echo REDkit zostal uruchomiony (Z uprawnieniami Administratora). Mozesz zamknac to okno.
