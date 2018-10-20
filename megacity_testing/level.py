import libtcodpy as libtcod
import tile
import entity
import room
import complexroom
import wall
import roomgen

class Level:
    entities = []
    rooms = []
    crooms = []
    walls = []
        
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
            print room.x ,room.y ,room.w ,room.h
            room.draw()
        for wall in self.walls:
            wall.draw()
        for croom in self.crooms:
            croom.draw()
        for entity in self.entities:
            entity.draw()
 
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
        else:
            print "bump"
        
    def add_room(self, room):
        self.rooms.append(room)
        tempcoords = room.get_coords()
        while len(tempcoords) > 0:
            try:
                tempcoord = tempcoords.pop()
            except:
                print "pop from empty list"
            self.set_tile_to_obstacle(tempcoord[0],tempcoord[1])

    def pop_room(self):
        return self.rooms.pop()

    def add_wall(self, wall):
        self.walls.append(wall)
        tempcoords = wall.get_coords()
        while len(tempcoords) > 0:
            try:
                tempcoord = tempcoords.pop()
            except:
                print "pop from empty wall list"
            self.set_tile_to_obstacle(tempcoord[0],tempcoord[1])

    def add_croom(self, croom):
        self.crooms.append(croom)
        for wall in croom.get_walls():
            tempcoords = wall.get_coords()
            print "croom wall added"
            while len(tempcoords) > 0:
                try:
                    tempcoord = tempcoords.pop()
                except:
                    print "pop from empty croom wall list"
                self.set_tile_to_obstacle(tempcoord[0],tempcoord[1])
            
    def pop_wall(self):
        return self.walls.pop()

    def set_tile_to_obstacle(self, x, y, state = True):
        self.lvl[x][y].isObstacle = state

    def generate_rooms(self, x, y, w, h, dimension_min):
        gen = roomgen.RoomGen(x,y,w,h)
        genrooms = gen.generate(dimension_min)
        while len(genrooms) > 0:
            try:
                genroom = genrooms.pop()
            except:
                print "pop from empty genroom list"
            self.add_room(genroom)
        
        
        

        


    
        
