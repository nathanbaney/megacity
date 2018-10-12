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
        for tempx in range(self.size):
            for tempy in range(self.size):
                 libtcod.console_set_default_foreground(0, self.color)
                 libtcod.console_put_char(0, tempx + self.x, tempy+self.y, self.char, libtcod.BKGND_NONE)

    def get_coords(self):
        coords = []
        for tempx in range(self.size):
            for tempy in range(self.size):
                    tempcoord = tempx+self.x, tempy+self.y
                    coords.append(tempcoord)
        return coords
