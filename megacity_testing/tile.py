import libtcodpy as libtcod
import drawable
import entity

class Tile(drawable.Drawable):
    
    def __init__(self, x, y, char, color, isSeeThru = True, isObstacle = False):
        self.x = x
        self.y = y
        self.color = color
        self.char = char
        self.isSeeThru = isSeeThru
        self.isObstacle = isObstacle
        self.contents = []
    def draw(self, con):
        if (len(self.contents) == 0):
            libtcod.console_set_default_foreground(con, self.color)
            libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
        else:
            self.contents[0].draw(0)
             
    def addEntity(self, entity):
        self.contents.append(entity)
