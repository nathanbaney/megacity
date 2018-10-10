import libtcodpy as libtcod
import drawable

class Entity(drawable.Drawable):
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def getInfo(self):
        
