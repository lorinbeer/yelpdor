from lib import libtcodpy as libtcod

from yelpdor.amulet import Amulet
from yelpdor.camera import Camera
from yelpdor.city_map_generator import generate_city_map
from yelpdor.player import Player
from yelpdor.renderer import Renderer
from yelpdor.renderer import Screen 
<<<<<<< ebc41918eb8064076be5fdd1883036188c58284e
=======
from yelpdor.gui.messenger import Messenger
from yelpdor.simple_dungeon import make_map
>>>>>>> messenger gui bar


MAP_WIDTH = 256 
MAP_HEIGHT = 256
 
SCREEN_HEIGHT = 64 
SCREEN_WIDTH = 80

CAMERA_HEIGHT = 60 
CAMERA_WIDTH = 48

MESSENGER_WIDTH = SCREEN_WIDTH
MESSENGER_HEIGHT = 16

 
LIMIT_FPS = 20  #20 frames-per-second maximum
 
def handle_keys():
    #key = libtcod.console_check_for_keypress()  #real-time
    key = libtcod.console_wait_for_keypress(True)  #turn-based
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    elif key.c == ord('y') or key.c == ord('Y'):
        amulet.toggle_mode()
 
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(dungeon_map, 0, -1)
        messenger.message("you moved UP")
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(dungeon_map, 0, 1)
        messenger.message("you moved SOUTH")
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(dungeon_map, -1, 0)
        messenger.message("you moved WEST")
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(dungeon_map, 1, 0)
        messenger.message("you moved WEST. Confused? Me too! We should get together and talk about it, maybe over beers! The problem is, with our sense of direction, we'd never find each other.")
 
 
#############################################
# Initialization & Main Loop
#############################################
 
libtcod.console_set_custom_font('res/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Amulet of Yelpdor', False)
libtcod.sys_set_fps(LIMIT_FPS)
console = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
 
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)
dungeon_objects = [player]

dungeon_map = generate_city_map(MAP_WIDTH, MAP_HEIGHT)
player.x, player.y = dungeon_map.spawn
dungeon_map.init_fov_map()
screen = Screen(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
camera = Camera(CAMERA_WIDTH, CAMERA_HEIGHT, dungeon_map) 
renderer = Renderer(console, screen, camera)
amulet = Amulet(player, 3, 3)
messenger = Messenger(
    width=MESSENGER_WIDTH,
    height=MESSENGER_HEIGHT,
    screen=screen)


while not libtcod.console_is_window_closed():
    renderer.render(player, dungeon_objects, dungeon_map, amulet)
