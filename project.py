from recept import Recept
from ingredient import Ingredient
from stap import Stap


def toon_menu():
    print("\n--- Receptenboek ---")
    print("1. Toon overzicht van recepten")
    print("2. Voeg recept toe")
    print("3. Exit")
    keuze = input("Kies een optie (1/2/3): ").strip()
    return keuze


def toon_recepten(recepten):
    if not recepten:
        print("Er zijn nog geen recepten beschikbaar.")
        return

    print("\nBeschikbare recepten:")
    for i, r in enumerate(recepten, start=1):
        print(f"{i}. {r}")

    try:
        keuze = int(input("\nKies een receptnummer: "))
        if 1 <= keuze <= len(recepten):
            aantal = int(input("Voor hoeveel personen? "))
            recepten[keuze - 1].set_aantal_personen(aantal)

            plantaardig_keuze = input("Plantaardige versie? (ja/nee): ").strip().lower() == "ja"
            recepten[keuze - 1].toon_recept(plantaardig=plantaardig_keuze)

            # Optie om te verwijderen
            actie = input("\nWil je dit recept verwijderen? (ja/nee): ").strip().lower()
            if actie == "ja":
                verwijderd = recepten.pop(keuze - 1)
                print(f"Recept '{verwijderd}' verwijderd.")
        else:
            print("Recept niet gevonden.")
    except ValueError:
        print("Foutieve invoer. Probeer opnieuw.")


def voeg_recept_toe():
    print("\n--- Nieuw recept toevoegen ---")
    naam = input("Naam van het recept: ").strip()
    omschrijving = input("Omschrijving: ").strip()

    nieuw_recept = Recept(naam, omschrijving)

    # Ingrediënten toevoegen
    while True:
        ingr_naam = input("Ingrediënt naam: ").strip()
        hoeveelheid = float(input("Hoeveelheid (per persoon): "))
        eenheid = input("Eenheid (bijv. g, ml, stuks): ").strip()
        kcal = float(input("Kcal per hoeveelheid: "))

        ingr = Ingredient(ingr_naam, hoeveelheid, eenheid, kcal)

        plantaardig = input("Heeft dit ingrediënt een plantaardig alternatief? (ja/nee): ").strip().lower()
        if plantaardig == "ja":
            alt_naam = input("Alternatief ingrediënt naam: ").strip()
            alt_hoeveelheid = float(input("Hoeveelheid alternatief: "))
            alt_eenheid = input("Eenheid alternatief: ").strip()
            alt_kcal = float(input("Kcal alternatief: "))
            ingr_alt = Ingredient(alt_naam, alt_hoeveelheid, alt_eenheid, alt_kcal)
            ingr._plantaardig_alternatief = ingr_alt

        nieuw_recept.voeg_ingredient_toe(ingr)

        nog_meer = input("Nog een ingrediënt toevoegen? (ja/nee): ").strip().lower()
        if nog_meer != "ja":
            break

    # Stappen toevoegen
    while True:
        beschrijving = input("Voer een stap in: ").strip()
        stap = Stap(beschrijving)

        tip_vraag = input("Wil je een tip toevoegen aan deze stap? (ja/nee): ").strip().lower()
        if tip_vraag == "ja":
            tip = input("Voer de tip in: ").strip()
            stap.set_tip(tip)

        nieuw_recept.voeg_stap_toe(stap)

        nog_meer = input("Nog een stap toevoegen? (ja/nee): ").strip().lower()
        if nog_meer != "ja":
            break

    print(f"\nNieuw recept '{naam}' toegevoegd!")
    return nieuw_recept


def main():
    recepten = []

    while True:
        keuze = toon_menu()
        if keuze == "1":
            toon_recepten(recepten)
        elif keuze == "2":
            nieuw = voeg_recept_toe()
            recepten.append(nieuw)
        elif keuze == "3":
            print("Programma afgesloten.")
            break
        else:
            print("Foutieve invoer. Kies 1, 2 of 3.")


if __name__ == "__main__":
    main()

