import os
import sys
import subprocess
from config import WITCHER2_EXE, WITCHER2_BIN_DIR

def uruchom_gre():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if not os.path.exists(WITCHER2_EXE):
        print(f"[BLAD] Nie odnaleziono pliku witcher2.exe w ścieżce:\n   {WITCHER2_EXE}")
        return

    print("=" * 60)
    print(" Uruchamianie gry Wiedźmin 2 w trybie -uncooked -novideos...")
    print("=" * 60)
    print(f"Ścieżka: {WITCHER2_EXE}\n")

    try:
        subprocess.Popen([WITCHER2_EXE, "-uncooked", "-novideos"], cwd=WITCHER2_BIN_DIR)
        print("[SUKCES] Gra Wiedźmin 2 została pomyślnie uruchomiona z flagą -uncooked -novideos!")
    except Exception as e:
        print(f"[BLAD] Błąd podczas uruchamiania gry: {e}")

if __name__ == "__main__":
    uruchom_gre()
