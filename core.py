__author__ = 'mathieu'


class Size(object):
    """defined size of object"""
    def __init__(self, name, description, fightings_square):
        self.name = name
        self.description = description
        self.fightingSquare = fightings_square


class Hull(object):
    """the hull part of a starship"""
    def __init__(self, name,description, hit_point,speedpenalty):
        self.name = name
        self.description = description
        self.hitPoint = hit_point
        self.speedPenalty = speedpenalty




class Armor(object):
    """the armor part of a starship"""
    def __init__(self,name,description, hardness, weight, speed_penality):
        self.name = name
        self.description = description
        self.hardness = hardness
        self.weight = weight
        self.speed_penality = speed_penality

class Starship(object):
    """this is a starship object"""
    def __init__(self,name, description, Size, Hull, Armor):
        self.name = name
        self.description = description
        self.size = Size
        self.hull = Hull
        self.armor = Armor


taille = Size("ultralight","a very small ship", 0.25)
ahull = Hull("vanadium hull","this is a basic hull", 50,-2)
armortst= Armor("tiberium","this tiberium armor is blabla",30,0.4,-3)
falcon = Starship("millenium","the fastest",taille,ahull,armortst)
#print(falcon.armor.name)
