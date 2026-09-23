import os
import sys
import subprocess

# Zapewnienie dostępu do modułów w folderze tools bez względu na miejsce uruchomienia
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

try:
    from config import WITCHER2_EXE, WITCHER2_BIN_DIR
except ImportError:
    from tools.config import WITCHER2_EXE, WITCHER2_BIN_DIR


def uruchom_gre():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(WITCHER2_EXE):
        print(f"[BLAD] Nie odnaleziono pliku witcher2.exe w ścieżce:\n   {WITCHER2_EXE}")
        print("Sprawdź ścieżkę w pliku tools/config.py lub upewnij się, że gra jest zainstalowana.")
        sys.exit(1)

    # Tworzymy steam_appid.txt jeśli nie istnieje, aby steam_api.dll zezwalał na bezpośrednie uruchomienie bez nadpisywania flag
    steam_appid_file = os.path.join(WITCHER2_BIN_DIR, "steam_appid.txt")
    if not os.path.exists(steam_appid_file):
        try:
            with open(steam_appid_file, "w", encoding="utf-8") as f:
                f.write("20920")
            print(f"[INFO] Utworzono plik {steam_appid_file}")
        except Exception as e:
            print(f"[OSTRZEZENIE] Nie udało się utworzyć steam_appid.txt: {e}")

    # Przygotowanie zmiennych środowiskowych, w tym SteamAppId dla poprawnego działania flag -uncooked
    env = os.environ.copy()
    env["SteamAppId"] = "20920"

    print("=" * 60)
    print(" Uruchamianie gry Wiedźmin 2 w trybie -uncooked -novideos...")
    print("=" * 60)
    print(f"Ścieżka pliku wykonywalnego: {WITCHER2_EXE}")
    print(f"Katalog roboczy: {WITCHER2_BIN_DIR}\n")

    try:
        cmd = [WITCHER2_EXE, "-uncooked", "-novideos", "-debug"]
        subprocess.Popen(cmd, cwd=WITCHER2_BIN_DIR, env=env)
        print("[SUKCES] Gra Wiedźmin 2 została pomyślnie uruchomiona z flagą -uncooked -novideos!")
    except PermissionError:
        print("[BLAD] Błąd uprawnień przy uruchamianiu witcher2.exe. Spróbuj uruchomić skrypt z uprawnieniami Administratora.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"[BLAD] Nie odnaleziono pliku wykonywalnego: {WITCHER2_EXE}")
        sys.exit(1)
    except Exception as e:
        print(f"[BLAD] Wystąpił nieoczekiwany błąd podczas uruchamiania gry: {e}")
        sys.exit(1)


if __name__ == "__main__":
    uruchom_gre()

