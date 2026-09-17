# Wiedźmin 2: Zabójcy Królów – Mod „Hybrydowa Ścieżka” (Roche & Iorveth)

Modyfikacja do gry *The Witcher 2: Assassins of Kings – Enhanced Edition*, której celem jest umożliwienie graczowi rozegrania zawartości i questów z obu ścieżek fabularnych (Vernona Roche’a oraz Iorwetha) w ramach **jednego przejścia gry**, bez konieczności rozpoczynania nowej rozgrywki.

---

## 📌 O Projekcie

W oryginalnej grze pod koniec Aktu I („Na rozdrożu”) gracz zmuszony jest wybrać pomiędzy współpracą z Vernonem Rochem a pomocą Iorwethowi. Wybór ten drastycznie rozdziela Akt II na dwie wykluczające się lokacje i wątki fabularne (Obóz Kaedweński vs Wolne Miasto Vergen) oraz tworzy wybór ratunku w Akcie III (Triss vs Anais / Filippa).

Niniejsza modyfikacja znosi sztuczną blokadę zawartości, pozwalając na doświadczenie obu historii w pojedynczej kampanii.

---

## 🗺️ Centrum Nawigacji po Dokumentacji (`docs/`)

Projekt posiada ustrukturyzowaną, dedykowaną dokumentację podzieloną na wyspecjalizowane pliki:

* 📘 **[Master Plan Projektu (docs/PLAN_PROJEKTU.md)](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/PLAN_PROJEKTU.md)**  
  Główny przewodnik rozwoju moda, harmonogram etapów (ze szczególnym uwzględnieniem **Etapu 1: Prototypu w Loc Muinne**), instrukcja workflow i zasady integracji.
* 📜 **[Struktura Fabuły, Questy i FactsDB (docs/STRUKTURA_FABULY_OG.md)](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/STRUKTURA_FABULY_OG.md)**  
  Słownik kluczowych faktów logicznych (`FactsDB`), tabelaryczne drzewo questów oraz szczegółowa mapa wyborów, podwyborów i konsekwencji w Akcie III.
* ⚙️ **[Specyfikacja REDkita i Środowiska (docs/SPECYFIKACJA_RED_KIT.md)](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/SPECYFIKACJA_RED_KIT.md)**  
  Kompendium wiedzy o narzędziach CD Projekt RED (World Editor, ScriptStudio, Red Strings, User Content Manager), plikach konfiguracyjnych (`editor.ini`), binarnej budowie grafów CR2W (`CQuestBlock`, gniazda, nadajniki, odbiorniki) i rozwiązywaniu błędu `depot.db` (Code 10).
* 🔬 **[Archiwum Badań i Reverse Engineering (docs/research/INDEX.md)](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/docs/research/INDEX.md)**  
  Indeks raportów z badania narzędzi zewnętrznych `Gibbed.RED`, komend `wcc.exe`, dekompilacji skryptów `.ws` oraz skanowania binarnego.
* 📊 **[Dokumentacja Baz Danych (data/README.md)](file:///c:/Users/PC/Documents/GitHub/wiedzmin2_rocheANDiorveth/data/README.md)**  
  Opis schematu kolumn CSV oraz zestawienie 114 wyselekcjonowanych plików questowych.

---

## 🚀 Szybki Start na Nowym Urządzeniu

Jeśli klonujesz to repozytorium na nowym komputerze, wykonaj 2 proste kroki:

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
├── README.md                              # Główny plik nawigacyjny projektu
├── docs/                                  # Dokumentacja techniczna i planistyczna
│   ├── PLAN_PROJEKTU.md                   # Master Plan projektu i harmonogram
│   ├── SPECYFIKACJA_RED_KIT.md            # Kompendium REDkita, CR2W i depot.db
│   ├── STRUKTURA_FABULY_OG.md             # Słownik FactsDB + Analiza wyborów Aktu III
│   ├── notes.md                           # Notatki techniczne z FactsDB i PoC
│   └── research/                          # Archiwum ekspertyz badawczych i RE
│       ├── INDEX.md                       # Indeks dokumentów badawczych
│       ├── Analiza modyfikacji do gry Wiedźmin 2.pdf
│       └── Claude-Mod_Gibbed_RED.md
├── src/                                   # Zmodyfikowane grafy .w2quest/.w2phase moda
│   ├── 1_act1/                            # Logika wyboru w Akcie I (q108_choice)
│   ├── 2_act2/                            # Obóz Kaedwen, Vergen, Mgła i questy poboczne
│   ├── 3_act3/                            # [PRIORYTET ETAPU 1] Prototyp hybrydy w Loc Muinne (q301/q308)
│   └── meta_quests/                       # Logika dzienników (Postacie, Miejsca, Wspomnienia)
├── data/                                  # Wygenerowane dane i raporty ze skanowania
│   ├── README.md                          # Dokumentacja bazy danych
│   ├── questy_do_modyfikacji.csv          # Wyselekcjonowane 114 kluczowych plików questów
│   └── raport_questow.csv                 # Pełny wygenerowany raport skanera (368 questów)
└── tools/                                 # Skrypty Python oraz launchery narzędziowe
    ├── config.py                          # Centralny plik konfiguracyjny ścieżek
    ├── skaner_questow.py                  # Skaner binarny plików questów gry
    ├── sync_do_git.py                     # Automatyczna synchronizacja zmian z REDkita do Git
    ├── konfiguruj_symlink.py              # Tworzenie dowiązań Junction (UserContent <-> Git)
    ├── zarzadzaj_zapisami.py              # Zarządzanie profilami zapisów gry (czysty profil testowy)
    ├── napraw_redkit_ui.py                # Rebuild bazy indeksowej depot.db
    ├── uruchom_redkit.py / .bat           # Launcher REDkita z prawami Administratora (UAC)
    └── uruchom_gre.py / .bat              # Launcher gry Wiedźmin 2 w trybie -uncooked
```

---

## 🛠️ Skrypty Pomocnicze (`tools/`)

* **`tools/config.py`**: Centralny moduł ścieżek dostępu (Steam / REDkit / UserContent).
* **`tools/skaner_questow.py`**: Przeszukuje pliki logiki `.w2quest` / `.w2phase` i zapisuje wyniki w `data/questy_do_modyfikacji.csv`.
* **`tools/sync_do_git.py`**: Kopiuje zmodyfikowane pliki z katalogu gry bezpośrednio do repozytorium `src/`.
* **`tools/konfiguruj_symlink.py`**: Tworzy dowiązania typu Junction (`mklink /J`) pomiędzy katalogiem `UserContent` REDkita a folderem `src/`.
* **`tools/zarzadzaj_zapisami.py`**: Izoluje prywatne zapisy gry pod czyste środowisko testowe.
* **`tools/napraw_redkit_ui.py`**: Rozwiązuje błąd uszkodzonej bazy `depot.db` (Code 10).
* **`tools/uruchom_redkit.bat` / `uruchom_redkit.py`**: Szybkie uruchomienie edytora REDkit z wymuszeniem uprawnień Administratora (UAC).
* **`tools/uruchom_gre.bat` / `uruchom_gre.py`**: Uruchamia grę Wiedźmin 2 w trybie `-uncooked`.

---

## 📜 Licencja i Prawa Autorskie

Projekt ma charakter fanowski i niekomercyjny. Wszelkie prawa do marki *Wiedźmin* oraz gry *The Witcher 2: Assassins of Kings* należą do **CD PROJEKT RED**.
