import libtcodpy as libtcod
import level
import entity
import room

MAIN_X = 80
MAIN_Y = 40

def read_inputs():
    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ESCAPE:
        return True
    elif key.vk == libtcod.KEY_KP1:
        test.move_entity(test_entity, 1)
    elif key.vk == libtcod.KEY_KP2:
        test.move_entity(test_entity, 2)
    elif key.vk == libtcod.KEY_KP3:
        test.move_entity(test_entity, 3)
    elif key.vk == libtcod.KEY_KP4:
        test.move_entity(test_entity, 4)
    elif key.vk == libtcod.KEY_KP5:
        test.move_entity(test_entity, 5)
    elif key.vk == libtcod.KEY_KP6:
        test.move_entity(test_entity, 6)
    elif key.vk == libtcod.KEY_KP7:
        test.move_entity(test_entity, 7)
    elif key.vk == libtcod.KEY_KP8:
        test.move_entity(test_entity, 8)
    elif key.vk == libtcod.KEY_KP9:
        test.move_entity(test_entity, 9)
       
test = level.Level(MAIN_X,MAIN_Y)
test_entity = entity.Entity(15,15,'E',libtcod.green)
test_entity2 = entity.Entity(17,15,'2',libtcod.yellow)
test_room = room.Room(3,3,7, 205, libtcod.red)
test.add_entity(test_entity)
#test.add_entity(test_entity2)
test.add_room(test_room)
libtcod.console_set_custom_font("term10x16.png",libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(MAIN_X,MAIN_Y,"Test")
libtcod.sys_set_fps(30)

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    if read_inputs():
        break
    test.draw()
    libtcod.console_flush()

