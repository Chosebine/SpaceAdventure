__author__ = 'mathieu'
import random

class Size(object):
    """defined size of object"""

    def __init__(self, name, size_modif, targeting_system, autopilot, length, weight):
        self.name = name
        self.sizeModif = size_modif
        self.targetingSystem = targeting_system
        self.autopilot = autopilot
        self.length = length
        self.weight = weight


class StarshipType(object):
    """defined type of starship"""

    def __init__(self,name, description, fighting_square):
        self.name = name
        self.description = description
        self.fightingSquare = fighting_square


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

    def __init__(self, name, description, StarshipType, Size, Hull, Armor, equip, posx, posy,base_speed):
        self.name = name
        self.description = description
        self.starshiptype = StarshipType
        self.size = Size
        self.hull = Hull
        self.armor = Armor
        self.equip = equip
        self.posx = posx
        self.posy = posy
        self.baseSpeed = base_speed


equipage = Crew("ace", 4, 5, 2, 4, 23)
atype= StarshipType("lightweight","un genre de petit vaisseau",1)
taille = Size("huge",-2,5,6,64,256000)
ahull = Hull("vanadium hull", "this is a basic hull", 50, )
armortst = Armor("tiberium", "this tiberium armor is blabla", 30, 0.4, -3)
falcon = Starship("millenium", "the fastest", atype,taille, ahull, armortst, equipage, 0, 0,6)
print(falcon.armor.name)
print(falcon.equip.quality,falcon.starshiptype.description)
