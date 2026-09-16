import os
from pathlib import Path

# Ścieżka bazowa repozytorium (katalog wyżej niż tools/)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Ścieżki wewnątrz repozytorium
REPO_SRC_DIR = REPO_ROOT / "src"
REPO_DATA_DIR = REPO_ROOT / "data"
REPO_DOCS_DIR = REPO_ROOT / "docs"

# Lista potencjalnych ścieżek instalacji gry i REDkita (dla łatwej przenośności na nowe urządzenie)
POSSIBLE_GAME_PATHS = [
    r"C:\SteamLibrary\steamapps\common\the witcher 2",
    r"D:\SteamLibrary\steamapps\common\the witcher 2",
    r"E:\SteamLibrary\steamapps\common\the witcher 2",
    r"C:\Program Files (x86)\Steam\steamapps\common\the witcher 2",
    r"C:\Program Files\Steam\steamapps\common\the witcher 2",
    r"C:\GOG Games\The Witcher 2 Enhanced Edition",
    r"D:\GOG Games\The Witcher 2 Enhanced Edition",
]

def find_game_base_dir():
    for p in POSSIBLE_GAME_PATHS:
        if os.path.exists(os.path.join(p, "bin", "witcher2.exe")):
            return p
    # Jeśli nie wykryto automatycznie, zwracamy domyślną ścieżkę z dysku C:
    return POSSIBLE_GAME_PATHS[0]

# Wykryta lub domyślna ścieżka bazowa gry
GAME_BASE_DIR = find_game_base_dir()

GAME_DATA_DIR = os.path.join(GAME_BASE_DIR, "data", "game")
WITCHER2_EXE = os.path.join(GAME_BASE_DIR, "bin", "witcher2.exe")
WITCHER2_BIN_DIR = os.path.join(GAME_BASE_DIR, "bin")

REDKIT_EXE = os.path.join(GAME_BASE_DIR, "bin", "editor.exe")
REDKIT_BIN_DIR = os.path.join(GAME_BASE_DIR, "bin")

# Ścieżka do zapisu gier użytkownika (dynamicznie względem konta Windows ~)
GAMESAVES_DIR = os.path.expanduser(r"~\Documents\Witcher 2\gamesaves")
GAMESAVES_BACKUP_DIR = os.path.expanduser(r"~\Documents\Witcher 2\moje_stare_zapisy")

# Ścieżka do UserContent w REDkicie
USERCONTENT_PATHS = [
    os.path.expanduser(r"~\Documents\Witcher 2\UserContent\mod_hybrid_path"),
    os.path.join(GAME_BASE_DIR, "UserContent", "mod_hybrid_path")
]

