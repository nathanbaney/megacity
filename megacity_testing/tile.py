import libtcodpy as libtcod
import drawable

class Tile(drawable.Drawable):
    def __init__(self, x, y, char, color, isSeeThru = True, isObstacle = False):
        self.x = x
        self.y = y
        self.color = color
        self.char = char
        self.isSeeThru = isSeeThru
        self.isObstacle = isObstacle
        
