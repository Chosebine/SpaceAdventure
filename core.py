__author__ = 'mathieu'


class Size(object):
    """defined size of object"""

    def __init__(self, name, size_modif, targeting_system, autopilot, length, weight):
        self.name = name
        self.sizeModif = size_modif
        self.targetingSystem = targeting_system
        self.autopilot = autopilot
        self.length = length
        self.weight = weight


class Position(object):
    """Basic 2d position in space"""

    def __init__(self, posx, posy):
        self.posX = posx
        self.posY = posy


class StarshipType(object):
    """defined type of starship"""

    def __init__(self, name, description, fighting_square):
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
        self.speedPenality = speed_penality


class Weapon(object):
    def __init__(self, name, description, damage, crit, dmg_type, wpn_range, rof, min_ship_size, price):
        self.name = name
        self.description = description
        self.damage = damage
        self.crit = crit
        self.dmgeType = dmg_type
        self.wpnRange = wpn_range
        self.rof = rof
        self.minShipSize = min_ship_size
        self.price = price


class Starship(object):
    """this is a starship object"""

    def __init__(self, name, description, starship_type,starship_subtype, size, hull, armor, weapon, crew, position, base_speed):
        self.name = name
        self.description = description
        self.starshipType = starship_type
        self.starshipSubtype = starship_subtype
        self.size = size
        self.hull = hull
        self.armor = armor
        self.weapon = weapon
        self.crew = crew
        self.position = position
        self.baseSpeed = base_speed


equipage = Crew("ace", 4, 5, 2, 4, 23)
atype = StarshipType("lightweight", "un genre de petit vaisseau", 1)
taille = Size("huge", -2, 5, 6, 64, 256000)
place = Position(0, 0)
ahull = Hull("vanadium hull", "this is a basic hull", 50, )
armortst = Armor("tiberium", "this tiberium armor is blabla", 30, 0.4, -3)
arme = Weapon("blaster", "classic starwars blaster cannon", 42, 19, "energy", 2, 1, taille, 11)
falcon = Starship("millenium", "the fastest", atype,"transport", taille, ahull, armortst, arme, equipage, place, 6)
"""print(falcon.armor.name)
print(falcon.crew.quality, falcon.starshipType.description, falcon.weapon.name)
print(falcon.baseSpeed)"""
