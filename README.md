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

## 📁 Struktura Repozytorium

```
wiedzmin2_rocheANDiorveth/
├── src/                       # Zmodyfikowane grafy .w2quest/.w2phase moda
├── docs/                      # Dokumentacja techniczna i rejestr flag FactsDB
│   └── notes.md               # Notatki z analizy w REDkicie
├── skaner_questow.py          # Główny skrypt skanujący questy (dawniej plik.py)
├── sync_do_git.py             # Automatyczna synchronizacja zmian z REDkita do Git
├── zarzadzaj_zapisami.py      # Zarządzanie profilami zapisów gry (czysty profil testowy)
├── uruchom_redkit.bat         # Szybki launcher REDkita
├── README.md                  # Dokumentacja główna projektu
└── .gitignore                 # Wykluczenia z kontroli wersji
```

---

## 🔍 Narzędzia Pomocnicze (`skaner_questow.py` i inne)

* **`skaner_questow.py`**: Przeszukuje pliki logiki `.w2quest` / `.w2phase` pod kątem flag `roche`, `iorveth`, `side_chosen` i zapisuje wyselekcjonowane pliki w `questy_do_modyfikacji.csv`.
* **`sync_do_git.py`**: Kopiuje zmodyfikowane pliki z katalogu gry bezpośrednio do repozytorium `src/`.
* **`zarzadzaj_zapisami.py`**: Chowa dotychczasowe prywatne zapisy gry, zostawiając czysty folder pod szybkie testowanie moda.
* **`uruchom_redkit.bat`**: Szybkie uruchomienie edytora REDkit.

### Uruchomienie skanera:
```bash
python skaner_questow.py
```
Skrypt przeszukuje strukturę gry w poszukiwaniu odniesień do kluczowych frakcji i flag wyboru (`roche`, `iorveth`, `side_chosen`, `path`), a wynik zapisuje w pliku `raport_questow.csv`.

---

## 📅 Etapy Realizacji Moda

- [x] **Etap 1: Przygotowanie środowiska i nauka REDkita**
  - Instalacja gry, REDkita, edytorów oraz Gita.
  - Inicjalizacja repozytorium i dokumentacji.
- [/] **Etap 2: Analiza struktury gry i flag wyboru (`FactsDB`)**
  - Skanowanie plików `.w2quest` i `.w2scene` pod kątem flag `q108_iorveth_path`, `q108_roche_path`.
  - Identyfikacja punktów zwrotnych w Akcie I i II.
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
