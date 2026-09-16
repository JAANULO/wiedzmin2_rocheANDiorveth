import os
import shutil
from config import GAMESAVES_DIR, GAMESAVES_BACKUP_DIR

def schowaj_stare_zapisy():
    """
    Przenosi wszystkie dotychczasowe zapisy gry do osobnego folderu bezpiecznego,
    zostawiając folder gry czysty pod zapisy testowe.
    """
    os.makedirs(GAMESAVES_BACKUP_DIR, exist_ok=True)
    if not os.path.exists(GAMESAVES_DIR):
        print("[BŁĄD] Nie odnaleziono folderu gamesaves.")
        return

    pliki = os.listdir(GAMESAVES_DIR)
    przeniesiono = 0

    for p in pliki:
        # Przenosimy pliki zapisu .sav oraz miniaturki .bmp
        src = os.path.join(GAMESAVES_DIR, p)
        dst = os.path.join(GAMESAVES_BACKUP_DIR, p)
        if os.path.isfile(src):
            shutil.move(src, dst)
            przeniesiono += 1

    print("=" * 70)
    print(" PRZYGOTOWANO SYSTEM ZAPISÓW DO TESTOWANIA MODA")
    print("=" * 70)
    print(f"Schowano prywatnych plików zapisu: {przeniesiono}")
    print(f"Ścieżka kopii bezpiecznej: {GAMESAVES_BACKUP_DIR}")
    print(f"\nTeraz Twój folder gier w Wiedźminie 2 ({GAMESAVES_DIR}) jest czysty!")
    print("Gdy uruchomisz grę i wkleisz/zrobisz 1 wybrany zapis testowy,")
    print("w menu gry pojawi się TYLKO ten jeden zapis testowy!")
    print("=" * 70)

if __name__ == "__main__":
    schowaj_stare_zapisy()
