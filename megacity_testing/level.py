import libtcodpy as libtcod
import tile
import entity

class Level:
    entities = []
        
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.lvl = [[(tile.Tile(x,y,'.',libtcod.grey)) for x in range(w)]
                    for y in range(h)]
        
    def add_entity(self, entity):
        self.entities.append(entity)
        
    def draw(self):
        for x in range(self.w):
            for y in range(self.h):
                self.lvl[y][x].draw(0)
        for entity in self.entities:
            entity.draw(0)

    def pop_entity(self):
        return self.entities.pop()


    
        
