import libtcodpy as libtcod

class Wall:
    def __init__(self, x, y, char, color, length, dir):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.length = length
        self.dir = dir

    def draw(self):
        tempx = self.x
        tempy = self.y
        for inc in range(self.length):
            libtcod.console_set_default_foreground(0, self.color)
            libtcod.console_put_char(0, tempx, tempy, self.char, libtcod.BKGND_NONE)
            temp_pos = self.get_relative_pos(self.dir,inc)
            tempx = temp_pos[0]
            tempy = temp_pos[1]

    def get_coords(self):
        coords = []
        for inc in range(self.length):
            temp_pos = self.get_relative_pos(self.dir,inc)
            coords.append(temp_pos)
        return coords
            
    def get_relative_pos(self, dir, distance = 1):
        dx = 0
        dy = 0
        if dir == 1:#down left
            dx = -distance
            dy = distance
        elif dir == 2:#down
            dy = distance
        elif dir == 3:#down right
            dx = distance
            dy = distance
        elif dir == 4:#left
            dx = -distance
        elif dir == 5:#nada
            return
        elif dir == 6:#right 
            dx = distance
        elif dir == 7:#up left
            dx = -distance
            dy = -distance
        elif dir == 8:#up
            dy = -distance
        elif dir == 9:#up right
            dx = distance
            dy = -distance
        return (self.x + dx, self.y + dy)
