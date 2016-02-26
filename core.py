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


class BasicInfo(object):
    """Starship basic info"""

    def __init__(self, name, description, starship_type, starship_subtype, size, crew, base_speed):
        self.name = name
        self.description = description
        self.starshipType = starship_type
        self.starshipSubtype = starship_subtype
        self.size = size
        self.crew = crew
        self.baseSpeed = base_speed


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

    def __init__(self, basic_info, hull, armor, weapon, position):
        self.basicInfo = basic_info
        self.hull = hull
        self.armor = armor
        self.weapon = weapon
        self.position = position
