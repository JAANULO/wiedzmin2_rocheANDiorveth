import os
import subprocess
from config import WITCHER2_EXE, WITCHER2_BIN_DIR

def uruchom_gre():
    if not os.path.exists(WITCHER2_EXE):
        print(f"🔴 Błąd: Nie odnaleziono pliku witcher2.exe w ścieżce:\n   {WITCHER2_EXE}")
        return

    print("=" * 60)
    print(" 🚀 Uruchamianie gry Wiedźmin 2 w trybie -uncooked...")
    print("=" * 60)
    print(f"Ścieżka: {WITCHER2_EXE}\n")

    try:
        subprocess.Popen([WITCHER2_EXE, "-uncooked"], cwd=WITCHER2_BIN_DIR)
        print("🟢 Gra Wiedźmin 2 została pomyślnie uruchomiona z flagą -uncooked!")
    except Exception as e:
        print(f"🔴 Błąd podczas uruchamiania gry: {e}")

if __name__ == "__main__":
    uruchom_gre()
