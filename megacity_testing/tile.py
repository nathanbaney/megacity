import libtcodpy as libtcod
import drawable
import entity

class Tile:
    
    def __init__(self, xin, yin, charin, colorin, isSeeThruin = True, isObstaclein = False):
        self.x = xin
        self.y = yin
        self.color = colorin
        self.char = charin
        self.isSeeThru = isSeeThruin
        self.isObstacle = isObstaclein
        
    def draw(self, con):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
    
