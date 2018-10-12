import libtcodpy as libtcod

class Window:
    def __init__(self, x, y):
        self.con = libtcod.console_new(x,y)

    def draw(self):
        libtcod.console_set_background_color(self.con,libtcod.red)
        libtcod.console_clear(self.con)
        libtcod.console_blit(self.con,0,0,40,20,0,5,5,255)
