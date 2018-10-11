import libtcodpy as libtcod

class Entity:
    
    def __init__(self, xin, yin, charin, colorin):
        self.x = xin
        self.y = yin
        self.char = charin
        self.color = colorin

    def draw(self, con):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def getInfo(self):
        return

    def move(self, dir):#directions: 0,1,2,3 -> d,w,a,s
        if dir == 1:#down left
            self.x = (self.x) - 1
            self.y = (self.y) + 1
        elif dir == 2:#down
            self.y = (self.y) + 1
        elif dir == 3:#down right
            self.x = (self.x) + 1
            self.y = (self.y) + 1
        elif dir == 4:#left
            self.x = (self.x) - 1
        elif dir == 5:#nada
            return
        elif dir == 6:#right 
            self.x = (self.x) + 1
        elif dir == 7:#up left
            self.x = (self.x) - 1
            self.y = (self.y) - 1
        elif dir == 8:#up
            self.y = (self.y) - 1
        elif dir == 9:#up right
            self.x = (self.x) + 1
            self.y = (self.y) - 1
            
        
