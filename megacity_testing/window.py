import libtcodpy as libtcod

class Window:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.con = libtcod.console_new(self.x,self.y)

    def draw(self, x, y):
        libtcod.console_blit(self.con,0,0,0,0,0,x,y,255)
        libtcod.console_flush() #important, prevents flicker
