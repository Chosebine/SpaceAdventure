__author__ = 'mathieu'


class Starship(object):
    """basic starship class"""
    def __init__(self, starshipsubtype="fighter"):
        self.StarshipSubtype = starshipsubtype
        self.starship = [["Mediumweight", "Cruiser", 7, 5, 5, 30, 200, 6, 3, 2, 2, -8, 6, 720, 28800, 3, 120, 80, 7200, 16, 64, 3],
                        ["Ultralight", "Fighter", 19, 13, 6, 20, 8, 8, 7, 6, 8, -4, 6, 36, 39, 2, 1, 1, 1700, 8, 48, 3]]


unvaisseau = Starship("Cruiser")
print(unvaisseau.starship[1])
