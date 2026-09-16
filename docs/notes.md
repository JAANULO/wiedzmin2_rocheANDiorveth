# Notatki Techniczne i Rejestr Faktów (FactsDB)

Niniejszy plik służy do dokumentowania konkretnych faktów z bazy `FactsDB` oraz struktury węzłów questowych odnalezionych podczas analizy w REDkicie.

---

## 🔑 Rejestr Zidentyfikowanych Faktów (FactsDB)

| Nazwa Faktu (Fact ID) | Opis / Węzeł w REDkicie | Wpływ na świat gry / Questy |
| :--- | :--- | :--- |
| **`q108_helping_scoia`** | Węzeł `FactsDB Change` na górnej ścieżce `q108_choice` | Ustawiany przy pomocy Iorwethowi (Wiewiórkom) |
| **`q108_helping_roche`** | Węzeł `FactsDB Change` na dolnej ścieżce `q108_choice` | Ustawiany przy pomocy Roche'owi (Niebieskim Pasom) |
| `QSetGroupAttitude` | Węzeł skryptowy (górna ścieżka Iorwetha) | Zmienia nastawienie `player scoia_marauders` na `friendly` |
| `q108_after_choice_after_massacre` | Łącznik po wyborze Iorwetha | Prowadzi do wyjścia `with_Iorweth` |
| `q108_after_choice_no_massacre` | Łącznik po wyborze Roche'a | Prowadzi do wyjścia `with_Roche` |

---

## 🗺️ Główny Graf Aktu II (`act 2.w2quest`) - ODKRYCIE BAZOWE

Zidentyfikowane w REDkicie bramki wejściowe Aktu II:
1. **Węzeł startowy `Start` (Czerwona strzała):** Rozdziela sygnał startowy na dzienniki (`characters_journal`, `places_journal`) oraz kieruje sygnał do głównej bramki decyzyjnej.
2. **Purpurowy Trójkąt `Condition` (Bramka Główna):**
   * Wyjście **`True`** $\rightarrow$ aktywuje blok **`act 2 vergen` / `vergen`** (Ścieżka Iorwetha).
   * Wyjście **`False`** $\rightarrow$ aktywuje blok **`act 2 camp` / `camp`** (Ścieżka Roche'a w obozie Kaedwen) oraz odtwarzacz muzyki.

---

## 📊 Wyniki Skanowania Binardnego i Selektora Questów (`data/questy_do_modyfikacji.csv`)

Na podstawie analizy struktur logiki gry za pomocą `skaner_questow.py` wyselekcjonowano **114 kluczowych plików `.w2quest` / `.w2phase`**, stanowiących fundament pod dalsze modyfikacje:

| Kategoria | Liczba Wyselekcjonowanych Plików | Kluczowe Pliki / Obszary |
| :--- | :---: | :--- |
| **Akt I - Wybór Ścieżki (Na Rozdrożu)** | 10 | `q108_choice.w2phase`, `3_q106_act1.w2quest`, `4_act1_from_choice.w2quest` |
| **Akt II - Ścieżka Roche'a** | 22 | `q210r_*`, `q211r_*`, `q213r_*`, `q214r_*`, `q215r_*` |
| **Akt II - Ścieżka Iorwetha** | 35 | `q202_*`, `q203_*`, `q205_*`, `act2_community_vergen_spawn.w2phase` |
| **Akt II - Główne Zadania / Mgła** | 29 | `q201_kings_meet.w2phase`, `q208_ghost_of_banner.w2phase`, `a2_fog_transition.w2phase` |
| **Akt III - Kontynuacja i Finał** | 8 | `q301_*`, `q308_*` |
| **Główny Korzeń Gry / Aktu** | 4 | `witcher2.w2quest`, `act_1.w2quest`, `act 2.w2quest`, `act 3.w2quest` |

---

## 📦 Zsynchronizowane Zasoby Moda w `src/`

Prace zrealizowane i zczytane z edytora REDkit:

1. **Logika wyboru (Akt I):**
   * `src/1_act1/q108_choice.w2phase` – przepięcie wyjść i podwójna flaga (`q108_helping_roche` + `q108_helping_scoia`).
2. **Główny Graf (Akt II):**
   * `src/2_act2/act 2.w2quest` – jednoczesne uruchomienie obozów `vergen` i `camp`.
3. **Questy Poboczne Aktu II:**
   * `src/2_act2/sq202_burned_village.w2phase` & `sq202_press_phase.w2phase` (Spalone miasteczko / Rozlewisko).
   * `src/2_act2/sq204_dice.w2phase` (Kości).
   * `src/2_act2/sq205i_handwrestling.w2phase` (Siłowanie na rękę).
   * `src/2_act2/sq206i_fistfight.w2phase` (Walki na pięści).
4. **Meta-Questy / Dziennik:**
   * `src/meta_quests/characters_journal.w2phase` (Dziennik postaci).
   * `src/meta_quests/places_jurnal.w2phase` (Dziennik miejsc).
   * `src/meta_quests/lost_memories.w2phase` (Wspomnienia Geralta).

---

## 🧪 Dziennik Testów i Prototypów (PoC)

* **Mechanika oryginalna (Flotsam):** W unmodowanej grze oba zadania („Na rozstajach: Iorweth” i „Na rozstajach: Roche”) są aktywne równolegle w Dzienniku pod koniec Aktu I. Podjęcie akcji u jednego lidera natychmiast wysyła sygnał `QuestFailed` do drugiego.
* **Cel Modyfikacji w `q108_choice.w2phase`:** Usunięcie strzałki prowadzącej do bloku `QuestFailed` dla Iorwetha po rozpoczęciu misji u Roche'a (i analogicznie dla Roche'a przy misji Iorwetha). Dzięki temu oba zadania pozostaną aktywne i wykonalne.

---

## 🔬 Analiza Narzędzi Zewnętrznych i Inżynierii Wstecznej (Reverse Engineering)

Na podstawie badań udokumentowanych w pliku [Claude-Mod do Wiedźmina 2 z narzędziami Gibbed.RED-20260916-1555.md](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/Claude-Mod%20do%20Wied%C5%BAmina%202%20z%20narz%C4%99dziami%20Gibbed.RED-20260916-1555.md):

1. **Ocena Repozytoriów Gibbed.RED:**
   * **`gibbed/Gibbed.RED` (oryginał):** Archiwalny zestaw narzędzi (pakowanie/rozpakowywanie `.dzip`, tabele stringów, `ResourceEdit`). Brak aktywnego rozwoju.
   * **`yole/Gibbed.RED` (fork Dmitry Jemerova):** Rekomendowana wersja. Zawiera dodatkowo **`Gibbed.RED.ScriptDecompiler`** (dekompilator skryptów `.ws` WitcherScript) oraz narzędzie `Gibbed.RED.Diff`.
   * **Struktura `.w2quest` / CR2W:** Pliki `.w2quest` w REDkicie korzystają z binarnego formatu CR2W. Gibbed.RED potrafi parsować surową tabelę chunków i właściwości CR2W, lecz nie posiada klas typowanych (`CQuest`, `CQuestBlock`) interpretujących semantykę węzłów grafu i połączeń socket-to-socket.
2. **Ewaluacja Komend `wcc.exe` (Witcher Cooking Commandline):**
   * Przebadano komendy `wcc.exe` (`cook2`, `reslinker`, `cookEditor`, `listEffects` itp.).
   * Żadna ze standardowych komend `wcc.exe` nie oferuje opcji eksportu / dekompilacji binarnego grafu `.w2quest` do czytelnego formatu tekstowego (XML/JSON).
3. **Uzasadnienie Wyboru Skanera Binarnego (`skaner_questow.py`):**
   * Wyciąganie tekstów metodą **String Extraction** z binarnych plików `.w2quest` przy użyciu Python regex (`re.findall(b'[a-zA-Z0-9_]{4,}', ...)`) okazało się najszybszym i najbardziej niezawodnym sposobem wyselekcjonowania 114 questów zależnych od ścieżek fabularnych bez konieczności inżynierii wstecznej silnika serializacji CR2W.

---

## 🛠️ Diagnoza Środowiska REDkit i Procedury Testowe (PIE)

Na podstawie dokumentu [Analiza modyfikacji do gry Wiedźmin 2.pdf](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/Analiza%20modyfikacji%20do%20gry%20Wied%C5%BAmin%202.pdf):

1. **Rozwiązywanie Błędów Bazy Danych REDkit (Database Corruption / Code 10):**
   * W przypadku błędu odczytu bazy lub I/O, należy upewnić się, że REDkit jest wyłączony, a następnie zmienić nazwę pliku pamięci podręcznej bazy (np. `depot.db` $\rightarrow$ `depot_old.db` w katalogu gry lub `bin`).
   * Ponowne uruchomienie `redkit.exe` jako Administrator wymusza pełny rebuild bazy danych bez utraty plików źródłowych.
2. **Procedura Uruchamiania Symulacji w Edytorze (Play-In-Editor – PIE):**
   * Sama edycja grafu `.w2q` / `.w2quest` nie pozwala na uruchomienie symulacji – silnik wymaga załadowanego otoczenia 3D.
   * W oknie *Asset Browser* należy otworzyć plik świata/poziomu z rozszerzeniem `.w2w` (np. Dolina Pontaru / Vergen / Obóz).
   * Kliknięcie ikonki **Play** na głównym pasku narzędzi kompiluje skrypty w locie i uruchamia lokalną instancję gry w oknie *Viewport*.
3. **Skróty Klawiszowe w Trybie Testowym (PIE):**
   * `F10` – Wyjście z trybu gry i powrót do edytora.
   * `F1` – Przełączenie na tryb wolnej kamery (Free Camera).
   * `Pause / Break` – Wstrzymanie symulacji gry.


