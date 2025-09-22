from typing import List
from ingredient import Ingredient
from stap import Stap

class Recept:
    """
    Recept:
    - naam, omschrijving
    - lijst van Ingredient en Stap
    - aantal_personen (default = 1)
    """

    def __init__(self, naam: str, omschrijving: str, aantal_personen: int = 1):
        self._naam = naam
        self._omschrijving = omschrijving
        self._ingredienten: List[Ingredient] = []
        self._stappen: List[Stap] = []
        self._aantal_personen = 1
        self.set_aantal_personen(aantal_personen)

    def voeg_ingredient_toe(self, ingredient: Ingredient):
        ingredient.set_hoeveelheid(self._aantal_personen)
        if ingredient.get_ingredient(True) is not ingredient:
            ingredient.get_ingredient(True).set_hoeveelheid(self._aantal_personen)
        self._ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap: Stap):
        self._stappen.append(stap)

    def set_aantal_personen(self, aantal: int):
        if aantal < 1:
            raise ValueError("aantal_personen moet >= 1 zijn")
        self._aantal_personen = aantal
        for ing in self._ingredienten:
            ing.set_hoeveelheid(aantal)
            if ing.get_ingredient(True) is not ing:
                ing.get_ingredient(True).set_hoeveelheid(aantal)

    def toon_recept(self, plantaardig: bool = False):
        print(f"\nRecept: {self._naam}")
        print(f"Omschrijving: {self._omschrijving}\n")

        print("Ingrediënten:")
        for ing in self._ingredienten:
            gebruikte = ing.get_ingredient(plantaardig)
            unit = f" {gebruikte.eenheid}" if gebruikte.eenheid else ""
            print(f" - {gebruikte.get_hoeveelheid()}{unit} {gebruikte.naam}")

        print("\nBereidingsstappen:")
        for i, stap in enumerate(self._stappen, start=1):
            print(f" {i}. {stap}")

        print(f"\nTotaal kcal: {self.totaal_kcal(plantaardig):.0f}")

    def totaal_kcal(self, plantaardig: bool = False) -> float:
        total = 0.0
        for ing in self._ingredienten:
            gebruikte = ing.get_ingredient(plantaardig)
            total += gebruikte.get_kcal()
        return total

    def __str__(self):
        return self._naam


