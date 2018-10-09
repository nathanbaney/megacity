import libtcodpy as libtcod
import level

testlevel = level.Level(10,10)

def drawScreen(h, w):
    for y in range(h):
        for x in range(w):
            testlevel.draw_coord(y, x)
            

# inits

testlevel = level.Level(10,10)
drawScreen(10, 10)
