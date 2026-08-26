import os
import subprocess

REDKIT_PATH = r"C:\SteamLibrary\steamapps\common\the witcher 2\bin\editor.exe"
REDKIT_DIR = r"C:\SteamLibrary\steamapps\common\the witcher 2\bin"

def uruchom_redkit():
    if not os.path.exists(REDKIT_PATH):
        print(f"🔴 Błąd: Nie odnaleziono pliku editor.exe w ścieżce:\n   {REDKIT_PATH}")
        return

    print("=" * 60)
    print(" 🚀 Uruchamianie REDkit (Wiedźmin 2)...")
    print("=" * 60)
    print(f"Ścieżka: {REDKIT_PATH}\n")

    try:
        subprocess.Popen([REDKIT_PATH], cwd=REDKIT_DIR)
        print("🟢 REDkit został pomyślnie uruchomiony w tle!")
    except Exception as e:
        print(f"🔴 Błąd podczas uruchamiania: {e}")

if __name__ == "__main__":
    uruchom_redkit()
