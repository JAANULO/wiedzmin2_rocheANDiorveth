# Specyfikacja Techniczna REDkita (`editor.exe`) i Środowiska Moderskiego

Niniejszy dokument opisuje architekturę pakietu REDkit stworzonego przez **CD Projekt RED**, struktury binarne grafów logiki (`.w2quest` / `.w2phase`), pliki konfiguracyjne (`editor.ini`), komendy narzędziowe oraz procedury rozwiązywania błędów.

---

## 🛠️ 1. Pakiet Narzędzi CD Projekt RED (REDkit Suite)

Zgodnie z oficjalną dokumentacją CDPR, w skład pakietu REDkit wchodzą dedykowane aplikacje zainstalowane w katalogu `bin` gry:

1. **Edytor Świata – World Editor (`editor.exe` / `editor.release.exe`):**
   * Główny program środowiska IDE. Zawiera:
     * **Asset Browser:** Przeglądarka zasobów gry (siatki 3D, poziomy `.w2w`, grafy questów `.w2quest`, sceny `.w2scene`).
     * **Quest Editor:** Wizualny edytor węzłowy logiki zadań.
     * **Scene Editor & Dialogue Editor:** Edytory konwersacji (`.w2dlg`) i scen przerywnikowych (`.w2scene`).
     * **Community Editor:** Edytor stref spawnów, rutyn 24h i zachowań NPC.
     * **Log Window & Filter:** Narzędzia podglądu zdarzeń i filtrowania zasobów.
2. **Wiedźmińskie Studio Skryptów – ScriptStudio (`scriptStudio.release.exe`):**
   * Dedykowane IDE do pisania, kompilacji i debugowania skryptów w języku **Witcher Script** (`.ws`).
3. **Red Strings (`Redstrings.exe`):**
   * Aplikacja do wyszukiwania, edycji i indeksowania ciągów tekstowych oraz wersji językowych gry.
4. **User Content Manager (`userContentManager.exe`):**
   * Program pozwalający na wybór i aktywację poszczególnych modów zainstalowanych w katalogu `UserContent`.
5. **User Content Cooker (`wcc.exe` – Witcher Cooking Commandline):**
   * Narzędzie wiersza poleceń do gotowania i pakowania zasobów moda do postaci produkcyjnej.

---

## ⚙️ 2. Pliki Konfiguracyjne, Uprawnienia i Ścieżki

* **Plik `editor.ini`:**
  * Przechowuje konfigurację edytora (ścieżki do `DepotPath`, język interfejsu, ustawienia pamięci podręcznej oraz parametry widoku).
* **Ścieżki projektu (`tools/config.py`):**
  * Moduł ten automatycznie wykrywa instalację gry na dyskach `C:`, `D:`, `E:` (Steam / GOG) oraz ścieżkę konta użytkownika `~\Documents\Witcher 2\UserContent\mod_hybrid_path`.
* **Uprawnienia Administratora (UAC):**
  * Ze względu na zapisywanie indeksu SQLite w katalogu gry (`bin/depot.db`), `editor.exe` wymaga uruchomienia z wymuszeniem uprawnień Administratora. Służy do tego launcher [tools/uruchom_redkit.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/uruchom_redkit.py).

---

## 🧩 3. Budowa Binarna Grafów Questowych (`.w2quest` / `.w2phase`)

Pliki questowe wykorzystują binarny format zasobów **CR2W (REDEngine Resource v2)**.

### Architektura Chunks i Klasy `CQuestBlock`:
Grafy logiki zbudowane są z połączonych obiektów klas wywodzących się z `CQuestBlock`:

* **`CQuestStartBlock` / `CQuestEndBlock`:** Węzły wejścia i wyjścia sygnału fazy/questu.
* **`CQuestPhaseBlock`:** Węzeł fazy podrzędnej (wskazuje na zewnętrzny plik `.w2phase`).
* **`CQuestFactsDBChangeBlock`:** Węzeł modyfikujący stan w bazie faktów `FactsDB` (właściwości: `FactName`, `Value`, `Operation`).
* **`CQuestFactsDBConditionBlock`:** Purpurowy węzeł warunkowy sprawdzający istnienie/wartość faktu w `FactsDB` (wyjścia `True` / `False`).
* **`CQuestScriptBlock`:** Węzeł wywołujący funkcję skryptową WitcherScript (`.ws`).
* **`CQuestFailBlock`:** Węzeł wysyłający sygnał oblania zadania (`QuestFailed`) do Dziennika.

### Gniazda (Sockets), Nadajniki (Senders) i Odbiorniki (Listeners):
* Sygnały przepływają między gniazdami wyjściowymi (`Output Sockets`) jednego węzła a gniazdami wejściowymi (`Input Sockets`) drugiego.
* Edycja połączeń w REDkicie polega na tworzeniu par relacji socket-to-socket. Usunięcie połączenia z `CQuestFailBlock` chroni quest przed oblaniem.

---

## 🧪 4. Symulacja w Edytorze (PIE) i Rozwiązywanie Błędów

### Play-In-Editor (PIE):
1. Otwórz w edytorze poziom 3D z rozszerzeniem `.w2w` (np. Loc Muinne lub Vergen).
2. Kliknij przycisk **Play** na pasku narzędzi.
3. Klawisze sterujące:
   * **`F1`**: Swobodna kamera.
   * **`F10`**: Wyjście z gry do edytora.
   * **`~`**: Otwarcie konsoli skryptowej i podgląd zdarzeń `FactsDB`.

### Naprawa Bazy Danych (`depot.db` / Code 10):
W przypadku uszkodzenia pliku bazy indeksowej `depot.db` (błąd I/O lub Code 10):
1. Wyłącz `editor.exe`.
2. Zmień nazwę pliku `depot.db` w katalogu `bin` (np. na `depot_old.db`).
3. Uruchom launcher `tools/uruchom_redkit.py` – edytor automatycznie odbuduje czystą bazę indeksową.
