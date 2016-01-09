__author__ = 'mathieu'

class Size(object):
    """defined size of object"""
    def __init__(self, name, fightingSquare):
        self.name = name
        self.fightingSquare = fightingSquare

class Hull(object):
    """the hull part of a starship"""
    def __init__(self, size, name, hitPoint):
        self.size = size
        self.name = name
        self.hitPoint = hitPoint


taille = Size("ultralight",0.25)
ahull= Hull(taille,"vanadium hull",50)

