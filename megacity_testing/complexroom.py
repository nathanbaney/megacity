import libtcodpy as libtcod
import wall

class ComplexRoom:
    def __init__(self, verteces, char, color):
        self.verteces = verteces
        self.char = char
        self.color = color
        self.walls = []

        self.vrt = 0
        self.interpret_vertex_array()
        
        
    def draw(self):
        for wall in self.walls:
            try:
                wall.draw()
            except:
                print "croom draw fucked up"
                

    def interpret_wall_from_verteces(self, vertex1, vertex2):
        length = 0
        dir = 5
        print vertex1
        print vertex2
        if vertex1[0] == vertex2[0]: #if on same x line
            if vertex1[1] == vertex2[1]: #if same y line
                dir = 5 #then same point, return junk
                length = 0
            elif vertex1[1] > vertex2[1]: #if v2 is up
                dir = 8 #up
                length = vertex1[1] - vertex2[1] #length is deltaY
            elif vertex1[1] < vertex2[1]: #if v2 is down
                dir = 2 #down
                length = vertex2[1] - vertex1[1] #length is deltaY
        elif vertex1[0] > vertex2[0]: #if v2 is left
            if vertex1[1] == vertex2[1]: #if same y line
                dir = 4 #left
                length = vertex1[0] - vertex2[0] #deltaX
            elif vertex1[1] > vertex2[1]: #if v2 is up
                dir = 7 #left up
                length = vertex1[1] - vertex2[1] #length is deltaY
            elif vertex1[1] < vertex2[1]: #if v2 is down
                dir = 1 #down
                length = vertex2[1] - vertex1[1] #length is deltaY
            
        elif vertex1[0] < vertex2[0]: #if v2 is right
            if vertex1[1] == vertex2[1]: #if same y line
                dir = 6 #right
                length = vertex2[0] - vertex1[0] #deltaX
            elif vertex1[1] > vertex2[1]: #if v2 is up
                dir = 9 #up right
                length = vertex1[1] - vertex2[1] #length is deltaY
            elif vertex1[1] < vertex2[1]: #if v2 is down
                dir = 3 #down right
                length = vertex2[1] - vertex1[1] #length is deltaY
        print dir
        length += 1
        return wall.Wall(vertex1[0], vertex1[1], 'R', self.color, length, dir)

    def interpret_vertex_array(self):
        ii = 0
        while ii < len(self.verteces):
            if ii == len(self.verteces)-1:
                self.walls.append(self.interpret_wall_from_verteces(self.verteces[ii],self.verteces[0]))
            else:
                self.walls.append(self.interpret_wall_from_verteces(self.verteces[ii],self.verteces[ii+1]))
            ii += 1

    def get_walls(self):
        return self.walls
            
