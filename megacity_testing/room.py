import libtcodpy as libtcod
#square room, default parent class of rooms
class Room:
    def __init__(self, x, y, size, char, color):
        self.x = x
        self.y = y
        self.size = size
        self.char = char
        self.color = color

    def draw(self):
        for tempx in range(self.x + self.size):
            for tempy in range(self.y + self.size):
                 libtcod.console_set_default_foreground(0, self.color)
                 libtcod.console_put_char(0, tempx + self.x, tempy+self.y, self.char, libtcod.BKGND_NONE)

    def get_coords(self):
        coords = []
        tempcoord = 0,0
        for tempx in range(self.size):
            if tempx == 0 or tempx == self.size:
                for tempy in range(self.size):
                    tempcoord = self.x+tempx, self.y+tempy
                    coords.append(tempcoord)
            else:
                tempcoord = tempx, self.y
                coords.append(tempcoord)
                tempcoord = tempx, self.y+self.size
                coords.append(tempcoord)

        return coords
