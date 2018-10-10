import libtcodpy as libtcod
import tile
import entity

class Level:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.lvl = [[(tile.Tile(x,y,'x',libtcod.red)) for x in range(w)]
                    for y in range(h)]

    def draw(self):
        for x in range(self.w):
            for y in range(self.h):
                self.lvl[x][y].draw(0)
                
    def addEntity(self, entity):
        self.lvl[entity.x][entity.y].addEntity(entity)
        
