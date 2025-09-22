from typing import Optional

class Stap:
    """
    Bereidingsstap. Kan optioneel een tip bevatten.
    """

    def __init__(self, beschrijving: str, tip: Optional[str] = None):
        self._beschrijving = beschrijving
        self._tip = tip

    def set_tip(self, tip: str):
        self._tip = tip

    def __str__(self):
        if self._tip:
            return f"{self._beschrijving} (Tip: {self._tip})"
        return self._beschrijving

