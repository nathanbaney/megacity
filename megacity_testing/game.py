import libtcodpy as libtcod
import level
import entity

test = level.Level(40,40)
testEnt = entity.Entity(10,10,'#',libtcod.white)
test.addEntity(testEnt)
libtcod.console_set_custom_font("term10x16.png",libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(40,40,"Test")

while not libtcod.console_is_window_closed():
    libtcod.console_flush()
    test.draw()
