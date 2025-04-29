import pgone
import pgzrun
import save_load_manager
import gui
import pygame
import molecular_genetics

INIT_WIDTH = 600
INIT_HEIGHT = 500
WIDTH = INIT_WIDTH
HEIGHT = INIT_HEIGHT
TITLE = "Exploration of Genetic Repair"

#Declare initial variables; we do this before the game loop starts because we don't want to use processing power to define these each frame.
save_load = save_load_manager.save_load_system("savedata","savedata")
buttons = save_load.load_game_data(
        ["buttons.savedata"],
        [[gui.button(pgone.Sprite("buttons/play_button.png", 32, 32, 0, 4, 5), (WIDTH//2, HEIGHT//2))]]
    )

all_actors_list = [buttons]
blip = False

#Prune all unwanted types from the list. Typed arrays are better sometimes.
to_remove = []
for button in buttons:
    if not isinstance(button, gui.button):
        to_remove.append(button)
for item in to_remove:
    buttons.remove(item)
    print(f"{item} ({type(item)}) removed from buttons: not a gui.button")
#Remove the to_remove list because it is no longer used after this
del(to_remove)

#Dynamically change the positions of all actors upon the change of screen size
def update_pos(list):
    """
    Updates the position of items in [list], used when fullscreen
    Args:
        list (list): list of SpriteActors/Actors or their children classes
    """
    for nested_list in list:
        for actor in nested_list:
            actor.x_ratio = actor.x // INIT_WIDTH
            actor.y_ratio = actor.y // INIT_HEIGHT
            actor.x = actor.x_ratio * WIDTH
            actor.y = actor.y_ratio * HEIGHT

def draw():
    screen.clear()
    screen.fill("yellow")

    #Automatic draw order. Can be overridden if necessary by adding more draw statements afterward..
    for nested_list in all_actors_list:
        for actor in nested_list:
            actor.draw()

    dna = molecular_genetics.DNA("actggttatgtgatgtgctagtgggctat")
    dna.draw([0, 0])

def update():
    pass

def on_mouse_down(pos):
    for button in buttons:
        if button.mouse_collision_bool(pos):
            match button.get_filename():
                case "play_button_hover.png":
                    print("Clicking play_button_hover")

def on_mouse_move(pos):
    global blip
    for button in buttons:
        if button.mouse_collision_bool(pos):
            button.scale = 1.5
            if button.image[-10:] != "_hover.png":
                button.image = f"{button.image}"[0:-4]+"_hover.png"
            if not blip:
                sounds.blip.play()
                blip = True
        else:
            blip = False
            button.scale = 1.0
            if button.image[-10:] == "_hover.png":
                button.image = button.image[:-10]+ ".png"

def on_key_down(key):
    global WIDTH, HEIGHT
    if key == keys.F:  # Press 'F' to toggle fullscreen
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Fullscreen size
        update_pos(all_actors_list)

    elif key == keys.ESCAPE:  # Press 'ESC' to return to windowed mode
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        WIDTH, HEIGHT = 500, 500
        update_pos(all_actors_list)
pgzrun.go()