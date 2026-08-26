import os
import shutil
import time

GAME_DATA_DIR = r"C:\SteamLibrary\steamapps\common\the witcher 2\data\game"
REPO_SRC_DIR = r"c:\Users\PC\Documents\GitHub\wiedzmin2_rocheANDiorveth\src"

def synchronizuj_zmiany(minuty=120):
    """
    Znajduje zmienione pliki w katalogu gry i kopiuje je do folderu src/ w repozytorium.
    """
    now = time.time()
    limit = minuty * 60
    kopiowane = 0

    print("=" * 70)
    print(" SYNCHRONIZACJA ZMIAN Z REDKITA DO REPOZYTORIUM GIT")
    print("=" * 70)

    for root, dirs, files in os.walk(GAME_DATA_DIR):
        for file in files:
            if file.lower().endswith(('.w2quest', '.w2phase', '.w2scene', '.ws')):
                full_path = os.path.join(root, file)
                try:
                    mtime = os.path.getmtime(full_path)
                    if now - mtime < limit:
                        rel_path = os.path.relpath(full_path, GAME_DATA_DIR)
                        dest_path = os.path.join(REPO_SRC_DIR, rel_path)
                        
                        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                        shutil.copy2(full_path, dest_path)
                        print(f"[OK] Skopiowano do repo: src\\{rel_path}")
                        kopiowane += 1
                except Exception as e:
                    print(f"Błąd kopiowania {file}: {e}")

    print("=" * 70)
    print(f"Zakończono! Skopiowano zmienionych plików: {kopiowane}")
    print("=" * 70)

if __name__ == "__main__":
    synchronizuj_zmiany()
