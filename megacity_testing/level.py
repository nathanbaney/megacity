import libtcodpy as libtcod
import tile

class Level:
    def __init__(self, h, w):
        self.w = w
        self.h = h
        global gmap.append([[tile.Tile(x,y,'X',libtcod.white) for x in range(w)]for y in range(h)])

    def draw_coord(self, x, y):
        tiletemp = gmap[x][y]
        tiletemp.draw()
        
    
