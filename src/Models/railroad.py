"""
Board railroad class implementation
@author John Rumler https://github.com/rumlerjo
"""

from Models.player import Player

class Road:
    """Railroad Class"""

    __slots__ = ["_owner", "_name", "_abbreviation", "_price"]
    
    def __init__(self, name: str, abv: str, price: int) -> None:
        self._owner: Player = None
        self._name = name
        self._abbreviation = abv
        self._price = price
        
    def __eq__(self, name: str) -> bool:
        return name.lower() == self._name.lower()

    def __str__(self) -> str:
        out = self._name + "\nPrice: " + str(self._price) + "\nOwned by: "
        if self._owner:
            out += self._owner.name + "\n"
        else:
            out += "Nobody\n"
        return out
    
    def __repr__(self) -> str:
        return str(self)

    def name(self) -> str:
        return self._name
