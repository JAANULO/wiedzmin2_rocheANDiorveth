import os
import subprocess

REPO_SRC_DIR = r"c:\Users\PC\Documents\GitHub\wiedzmin2_rocheANDiorveth\src"

# Standardowe lokalizacje projektów/UserContent w REDkicie
MIEJSCA_USERCONTENT = [
    r"C:\Users\PC\Documents\Witcher 2\UserContent\mod_hybrid_path",
    r"C:\SteamLibrary\steamapps\common\the witcher 2\UserContent\mod_hybrid_path"
]

def konfiguruj_automatyczne_polaczenie():
    print("=" * 70)
    print(" AUTOMATYCZNA KONFIGURACJA REDKIT <-> GIT (Junction Links)")
    print("=" * 70)
    print(f"Katalog zrodlowy w Git: {REPO_SRC_DIR}\n")

    if not os.path.exists(REPO_SRC_DIR):
        os.makedirs(REPO_SRC_DIR, exist_ok=True)

    sukces = 0
    for target in MIEJSCA_USERCONTENT:
        parent = os.path.dirname(target)
        os.makedirs(parent, exist_ok=True)

        if os.path.exists(target):
            print(f"[OK] Łącznik juz istnieje w: {target}")
            sukces += 1
            continue

        cmd = f'cmd /c mklink /J "{target}" "{REPO_SRC_DIR}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if res.returncode == 0:
            print(f"[SUKCES] Utworzono dowiazanie:\n   {target}\n   --> {REPO_SRC_DIR}\n")
            sukces += 1
        else:
            print(f"[BLAD] Błąd tworzenia dowiązania dla {target}: {res.stderr}")

    if sukces > 0:
        print("=" * 70)
        print("GOTOWE! Węzły połączeniowe zostały utworzone.")
        print("Gdy uruchomisz REDkit i wczytasz lub zapiszesz projekt w folderze 'mod_hybrid_path',")
        print("wszystkie pliki zostaną automatycznie zapisane bezpośrednio w Twoim repozytorium Git!")
        print("=" * 70)

if __name__ == "__main__":
    konfiguruj_automatyczne_polaczenie()
