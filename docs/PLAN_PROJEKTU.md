# Master Plan Projektu: Wiedźmin 2 – Hybrydowa Ścieżka (Roche & Iorveth)

Niniejszy dokument stanowi główny przewodnik rozwoju modyfikacji, definiuje cele projektu, podział na etapy wdrożeniowe, procedury automatyzacji oraz wykaz 114 kluczowych plików questowych.

---

## 🎯 1. Cel i Założenia Projektowe

Wyeliminowanie sztucznej blokady fabularnej w gry *Wiedźmin 2: Zabójcy Królów*, umożliwiając graczowi ukończenie wątków i zadań obu frakcji (Vernona Roche'a oraz Iorwetha) w **pojedynczej kampanii**.

---

## 📅 2. Harmonogram Etapów Wdrożeniowych (Milestones)

### 🚀 ETAP 1 (PRIORYTET): Prototyp i Rozgrzewka w Akcie III (Loc Muinne)
* **Cel:** Testowanie pełnego cyklu modyfikacji na mniejszym obszarze.
* **Zadania:**
  1. Odblokowanie symultanicznego wykonania zadania **„Gdzie jest Triss Merigold?”** oraz zadań frakcyjnych (**„Łamacz czarów”** / **„Za Temerię!”**).
  2. Weryfikacja spójności Dziennika i dialogów końcowych.
  3. Testy w trybie **Play-In-Editor (PIE)** oraz z czystym zapisem z [tools/zarzadzaj_zapisami.py](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/tools/zarzadzaj_zapisami.py).

### ⚔️ ETAP 2: Hybrydyzacja Aktu I i II (Rozdroże, Vergen i Obóz Kaedwen)
* **Zadania:**
  1. Zduplikowanie wyjść w `q108_choice.w2phase` (wykonane w `src/1_act1/`).
  2. Aktywacja obu obozów w `act 2.w2quest` (wykonane w `src/2_act2/`).
  3. Dostosowanie nastawień frakcji (`act2_community_*_spawn.w2phase`) oraz odblokowanie swobodnego przechodzenia przez Mgłę (`a2_fog_transition.w2phase`).
  4. Modyfikacja 114 wyselekcjonowanych questów pobocznych i głównych z [data/questy_do_modyfikacji.csv](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/data/questy_do_modyfikacji.csv).

---

## 🔄 3. Procedury Automatyzacji i Workflow

```mermaid
flowchart LR
    A["REDkit (editor.exe)"] -->|Zapis pliku| B["UserContent/mod_hybrid_path"]
    B <-->|Junction Symlink (konfiguruj_symlink.py)| C["src/ (Repozytorium Git)"]
    C -->|Git Commit| D["GitHub Repository"]
    C -->|Sync / Launch| E["Wiedźmin 2 (-uncooked)"]
```

1. **Konfiguracja Środowiska (Jednorazowo):**
   ```bash
   python tools/konfiguruj_symlink.py
   ```
2. **Praca w REDkicie:**
   * Uruchom launcher `tools/uruchom_redkit.bat` lub `tools/uruchom_redkit.py`.
   * Edycja plików grafów w edytorze – zapis trafia od razu do `src/`.
3. **Testowanie w Grze:**
   * Uruchom grę w trybie `-uncooked` przez `tools/uruchom_gre.bat` lub `tools/uruchom_gre.py`.
4. **Zapisanie Postępów:**
   ```bash
   git add src/
   git commit -m "feat(act3): odblokowano symultaniczny ratunek Triss i Filippy"
   ```

---

## 📚 4. Odnośniki do Dokumentacji Pomocniczej

* 📘 [docs/SPECYFIKACJA_RED_KIT.md](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/SPECYFIKACJA_RED_KIT.md) – Opis pakietu REDkit, `.ini`, budowa grafów CR2W i naprawa `depot.db`.
* 📜 [docs/STRUKTURA_FABULY_OG.md](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/STRUKTURA_FABULY_OG.md) – Słownik `FactsDB` oraz pełne drzewo questów i wyborów Aktu III.
* 📊 [data/README.md](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/data/README.md) – Opis schematu bazy 114 questów.
* 🔬 [docs/research/INDEX.md](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/research/INDEX.md) – Archiwum badań Reverse Engineering i narzędzi Gibbed.RED.
