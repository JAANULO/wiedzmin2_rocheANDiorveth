import os
import sys
import ctypes
import subprocess

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

try:
    from config import REDKIT_EXE, REDKIT_BIN_DIR
except ImportError:
    from tools.config import REDKIT_EXE, REDKIT_BIN_DIR

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def uruchom_redkit():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if not is_admin():
        print("[INFO] Brak uprawnień administratora. Próba wymuszenia (zapobiega błędom disk I/O)...")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"[BLAD] Błąd uprawnień UAC: Użytkownik odrzucił prośbę lub wystąpił problem techniczny: {e}")
        return

    if not os.path.exists(REDKIT_BIN_DIR):
        print(f"[BLAD] Nie odnaleziono katalogu gry: {REDKIT_BIN_DIR}")
        print("Upewnij się, że gra znajduje się na dysku pod wskazanym adresem w config.py.")
        return

    if not os.path.exists(REDKIT_EXE):
        print(f"[BLAD] Wskazany folder nie zawiera pliku editor.exe!")
        print(f"Brak REDkita w: {REDKIT_EXE}")
        return

    print("=" * 60)
    print(" Uruchamianie REDkit (editor.exe) jako Administrator...")
    print("=" * 60)
    print(f"Ścieżka: {REDKIT_EXE}\n")

    try:
        subprocess.Popen([REDKIT_EXE], cwd=REDKIT_BIN_DIR)
        print("[SUKCES] REDkit został pomyślnie uruchomiony!")
    except FileNotFoundError:
        print("[BLAD] Pomimo istnienia katalogu, proces subprocess nie mógł załadować programu.")
    except PermissionError:
        print("[BLAD] Błąd dostępu: Brak wystarczających uprawnień, anty-wirus blokuje działanie pliku exe, lub dysk jest tylko do odczytu.")
    except Exception as e:
        print(f"[BLAD] Nieznany błąd podczas uruchamiania REDkita: {e}")

if __name__ == "__main__":
    uruchom_redkit()
