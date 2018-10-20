import libtcodpy as libtcod
import level
import entity
import room
import complexroom
import wall
import window

#eventually prompt for x y size lol
MAIN_X = 130
MAIN_Y = 50

#boolean of whether the game's on or not
game_state = True

def read_inputs():
    global game_state
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ESCAPE:
        game_state = False
    elif key.vk == libtcod.KEY_KP1:
        test.move_entity(test_entity, 1)
    elif key.vk == libtcod.KEY_KP2 or key.vk == libtcod.KEY_DOWN:
        test.move_entity(test_entity, 2)
    elif key.vk == libtcod.KEY_KP3:
        test.move_entity(test_entity, 3)
    elif key.vk == libtcod.KEY_KP4 or key.vk == libtcod.KEY_LEFT:
        test.move_entity(test_entity, 4)
    elif key.vk == libtcod.KEY_KP5:
        test.move_entity(test_entity, 5)
    elif key.vk == libtcod.KEY_KP6 or key.vk == libtcod.KEY_RIGHT:
        test.move_entity(test_entity, 6)
    elif key.vk == libtcod.KEY_KP7:
        test.move_entity(test_entity, 7)
    elif key.vk == libtcod.KEY_KP8 or key.vk == libtcod.KEY_UP:
        test.move_entity(test_entity, 8)
    elif key.vk == libtcod.KEY_KP9:
        test.move_entity(test_entity, 9)

#inv = libtcod.console_new(30,30)
#libtcod.console_set_default_background(inv,libtcod.red)

#wdw = window.Window(20,40)

test = level.Level(MAIN_X,MAIN_Y)
test.generate_rooms(10,10,32,32,4)
test_entity = entity.Entity(15,15,'E',libtcod.green)
test_entity2 = entity.Entity(17,15,'2',libtcod.yellow)
test_room = room.Room(3,3,7,20, 205, libtcod.red)
test_wall = wall.Wall(20,20,'W',libtcod.blue,20,3)
verteces = ((20,20),(20,30),(40,30),(40,20))
test_croom = complexroom.ComplexRoom(verteces, 'C', libtcod.orange)
test.add_entity(test_entity)
test.add_wall(test_wall)
test.add_room(test_room)
test.add_croom(test_croom)
libtcod.console_set_custom_font("term10x16.png",libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(MAIN_X,MAIN_Y,"Test")
libtcod.sys_set_fps(60)

while not libtcod.console_is_window_closed():
    read_inputs()
    if game_state == False:
        break
    libtcod.console_set_default_foreground(0, libtcod.white) 
    test.draw()
    #wdw.draw(100,5)
    
    #libtcod.console_blit(inv,0,0,0,0,0,100,5,255)
    
    libtcod.console_flush()

