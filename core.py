__author__ = 'mathieu'


class Size(object):
    """defined size of object"""

    def __init__(self, name, description, fightings_square):
        self.name = name
        self.description = description
        self.fightingSquare = fightings_square


class Crew(object):
    """The crew of a starship"""

    def __init__(self, quality, skill, defense, dexterity, attack, price):
        self.quality = quality
        self.skill = skill
        self.defense = defense
        self.dexterity = dexterity
        self.attack = attack
        self.price = price


class Hull(object):
    """the hull part of a starship"""

    def __init__(self, name, description, hit_point):
        self.name = name
        self.description = description
        self.hitPoint = hit_point


class Armor(object):
    """the armor part of a starship"""

    def __init__(self, name, description, hardness, weight, speed_penality):
        self.name = name
        self.description = description
        self.hardness = hardness
        self.weight = weight
        self.speed_penality = speed_penality


class Starship(object):
    """this is a starship object"""

    def __init__(self, name, description, Size, Hull, Armor, equip, posx, posy):
        self.name = name
        self.description = description
        self.size = Size
        self.hull = Hull
        self.armor = Armor
        self.equip = equip
        self.posx = posx
        self.posy = posy


equipage = Crew("ace", 4, 5, 2, 4, 23)

taille = Size("ultralight", "a very small ship", 0.25)
ahull = Hull("vanadium hull", "this is a basic hull", 50, )
armortst = Armor("tiberium", "this tiberium armor is blabla", 30, 0.4, -3)
falcon = Starship("millenium", "the fastest", taille, ahull, armortst, equipage, 4, 5)
print(falcon.armor.name)
print(falcon.equip.quality)
