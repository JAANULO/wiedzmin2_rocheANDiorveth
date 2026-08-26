import os
import shutil

GAMESAVES_DIR = r"C:\Users\PC\Documents\Witcher 2\gamesaves"
BACKUP_DIR = r"C:\Users\PC\Documents\Witcher 2\moje_stare_zapisy"

def schowaj_stare_zapisy():
    """
    Przenosi wszystkie dotychczasowe zapisy gry do osobnego folderu bezpiecznego,
    zostawiając folder gry czysty pod zapisy testowe.
    """
    os.makedirs(BACKUP_DIR, exist_ok=True)
    if not os.path.exists(GAMESAVES_DIR):
        print("[BLAD] Nie odnaleziono folderu gamesaves.")
        return

    pliki = os.listdir(GAMESAVES_DIR)
    przeniesiono = 0

    for p in pliki:
        # Przenosimy pliki zapisu .sav oraz miniaturki .bmp
        src = os.path.join(GAMESAVES_DIR, p)
        dst = os.path.join(BACKUP_DIR, p)
        if os.path.isfile(src):
            shutil.move(src, dst)
            przeniesiono += 1

    print("=" * 70)
    print(" PRZYGOTOWANO SYSTEM ZAPISOW DO TESTOWANIA MODA")
    print("=" * 70)
    print(f"Schowano prywatnych plikow zapisu: {przeniesiono}")
    print(f"Sciezka kopii bezpiecznej: {BACKUP_DIR}")
    print(f"\nTeraz Twoj folder gier w Wiedźminie 2 ({GAMESAVES_DIR}) jest czysty!")
    print("Gdy uruchomisz gre i wkleisz/zrobisz 1 wybrany zapis testowy,")
    print("w menu gry pojawi sie TYLKO ten jeden zapis testowy!")
    print("=" * 70)

if __name__ == "__main__":
    schowaj_stare_zapisy()
