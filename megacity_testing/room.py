import libtcodpy as libtcod
#square room, default parent class of rooms
class Room:
    def __init__(self, x, y, w, h, char, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.char = char
        self.color = color

    def draw(self):
        for x in range(self.w):
            for y in range(self.h):
                if x == 0 or x == self.w-1: #if you're getting the tops or bottoms of the part...
                    libtcod.console_set_default_foreground(0, self.color)
                    libtcod.console_put_char(0, x+self.x, y+self.y, self.char, libtcod.BKGND_NONE)
                elif y == 0 or y == self.h-1: #if you're getting the sides...
                    libtcod.console_set_default_foreground(0, self.color)
                    libtcod.console_put_char(0, x+self.x, y+self.y, self.char, libtcod.BKGND_NONE)

    def get_coords(self):
        coords = []
        for x in range(self.w):
            for y in range(self.h):
                if x == 0 or x == self.w-1: #if you're getting the tops or bottoms of the part...
                    coords.append((x+self.x,y+self.y))
                elif y == 0 or y == self.h-1: #if you're getting the sides...
                    coords.append((x+self.x,y+self.y))
        return coords
