__author__ = 'mathieu'


class Size(object):
    """defined size of object"""
    def __init__(self, name, fightings_square):
        self.name = name
        self.fightingSquare = fightings_square


class Hull(object):
    """the hull part of a starship"""
    def __init__(self, name, hit_point):
        self.name = name
        self.hitPoint = hit_point


taille = Size("ultralight", 0.25)
ahull = Hull("vanadium hull", 50)
print(taille.fightingSquare)