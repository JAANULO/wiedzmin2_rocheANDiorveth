# Wiedźmin 2: Zabójcy Królów – Mod „Hybrydowa Ścieżka” (Roche & Iorveth)

Modyfikacja do gry *The Witcher 2: Assassins of Kings – Enhanced Edition*, której celem jest umożliwienie graczowi rozegrania zawartości i questów z obu ścieżek fabularnych (Vernona Roche’a oraz Iorwetha) w ramach **jednego przejścia gry**, bez konieczności rozpoczynania nowej rozgrywki.

---

## 📌 O Projekcie

W oryginalnej grze pod koniec Aktu I („Na rozdrożu”) gracz zmuszony jest wybrać pomiędzy współpracą z Vernonem Rochem a pomocą Iorwethowi. Wybór ten drastycznie rozdziela Akt II na dwie wykluczające się lokacje i wątki fabularne:
* **Ścieżka Roche’a:** Obóz Kaedweński, Henselt, Detmold, obóz Niebieskich Pasów.
* **Ścieżka Iorwetha:** Wolne Miasto Vergen, Saskia, Filippa Eilhart, rada krasnoludów.

Niniejsza modyfikacja znosi sztuczną blokadę zawartości, pozwalając na doświadczenie obu historii, wykonanie zadań pobocznych obu frakcji oraz poznanie pełnego tła fabularnego w pojedynczej kampanii.

---

## 🛠️ Wymagania i Środowisko

### Wymagane Oprogramowanie (Must-have)
* **Gra:** *The Witcher 2: Assassins of Kings – Enhanced Edition* (GOG / Steam).
* **REDkit:** Oficjalne narzędzia moderskie CD Projekt RED do edycji questów (`.w2quest`), dialogów (`.w2dlg`), scen (`.w2scene`) i skryptów (`.ws`).
* **Python 3.8+:** Do uruchamiania skryptów analizy binarnej i skanowania struktur danych gry.
* **Git:** System kontroli wersji.

### Oprogramowanie Dodatkowe (Nice-to-have)
* **W2EE Unpacker / Gibbed Tools:** Do wypakowywania kontenerów `.dzip`.
* **VS Code / Notepad++:** Edytor kodu do skryptów Python i dokumentacji Markdown.
* **WinMerge / VS Code Diff:** Do porównywania zmienionych zasobów i struktur.

---

## 🚀 Szybki Start na Nowym Urządzeniu

Jeśli klonujesz to repozytorium na nowym komputerze, wykonaj te 2 proste kroki:

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/JAANULO/wiedzmin2_rocheANDiorveth.git
cd wiedzmin2_rocheANDiorveth

# 2. Utwórz powiązanie Junction z UserContent REDkita (standard CDPR):
python tools/konfiguruj_symlink.py
```

> **Gotowe!** Skrypt `konfiguruj_symlink.py` połączy folder `UserContent\mod_hybrid_path` REDkita z katalogiem `src/` repozytorium w czasie rzeczywistym.  
> Każdy zapis w REDkicie trafia od razu do repozytorium Git, bez konieczności ręcznego kopiowania czegokolwiek.

---

## 📁 Struktura Repozytorium

```
wiedzmin2_rocheANDiorveth/
├── Analiza modyfikacji do gry Wiedźmin 2.pdf # Raport z rozwiązywania problemów REDkit/PIE i skanowania
├── Claude-Mod do Wiedźmina 2 z narzędziami Gibbed.RED-20260916-1555.md # Analiza Gibbed.RED, wcc.exe i CR2W
├── src/                          # Zmodyfikowane grafy .w2quest/.w2phase moda
│   ├── 1_act1/                   # Logika wyboru w Akcie I (q108_choice)
│   ├── 2_act2/                   # Bramka wejściowa Aktu II (act 2.w2quest) i questy poboczne
│   └── meta_quests/              # Logika dzienników (postaci, miejsca, wspomnienia)
├── docs/                         # Dokumentacja techniczna projektu
│   ├── notes.md                  # Notatki z analizy w REDkicie, RE i zestawienie badań
│   └── ROADMAP.md                # Przewodnik rozwoju moda, zadania i prompt startowy
├── data/                         # Dane wygenerowane ze skanowania logiki gry
│   ├── questy_do_modyfikacji.csv # Wyselekcjonowane 114 kluczowych plików questów
│   └── raport_questow.csv        # Pełny wygenerowany raport skanera
├── tools/                        # Skrypty Python oraz launchery narzędziowe
│   ├── config.py                 # Centralny plik konfiguracyjny ścieżek
│   ├── skaner_questow.py         # Skaner binarny plików questów gry
│   ├── sync_do_git.py            # Automatyczna synchronizacja zmian z REDkita do Git
│   ├── konfiguruj_symlink.py     # Tworzenie dowiązań typu Junction (UserContent <-> Git)
│   ├── zarzadzaj_zapisami.py     # Zarządzanie profilami zapisów gry (czysty profil testowy)
│   ├── uruchom_redkit.bat / .py  # Launcher REDkita z prawami Administratora
│   └── uruchom_gre.bat / .py     # Launcher gry Wiedźmin 2 w trybie -uncooked
├── README.md                     # Dokumentacja główna projektu
└── .gitignore                    # Wykluczenia z kontroli wersji
```

---

## 🔍 Narzędzia Pomocnicze (`tools/`)

* **`tools/config.py`**: Centralny moduł ścieżek dostępu (Steam / REDkit / UserContent).
* **`tools/skaner_questow.py`**: Przeszukuje pliki logiki `.w2quest` / `.w2phase` i zapisuje wyniki w `data/questy_do_modyfikacji.csv`.
* **`tools/sync_do_git.py`**: Kopiuje zmodyfikowane pliki z katalogu gry bezpośrednio do repozytorium `src/`.
* **`tools/konfiguruj_symlink.py`**: Tworzy dowiązania typu Junction (`mklink /J`) pomiędzy katalogiem `UserContent` REDkita a folderem `src/`.
* **`tools/zarzadzaj_zapisami.py`**: Chowa dotychczasowe prywatne zapisy gry pod czyste środowisko testowe.
* **`tools/uruchom_redkit.bat` / `uruchom_redkit.py`**: Szybkie uruchomienie edytora REDkit z wymuszeniem uprawnień Administratora (UAC).
* **`tools/uruchom_gre.bat` / `uruchom_gre.py`**: Uruchamia grę Wiedźmin 2 z flagą `-uncooked` z `data/game/`.

### Uruchomienie skanera:
```bash
python tools/skaner_questow.py
```
Skrypt przeszukuje strukturę gry w poszukiwaniu odniesień do kluczowych frakcji i flag wyboru (`roche`, `iorveth`, `side_chosen`, `path`), a wynik zapisuje w pliku `data/questy_do_modyfikacji.csv`.

---

## 📅 Etapy Realizacji Moda

- [x] **Etap 1: Przygotowanie środowiska i nauka REDkita**
  - Instalacja gry, REDkita, edytorów oraz Gita.
  - Inicjalizacja repozytorium i dokumentacji.
- [/] **Etap 2: Analiza struktury gry, flag wyboru (`FactsDB`) oraz edycje bazowe**
  - Skanowanie plików `.w2quest` i `.w2scene` pod kątem flag (`q108_choice`, `act 2.w2quest`).
  - Przepięcie rozgałęzienia Aktu I (`q108_choice.w2phase`) i bramki Aktu II (`act 2.w2quest`).
  - Dodanie zsynchronizowanych questów poboczne Aktu II (`sq202`, `sq204`, `sq205i`, `sq206i`) oraz meta-questów (`characters_journal`, `places_jurnal`, `lost_memories`).
- [ ] **Etap 3: Projektowanie rozwiązania hybrydowego**
  - Wybór architektury połączenia ścieżek (sekwencyjna vs równoległa z przejściem przez Mgłę).
  - Opracowanie zbalansowanych nastawień frakcji (`Factions`).
- [ ] **Etap 4: Implementacja w REDkicie**
  - Przepięcie logiki questów w `.w2quest` i warunków startowych dialogów (`.w2dlg`).
  - Dostosowanie stref spawnów i zachowań NPC.
- [ ] **Etap 5: Testy i debugowanie**
  - Weryfikacja spójności zapisów (`save compatibility`).
  - Testowanie potencjalnych blokad fabularnych w Akcie III (Loc Muinne).
- [ ] **Etap 6: Finalizacja i Publikacja**
  - Budowa pakietu instalacyjnego moda.
  - Publikacja na Nexus Mods i GitHubie.

---

## 📜 Licencja i Prawa Autorskie

Projekt ma charakter fanowski i niekomercyjny. Wszelkie prawa do marki *Wiedźmin* oraz gry *The Witcher 2: Assassins of Kings* należą do **CD PROJEKT RED**.
