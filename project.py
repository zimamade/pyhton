from recept import Recept
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    # Recept 1
    pannenkoeken = Recept("Pannenkoeken", "Lekkere Hollandse pannenkoeken")
    pannenkoeken.voeg_ingredient_toe(Ingredient("Bloem", 100, "g", 364))
    pannenkoeken.voeg_ingredient_toe(Ingredient("Melk", 200, "ml", 103))
    ei = Ingredient("Ei", 1, "stuks", 78,
                    plantaardig_alternatief=Ingredient("Aquafaba", 45, "ml", 10))
    pannenkoeken.voeg_ingredient_toe(ei)
    pannenkoeken.voeg_stap_toe(Stap("Meng alle ingrediënten."))
    pannenkoeken.voeg_stap_toe(Stap("Bak de pannenkoeken in een koekenpan."))
    recepten.append(pannenkoeken)

    # Extra recepten kun je hier toevoegen

    # Overzicht tonen
    print("Beschikbare recepten:")
    for i, r in enumerate(recepten, start=1):
        print(f"{i}. {r}")

    keuze = int(input("\nKies een receptnummer: "))
    if 1 <= keuze <= len(recepten):
        aantal = int(input("Voor hoeveel personen? "))
        recepten[keuze - 1].set_aantal_personen(aantal)

        plantaardig_keuze = input("Plantaardige versie? (ja/nee): ").strip().lower() == "ja"
        recepten[keuze - 1].toon_recept(plantaardig=plantaardig_keuze)
    else:
        print("Recept niet gevonden.")

if __name__ == "__main__":
    main()
