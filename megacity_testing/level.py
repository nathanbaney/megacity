import libtcodpy as libtcod
import tile
import entity
import room

class Level:
    entities = []
    rooms = []
        
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.lvl = [[(tile.Tile(x,y,'.',libtcod.grey)) for y in range(h)]
                    for x in range(w)]
        
    def draw(self):
        for x in range(self.w):
            for y in range(self.h):
                self.lvl[x][y].draw(0)
        for room in self.rooms:
            room.draw()
        for entity in self.entities:
            entity.draw(0)
 
    def add_entity(self, entity):
        self.entities.append(entity)
           
    def pop_entity(self):
        return self.entities.pop()

    def check_entity_collision(self, entity, dir):
        if self.entities.count(entity) != 0:
            temp_entity = self.entities.pop()
            temp_coords = temp_entity.get_relative_pos(dir)
            self.entities.append(temp_entity)
            if self.lvl[temp_coords[0]][temp_coords[1]].isObstacle == True:
                return True
            return False
    
    def move_entity(self, entity, dir):
        if self.check_entity_collision(entity, dir) == False:
            entity.move(dir)
        
    def add_room(self, room):
        self.rooms.append(room)
        tempcoords = room.get_coords()
        try:
            tempcoord = tempcoords.pop()
        except:
            print "pop from empty list"
        self.lvl[tempcoord[0]][tempcoord[1]].isObstacle = True

    def pop_room(self):
        return self.rooms.pop()


    
        
