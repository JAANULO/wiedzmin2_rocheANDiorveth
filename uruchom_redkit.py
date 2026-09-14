import os
import sys
import ctypes
import subprocess

REDKIT_PATH = r"D:\SteamLibrary\steamapps\common\the witcher 2\bin\editor.exe"
REDKIT_DIR = r"D:\SteamLibrary\steamapps\common\the witcher 2\bin"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def uruchom_redkit():
    if not is_admin():
        print("Brak uprawnien administratora. Proba wymuszenia (zapobiega bledom disk I/O)...")
        try:
            # sys.executable to np. python.exe, sys.argv[0] to obecny skrypt
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"🔴 Błąd uprawnień UAC: Użytkownik odrzucił prośbę lub wystąpił problem techniczny: {e}")
        return

    if not os.path.exists(REDKIT_DIR):
        print(f"🔴 Błąd: Nie odnaleziono katalogu gry: {REDKIT_DIR}")
        print("Upewnij się, że gra znajduje się na dysku pod wskazanym adresem.")
        return

    if not os.path.exists(REDKIT_PATH):
        print(f"🔴 Błąd: Wskazany folder nie zawiera pliku editor.exe!")
        print(f"Brak REDkita w: {REDKIT_PATH}")
        return

    print("=" * 60)
    print(" 🚀 Uruchamianie REDkit (Wiedźmin 2) jako Administrator...")
    print("=" * 60)
    print(f"Ścieżka: {REDKIT_PATH}\n")

    try:
        subprocess.Popen([REDKIT_PATH], cwd=REDKIT_DIR)
        print("🟢 REDkit został pomyślnie uruchomiony w tle!")
    except FileNotFoundError:
        print("🔴 Błąd: Pomimo istnienia katalogu, proces subprocess nie mógł załadować programu.")
    except PermissionError:
        print("🔴 Błąd dostępu: Brak wystarczających uprawnień, anty-wirus blokuje działanie pliku exe, lub dysk jest tylko do odczytu.")
    except Exception as e:
        print(f"🔴 Nieznany błąd podczas uruchamiania: {e}")

if __name__ == "__main__":
    uruchom_redkit()
