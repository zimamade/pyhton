from typing import Optional

class Ingredient:
    """
    Ingredient:
    - Hoeveelheid wordt opgeslagen per 1 persoon als _base_hoeveelheid.
    - kcal is de energie voor de base_hoeveelheid (dus per 1 persoon).
    - plantaardig_alternatief is optioneel een ander Ingredient object.
    """

    def __init__(self, naam: str, hoeveelheid: float, eenheid: str = "",
                 kcal: float = 0.0, plantaardig_alternatief: Optional['Ingredient'] = None):
        self._naam = naam
        self._base_hoeveelheid = float(hoeveelheid)   # hoeveelheid per 1 persoon
        self._hoeveelheid = float(hoeveelheid)        # huidige totale hoeveelheid
        self._eenheid = eenheid
        self._kcal = float(kcal)
        self._plantaardig_alternatief = plantaardig_alternatief

    def set_hoeveelheid(self, aantal_personen: int):
        if aantal_personen < 1:
            raise ValueError("aantal_personen moet >= 1 zijn")
        self._hoeveelheid = self._base_hoeveelheid * aantal_personen

    def get_hoeveelheid(self) -> float:
        return self._hoeveelheid

    def get_kcal(self) -> float:
        if self._base_hoeveelheid == 0:
            return 0.0
        factor = self._hoeveelheid / self._base_hoeveelheid
        return self._kcal * factor

    def get_ingredient(self, plantaardig: bool = False) -> 'Ingredient':
        if plantaardig and self._plantaardig_alternatief:
            return self._plantaardig_alternatief
        return self

    
    def naam(self):
        return self._naam

    
    def eenheid(self):
        return self._eenheid

    def __str__(self):
        unit = f" {self._eenheid}" if self._eenheid else ""
        return f"{self._hoeveelheid}{unit} {self._naam} ({self.get_kcal():.0f} kcal)"
