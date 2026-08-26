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

## 🧪 Dziennik Testów i Prototypów (PoC)

* **Mechanika oryginalna (Flotsam):** W unmodowanej grze oba zadania („Na rozstajach: Iorweth” i „Na rozstajach: Roche”) są aktywne równolegle w Dzienniku pod koniec Aktu I. Podjęcie akcji u jednego lidera natychmiast wysyła sygnał `QuestFailed` do drugiego.
* **Cel Modyfikacji w `q108_choice.w2phase`:** Usunięcie strzałki prowadzącej do bloku `QuestFailed` dla Iorwetha po rozpoczęciu misji u Roche'a (i analogicznie dla Roche'a przy misji Iorwetha). Dzięki temu oba zadania pozostaną aktywne i wykonalne.
