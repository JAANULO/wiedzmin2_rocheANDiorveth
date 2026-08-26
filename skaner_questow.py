import os
import csv
import re

# Konfiguracja ścieżki gry
SCIEZKA_BAZOWA = r"C:\SteamLibrary\steamapps\common\the witcher 2\data\game"

# Pliki docelowe raportu
PLIK_WYNIKOWY = "questy_do_modyfikacji.csv"

# Tylko pliki grafów i faz questów (omijamy sceny dialogowe .w2scene, voicesety i rozmowy tła)
ROZSZERZENIA_LOGIKI = (".w2quest", ".w2phase")

# Wykluczane katalogi generujące szum (np. odgłosy tłumu, czaty tła)
KATALOGI_IGNOROWANE = ["voicesets", "chats", "community_soldiers", "community_town", "ambient"]

# Flagi i identyfikatory bezpośrednio powiązane z wyborem ścieżki i blokadami questów
FLAGI_SCIEZEK = [
    "q108", "side_chosen", "iorveth_path", "roche_path",
    "q201", "q202", "q210r", "q211r", "q213r", "q214r", "q215r",
    "q203", "q205", "q207", "q208", "q301", "q308"
]

def kategoryzuj_quest(nazwa_pliku, sciezka, wykryte_flagi):
    nazwa_l = nazwa_pliku.lower()
    sciezka_l = sciezka.lower()
    
    if nazwa_l in ("witcher2.w2quest", "act_1.w2quest", "act 2.w2quest", "act 3.w2quest"):
        return "Główny Korzeń Gry / Aktu"
    elif "q108" in wykryte_flagi or "q108" in sciezka_l or "side_chosen" in wykryte_flagi:
        return "Akt I - Wybór Ścieżki (Na Rozdrożu)"
    elif any(f in wykryte_flagi for f in ["q210r", "q211r", "q213r", "q214r", "q215r", "roche_path"]) or "roche" in sciezka_l:
        return "Akt II - Ścieżka Roche'a"
    elif any(f in wykryte_flagi for f in ["q202", "q203", "q205", "iorveth_path"]) or "vergen" in sciezka_l or "iorveth" in sciezka_l:
        return "Akt II - Ścieżka Iorwetha"
    elif "q201" in wykryte_flagi or "q207" in wykryte_flagi or "q208" in wykryte_flagi or "2_act2" in sciezka_l:
        return "Akt II - Główne Zadania / Mgła"
    elif "3_act3" in sciezka_l or "q301" in wykryte_flagi or "q308" in wykryte_flagi:
        return "Akt III - Kontynuacja i Finał"
    else:
        return "Pozostałe Zadania Ścieżek"

def skanuj_kluczowe_questy(katalog_startowy, plik_wyjsciowy):
    wyniki = []
    przeszukane_pliki = 0
    
    print("=" * 70)
    print(" SKANOWANIE KLUCZOWYCH QUESTÓW DO MODYFIKACJI (Wiedźmin 2)")
    print("=" * 70)
    print(f"Katalog źródłowy: {katalog_startowy}\n")
    
    for root, dirs, files in os.walk(katalog_startowy):
        # Omijanie katalogów generujących szum
        if any(ign in root.lower() for ign in KATALOGI_IGNOROWANE):
            continue
            
        for file in files:
            if file.lower().endswith(ROZSZERZENIA_LOGIKI):
                przeszukane_pliki += 1
                pelna_sciezka = os.path.join(root, file)
                znalezione_flagi = set()
                
                try:
                    with open(pelna_sciezka, 'rb') as f:
                        zawartosc_binarna = f.read().lower()
                        
                        # Sprawdzanie obecności kluczowych flag
                        for flaga in FLAGI_SCIEZEK:
                            if flaga.encode('ascii') in zawartosc_binarna:
                                znalezione_flagi.add(flaga)
                                
                except Exception as e:
                    print(f"Błąd odczytu {file}: {e}")
                
                # Dodajemy plik jeśli zawiera kluczowe flagi lub jest głównym plikiem Aktu
                is_main_act_file = file.lower() in ("witcher2.w2quest", "act_1.w2quest", "act 2.w2quest", "act 3.w2quest")
                
                if znalezione_flagi or is_main_act_file:
                    kategoria = kategoryzuj_quest(file, pelna_sciezka, list(znalezione_flagi))
                    wyniki.append({
                        "Kategoria": kategoria,
                        "Plik": file,
                        "Wykryte_Flagi": ", ".join(sorted(znalezione_flagi)) if znalezione_flagi else "Główny_Graf",
                        "Sciezka": pelna_sciezka
                    })
                    
    # Sortowanie wyników według kategorii i nazwy pliku
    wyniki.sort(key=lambda x: (x["Kategoria"], x["Plik"]))
    
    # Generowanie wyfiltrowanego raportu CSV
    with open(plik_wyjsciowy, 'w', newline='', encoding='utf-8') as csvfile:
        pola = ["Kategoria", "Plik", "Wykryte_Flagi", "Sciezka"]
        writer = csv.DictWriter(csvfile, fieldnames=pola)
        
        writer.writeheader()
        for w in wyniki:
            writer.writerow(w)

    # Wyświetlenie wyfiltrowanych wyników w konsoli
    kategorie_dict = {}
    for r in wyniki:
        kat = r["Kategoria"]
        kategorie_dict[kat] = kategorie_dict.get(kat, 0) + 1

    print(" ZAKOŃCZONO FILTROWANIE!")
    print(f" Przeszukano plików logiki (.w2quest/.w2phase): {przeszukane_pliki}")
    print(f" Wyselekcjonowano KLUCZOWYCH plików do edycji: {len(wyniki)}\n")
    print(" Podsumowanie według kategorii:")
    for kat, count in kategorie_dict.items():
        print(f"   • {kat}: {count} plików")
        
    print(f"\n Wyfiltrowana lista została zapisana do: {plik_wyjsciowy}")

if __name__ == "__main__":
    skanuj_kluczowe_questy(SCIEZKA_BAZOWA, PLIK_WYNIKOWY)