import libtcodpy as libtcod
import room
import wall

class RoomGen: 
    def __init__(self,x,y,w,h):
        self.mainnode = Partition(x,y,w,h)

    def generate(self,dimension_min):
        self.rooms = []
        self.mainnode.recursive_cut_helper(dimension_min,self.rooms)
        return self.rooms

class Partition:
    room = None
    node1 = None
    node2 = None
    def __init__(self,x,y,w,h,cutdist=16,orientation = 1):
        self.x = x #x and y are top left point of partition
        self.y = y
        self.w = w
        self.h = h
        self.cutdist = cutdist #how far down the particular part is cut
        self.orientation = orientation#orientation is cut vert(1) or horiz(0)

    def cut(self):
        if self.orientation == 0: #horizontal cut
            self.node1 = Partition(self.x,self.y,self.w,self.h-self.cutdist,self.cutdist/2,self.orientation)
            self.node2 = Partition(self.x,self.y+self.cutdist,self.w,self.h-self.cutdist,self.cutdist/2,self.orientation)
        elif self.orientation == 1: #vertical cut
            self.node1 = Partition(self.x,self.y,self.w-self.cutdist,self.h,self.cutdist/2)
            self.node2 = Partition(self.x+self.cutdist,self.y-self.cutdist,self.w-self.cutdist,self.h,self.cutdist/2)

        self.node1.set_cutdist(self.cutdist / 2)
        self.node2.set_cutdist(self.cutdist / 2)
        self.node1.set_orientation((self.orientation + 1)%2)
        self.node2.set_orientation((self.orientation + 1)%2)
            
    def recursive_cut_helper(self,dimension_min,room_container):
        if self.w <= dimension_min or self.h <= dimension_min or self.cutdist <= 4:
            temproom = room.Room(self.x,self.y,self.w,self.h,'P',libtcod.purple)
            print self.orientation
            room_container.append(temproom)
        else:
            self.cut()
            self.node1.recursive_cut_helper(dimension_min,room_container)
            self.node2.recursive_cut_helper(dimension_min,room_container)
            
    def set_cutdist(self,cutdist):
        self.cutdist = cutdist

    def set_orientation(self, orientation):
        self.orientation = orientation

    def get_coords(self):
        coords = []
        for x in range(self.w):
            for y in range(self.h):
                if x == 0 or x == self.w-1: #if you're getting the tops or bottoms of the part...
                    coords.append((x,y))
                elif y == 0 or y == self.h-1: #if you're getting the sides...
                    coords.append((x,y))
        return coords
                
        

    
