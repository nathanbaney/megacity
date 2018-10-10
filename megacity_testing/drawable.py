import libtcodpy as libtcod

class Drawable:
    def __init__(self, x, y, char, color, isSeeThru = True, isObstacle = False):
        self.x = x
        self.y = y
        self.color = color
        self.char = char
    
    def draw(self, con):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self, con):
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
        
