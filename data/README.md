# Dokumentacja Baz Danych Questów (`data/`)

Katalog `data/` zawiera wygenerowane raporty i bazy danych binarnego skanowania plików gry *Wiedźmin 2: Zabójcy Królów*.

---

## 📁 1. Wykaz Plików

* **`questy_do_modyfikacji.csv`:**  
  Baza **114 wyselekcjonowanych questów i faz** posiadających odniesienia do logiki wyboru ścieżek (`roche`, `iorveth`, `side_chosen`, `path`). Stanowi fundament pod dalsze edycje w REDkicie.
* **`raport_questow.csv`:**  
  Pełny, wygenerowany przez [tools/skaner_questow.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/skaner_questow.py) raport skanowania binarnego zawierający analizę wszystkich **368 plików `.w2quest` i `.w2phase`** w strukturze gry.

---

## 📊 2. Opis Pól i Kolumn w Plikach CSV

| Nazwa Kolumny | Opis Zawartości | Przykładowa Wartość |
| :--- | :--- | :--- |
| **`file_path`** | Względna ścieżka do pliku grafu questu w strukturze gry | `2_act2/act 2.w2quest` |
| **`category`** | Zaklasyfikowany moduł fabularny gry | `Akt II - Obóz Kaedwen` |
| **`matched_keywords`** | Odnalezione w pliku binarnym słowa kluczowe i fakty | `q108_helping_roche, iorveth` |
| **`status`** | Status modyfikacji w repozytorium | `ZMODYFIKOWANE` / `DO EDYCJI` |

---

## 🔍 3. Skanowanie Binarne (`skaner_questow.py`)

Skrypt przeszukuje strukturę binarną plików CR2W metodą wyciągania ciągów tekstowych (`String Extraction` w Pythonie), wyłapując identyfikatory faktów i nazw węzłów bez konieczności pełnej dekompilacji.
