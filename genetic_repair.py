import pgone
import pgzrun
import save_load_manager
import gui
import pygame

INIT_WIDTH = 600
INIT_HEIGHT = 500
WIDTH = INIT_WIDTH
HEIGHT = INIT_HEIGHT
TITLE = "Exploration of Genetic Repair"

save_load = save_load_manager.save_load_system("savedata","savedata")
gui.button()
buttons = save_load.load_game_data(
        ["buttons.savedata"],
        [[]]
    )

all_actors_list = [buttons]

#Prune all unwanted types from the list. Typed arrays are better sometimes.
to_remove = []
for button in buttons:
    if not isinstance(button, gui.button):
        to_remove.append(button)
for item in to_remove:
    buttons.remove(item)
    print(f"{item} ({type(item)}) removed from buttons: not a gui.button")

def update_pos(list):
    """
    Updates the position of items in [list]
    Args:
        list (list): list of SpriteActors/Actors or their children classes
    """
    for actor in list:
        actor.x_ratio = actor.x // INIT_WIDTH
        actor.y_ratio = actor.y // INIT_HEIGHT
        actor.x = actor.x_ratio * WIDTH
        actor.y = actor.y_ratio * HEIGHT

def draw():
    screen.clear()
    screen.fill("white")

def update():
    pass

def on_mouse_down(pos):
    for button in buttons:
        if button.mouse_collision_bool(pos):
            pass

blip = False
def on_mouse_move(pos):
    global blip
    for button in buttons:
        if button.mouse_collision_bool(pos):
            button.angle = 10
            button.image = f"{button.image}_hover"
            if not blip:
                sounds.blip.play()
        else:
            blip = True
            button.angle = 0

def on_key_down(key):
    if key == keys.F:  # Press 'F' to toggle fullscreen
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Fullscreen size

    elif key == keys.ESCAPE:  # Press 'ESC' to return to windowed mode
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        WIDTH, HEIGHT = 500, 500
    
    for actor in all_actors_list:
        update_pos(all_actors_list)
pgzrun.go()