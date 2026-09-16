import os
import subprocess
from config import REPO_SRC_DIR, USERCONTENT_PATHS

def konfiguruj_automatyczne_polaczenie():
    print("=" * 70)
    print(" AUTOMATYCZNA KONFIGURACJA REDKIT <-> GIT (Junction Links)")
    print("=" * 70)
    print(f"Katalog źródłowy w Git: {REPO_SRC_DIR}\n")

    os.makedirs(REPO_SRC_DIR, exist_ok=True)

    sukces = 0
    for target in USERCONTENT_PATHS:
        parent = os.path.dirname(target)
        os.makedirs(parent, exist_ok=True)

        if os.path.exists(target):
            print(f"[OK] Łącznik już istnieje w: {target}")
            sukces += 1
            continue

        cmd = f'cmd /c mklink /J "{target}" "{REPO_SRC_DIR}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if res.returncode == 0:
            print(f"[SUKCES] Utworzono dowiązanie:\n   {target}\n   --> {REPO_SRC_DIR}\n")
            sukces += 1
        else:
            print(f"[BŁĄD] Błąd tworzenia dowiązania dla {target}: {res.stderr}")

    if sukces > 0:
        print("=" * 70)
        print("GOTOWE! Węzły połączeniowe zostały utworzone.")
        print("Gdy uruchomisz REDkit i wczytasz lub zapiszesz projekt w folderze 'mod_hybrid_path',")
        print("wszystkie pliki zostaną automatycznie zapisane bezpośrednio w Twoim repozytorium Git!")
        print("=" * 70)

if __name__ == "__main__":
    konfiguruj_automatyczne_polaczenie()
