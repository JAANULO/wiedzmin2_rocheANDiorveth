# Analiza Prac i Raport PoC – Wiedźmin 2: Hybrydowa Ścieżka
**Data raportu:** 17 września 2026 r.  
**Projekt:** *The Witcher 2: Assassins of Kings – Mod „Hybrydowa Ścieżka” (Roche & Iorveth)*  
**Autor / Zespół:** JAANULO & Antigravity AI  

---

## 📌 1. Podsumowanie Celu Projektu

Głównym celem modyfikacji jest zniesienie sztucznej blokady fabularnej w grze *Wiedźmin 2: Zabójcy Królów*, która zmusza gracza pod koniec Aktu I do wyboru pomiędzy współpracą z Vernonem Rochem a pomocą Iorwethowi. Modyfikacja zmierza do umożliwienia rozegrania zawartości obu ścieżek (Vergen i Obóz Kaedweński) oraz wykonania zadań z obu linii fabularnych w ramach **jednego przejścia gry**.

---

## 🧪 2. Wyniki Przeprowadzonego Testu Poligonowego (Proof of Concept – PoC)

W ramach dzisiejszej sesji przetestowano mechanikę nieliniowych wyborów na odizolowanym i skoncentrowanym obszarze **Aktu III (Loc Muinne)** – wybór pomiędzy ratowaniem **Triss Merigold** (`q304_triss`) a ratowaniem **Filippy Eilhart** (`q305_dagger` – zadanie *„Łamacz czarów”*) lub **Anais La Valette** (`q303_bastards`).

### 🔬 Przebieg prac i modyfikacji grafów w REDkicie:

1. **Analiza Struktury Grafów Aktu III**:
   * Zidentyfikowano główny korzeń Aktu III: `data/game/3_act3/act 3.w2quest`.
   * Odnaleziono fazy startowe: `q301_start_pro_roche.w2phase` oraz `q302_start_pro_iorweth.w2phase`.
   * Rozpracowano powiązania węzłów:
     * `q302_start_pro_iorweth` posiada wyjścia `filippa_out` oraz `shilard_out`.
     * `q305_Dagger` – faza zdobycia sztyletu i odczarowania Saskii (*„Łamacz czarów”*).
     * `q304_Triss` – faza ratowania Triss z obozu Nilfgaardu (wejścia `through_gate` oraz `through_prison`).

2. **Wykonane Edycje Grafów (`.w2phase` i `.w2quest`)**:
   * **Zduplikowanie Sygnałów Wyjściowych**: W węźle wyboru po rozmowie z Radowidem (`after meeting with radowid`) połączono wyjścia `Out triss` oraz `Out bastards` / `filippa_out` z obydwoma zielonymi łącznikami `In Out`.
   * **Przepięcie Aktywacji Fazy `q304_Triss`**: W głównym grafie `act 3.w2quest` połączono wyjście `filippa_out` (oraz wyjście `Out` z `q305_Dagger`) bezpośrednio z gniazdem `through_gate` klocka `q304_Triss`.
   * **Usunięcie Sygnałów Oblania Questów (`QuestFailed`)**: Odłączono krawędzie wysyłające sygnał niepowodzenia do drugiego zadania.

3. **Rezultat Testu w Grze (100% SUKCES)**:
   * **Zadania w Dzienniku**: Po pójściu z Filippą i ukończeniu questu *„Łamacz czarów”*, zadanie **„Gdzie jest Triss Merigold?” NOT OBLANE** i pozostało aktywne w Dzienniku.
   * **Świat Gry i Spawny**: Obóz Nilfgaardczyków został prawidłowo zespawnowany wraz z Szilardem Fitz-Osterlenem i strażnikami przy bramie, umożliwiając kontynuację odbijania Triss.
   * **Wniosek**: Przepinanie sygnałów wyjściowych w grafach `.w2phase` pozwala na pełne rozbicie sztucznych wykluczeń fabularnych silnika REDengine.

---

## 🛠️ 3. Optymalizacja Środowiska i Przyspieszenie Ładowania

Przeprowadzono analizę i wdrożono optymalizacje wydajnościowe dla gry oraz edytora REDkit:

1. **Flaga `-novideos`**:
   * Zaktualizowano skrypty launchera [`tools/uruchom_gre.py`](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/uruchom_gre.py) oraz [`tools/uruchom_gre.bat`](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/uruchom_gre.bat) o flagę `-novideos`.
   * Uruchamianie gry z tą flagą pomija filmiki startowe producentów, ładując grę od razu do menu głównego.
2. **Obsługa Kodowania UTF-8**:
   * Naprawiono błędy `UnicodeEncodeError` w konsoli Windows PowerShell, dodając automatyczne rekonfigurowanie `sys.stdout` w skryptach Pythona.
3. **Zarządzanie Pamięcią i Zapisami**:
   * Przeanalizowano wpływ starych plików zapisów w `Documents\Witcher 2\gamesaves` na czas ładowania. Skrypt [`tools/zarzadzaj_zapisami.py`](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/zarzadzaj_zapisami.py) pozwala skrócić czas skanowania zapisów z kilkudziesięciu sekund do około 3 sekund.
   * Wyjaśniono architekturę pamięci RAM dla procesu 32-bitowego (`witcher2.exe` / `editor.exe` max 4 GB) oraz rolę systemowego cache Windows (SysMain) przy 32 GB RAM.

4. **Katalogi Map 3D w REDkicie (`.w2w`)**:
   Zmapowano i udokumentowano ścieżki głównych poziomów 3D do testów w trybie PIE (Play-In-Editor):
   * **Akt III (Loc Muinne):** `levels/04_city/world.w2w`
   * **Akt II (Kaedwen / Vergen):** `levels/03_camp/world.w2w`
   * **Akt I (Flotsam):** `levels/l02-port/L02-port.w2w`
   * **Prolog (Zamek La Valette):** `levels/l01-keep/L01-keep.w2w`

---

## 📦 4. Aktualny Stan Zasobów Zsynchronizowanych w `src/`

Wszystkie edycje z edytora REDkit trafiają w czasie rzeczywistym do repozytorium dzięki dowiązaniu typu Junction (`python tools/konfiguruj_symlink.py`):

```
src/
├── 1_act1/
│   └── q108_choice.w2phase            # Modyfikacja rozdroża we Flotsam (Roche & Iorweth)
├── 2_act2/
│   ├── act 2.w2quest                  # Główna bramka wejściowa (start obozów Vergen + Kaedwen)
│   ├── sq202_burned_village.w2phase   # Questy poboczne Aktu II
│   ├── sq204_dice.w2phase
│   ├── sq205i_handwrestling.w2phase
│   └── sq206i_fistfight.w2phase
├── meta_quests/
│   ├── characters_journal.w2phase     # Meta-questy i wpisy w Dzienniku
│   ├── places_jurnal.w2phase
│   └── lost_memories.w2phase
```

---

## 🚀 5. Następne Kroki w Projekcie

1. **Akt I – Wybór Ścieżki (`q108_choice.w2phase`)**:
   * Zastosowanie przetestowanej w Akcie III metodyki do rozdroża w Akcie I, zapewniając nie-odrzucanie questa drugiej frakcji.
2. **Akt II – Hybrydowy Obóz i Wrogość Frakcji (`act 2.w2quest`)**:
   * Przetestowanie zachowania NPC i strażników w Vergen oraz obozie Kaedweńskim (korekta `Factions` / `QSetGroupAttitude`).
   * Zapewnienie przechodzenia przez Mgłę (`q208_draug.w2phase`).
3. **Weryfikacja Kompatybilności Zapisów i Zwieńczenie**:
   * Przetestowanie pełnego przejścia wątków od Aktu I do Aktu III na zmodowanym zapisie gry.

---
*Raport wygenerowany automatycznie i zapisany w repozytorium projektu w pliku [`docs/analiza_prac_2026-09-17.md`](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/analiza_prac_2026-09-17.md). Zobacz również szczegółowe podsumowanie diagnozy REDkita w [`docs/podsumowanie_prac_2026-09-17.md`](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/podsumowanie_prac_2026-09-17.md).*
