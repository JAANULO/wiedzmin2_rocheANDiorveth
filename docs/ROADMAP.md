# Przewodnik Rozwoju Moda: Wiedźmin 2 – Hybrydowa Ścieżka (Roche & Iorveth)

---

## 1. Podsumowanie Stanu Projektu (Co już zrobiono)

### 📁 Środowisko i Repozytorium Git
* Utworzono strukturę plikową: `README.md`, `.gitignore`, `docs/notes.md`, `docs/ROADMAP.md` oraz ustrukturyzowane commity.
* Zmodyfikowane pliki moda z REDkita trafiają do katalogu: `src/`
* Dane i wyniki skanowania logiki gry zapisane są w: `data/questy_do_modyfikacji.csv` oraz `data/raport_questow.csv`.

### 🛠️ Stworzone Narzędzia Pomocnicze (`tools/`)
* **[tools/skaner_questow.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/skaner_questow.py)** – skaner plików binarnych gry (wyselekcjonował 114 kluczowych questów).
* **[tools/sync_do_git.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/sync_do_git.py)** – kopiuje zmodyfikowane w REDkicie pliki gry prosto do `src/`.
* **[tools/konfiguruj_symlink.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/konfiguruj_symlink.py)** – tworzy dowiązania Junction (`UserContent` <-> `src/`) dla automatycznego zapisu.
* **[tools/zarzadzaj_zapisami.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/zarzadzaj_zapisami.py)** – chowa stare prywatne zapisy pod czyste testowanie moda.
* **[tools/uruchom_redkit.bat](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/uruchom_redkit.bat) / `.py`** – launcher REDkita z uprawnieniami Administratora (UAC).
* **[tools/uruchom_gre.bat](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/uruchom_gre.bat) / `.py`** – launcher gry Wiedźmin 2 w trybie `-uncooked`.
* **[tools/config.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/config.py)** – centralna konfiguracja ścieżek projektu.

### 📦 Wykonane Edycje w REDkicie (Zapisane w Git)
* **`src/1_act1/q108_choice.w2phase`** – Zduplikowano sygnały wyjściowe z węzła `choice` (wypuszcza sygnał przez zduplikowane strzałki `with_Iorweth` i `with_Roche` oraz nadaje oba fakty `q108_helping_roche` i `q108_helping_scoia`).
* **`src/2_act2/act 2.w2quest`** – Przepięto bramkę wejściową Aktu II (sygnał po wjeździe do Aktu II uruchamia jednocześnie obóz Vergen i Kaedwen).
* **`src/2_act2/`** – Zsynchronizowano pliki questów pobocznych: `sq202_burned_village`, `sq204_dice`, `sq205i_handwrestling`, `sq206i_fistfight`.
* **`src/meta_quests/`** – Zsynchronizowano pliki dzienników: `characters_journal.w2phase`, `places_jurnal.w2phase`, `lost_memories.w2phase`.

### 🔬 Przebadane Dokumenty i Narzędzia Zewnętrzne (RE)
* **`Analiza modyfikacji do gry Wiedźmin 2.pdf`** – Przebadano diagnozę bazy danych REDkit (`depot.db`), strukturę katalogów questowych oraz procedurę testowania symulacji w edytorze (Play-In-Editor – PIE z poziomami `.w2w`).
* **`Claude-Mod do Wiedźmina 2 z narzędziami Gibbed.RED-20260916-1555.md`** – Przeanalizowano przydatność narzędzi `yole/Gibbed.RED` (`ScriptDecompiler`) oraz komend `wcc.exe`. Potwierdzono, że **String Extraction** w Pythonie (`skaner_questow.py`) to optymalne podejście do selekcji questów w formacie binarnym CR2W.

---

## 2. Kolejne Kroki do Wykonania (Plan Działania)

### KROK 1: TEST W GRZE (Weryfikacja Rozdroża i Aktu II)
1. Uruchom grę Wiedźmin 2 w trybie `-uncooked` za pomocą [tools/uruchom_gre.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/uruchom_gre.py) lub `tools/uruchom_gre.bat`.
2. Wczytaj zapis z Aktu I (przed wyborem u Roche'a/Iorwetha).
3. Wykonaj akcję z Rochem i przejdź do Aktu II.
4. Sprawdź w Dzienniku (`J`):
   * Czy quest Iorwetha **NIE ZOSTANIE OBLANY** w Akcie I?
   * Czy po wylądowaniu w Akcie II aktywują się wątki obu obozów?

### KROK 2: SYSTEM FRAKCJI I WROGOŚCI NPC (Akt II)
* Jeśli po wejściu do obozu Kaedweńczyków lub Vergen strażnicy atakują Geralta, modyfikujemy nastawienie frakcji (`Factions`) w plikach:
  * `data/game/2_act2/act2_community_camp_spawn.w2phase`
  * `data/game/2_act2/act2_community_vergen_spawn.w2phase`
  lub ustawiamy w skrypcie `QSetGroupAttitude` nastawienie neutralne/friendly.

### KROK 3: NAWIGACJA PRZEZ MGŁĘ I SEKWENCJA QUESTÓW POBOCZNYCH
* Umożliwienie swobodnego przechodzenia przez Mgłę w Akcie II (modyfikacja `q208_draug.w2phase`).
* Weryfikacja questów głównej linii obu stron (Saskia vs Henselt).

---

## 3. Prompt Startowy do Nowej Rozmowy z AI

> "Cześć! Kontynuujemy pracę nad modem do gry Wiedźmin 2: Zabójcy Królów (Hybrydowa ścieżka Roche/Iorweth).  
> Całe repozytorium jest już ustrukturyzowane i zcommitowane w Gicie.  
> Mamy wykonane i zsynchronizowane w `src/` kluczowe pliki questów:  
> 1. `src/1_act1/q108_choice.w2phase` (rozgałęzienie Aktu I)  
> 2. `src/2_act2/act 2.w2quest` (podwójny start obozów Vergen i Kaedwen w Akcie II)  
> 3. `src/2_act2/` oraz `src/meta_quests/` (questy poboczne i dzienniki)  
> 4. `data/questy_do_modyfikacji.csv` (wyselekcjonowane 114 questów pod dalsze prace)  
> Przeczytaj plik `docs/ROADMAP.md` oraz `docs/notes.md` i pomóż mi przejść do kolejnego kroku."
