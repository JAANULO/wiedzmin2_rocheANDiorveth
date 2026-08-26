import os
import subprocess

WITCHER2_PATH = r"C:\SteamLibrary\steamapps\common\the witcher 2\bin\witcher2.exe"
WITCHER2_DIR = r"C:\SteamLibrary\steamapps\common\the witcher 2\bin"

def uruchom_gre():
    if not os.path.exists(WITCHER2_PATH):
        print(f"🔴 Błąd: Nie odnaleziono pliku witcher2.exe w ścieżce:\n   {WITCHER2_PATH}")
        return

    print("=" * 60)
    print(" 🚀 Uruchamianie gry Wiedźmin 2 w trybie -uncooked...")
    print("=" * 60)
    print(f"Ścieżka: {WITCHER2_PATH}\n")

    try:
        subprocess.Popen([WITCHER2_PATH, "-uncooked"], cwd=WITCHER2_DIR)
        print("🟢 Gra Wiedźmin 2 została pomyślnie uruchomiona z flaga -uncooked!")
    except Exception as e:
        print(f"🔴 Błąd podczas uruchamiania gry: {e}")

if __name__ == "__main__":
    uruchom_gre()
