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
        [[]]
    )

all_actors_list = [buttons]
blip = False
taking_inputs = True
input_string = ""
alphabet_keys = [keys.A, keys.B, keys.C, keys.D, keys.E, keys.F, keys.G, keys.H, keys.I, keys.J, keys.K, keys.L, keys.M, keys.N, keys.O, keys.P, keys.Q, keys.R, keys.S, keys.T, keys.U, keys.V, keys.W, keys.X, keys.Y, keys.Z, keys.SPACE]

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

    #Automatic draw order. Can be overridden if necessary by adding more draw statements afterward.
    for nested_list in all_actors_list:
        for actor in nested_list:
            actor.draw()
    screen.draw.text(input_string, centerx = WIDTH//2, centery = HEIGHT//2, owidth = 2)

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
    global WIDTH, HEIGHT, input_string
    if key == keys.F and not taking_inputs:  # Press 'F' to toggle fullscreen
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Fullscreen size
        update_pos(all_actors_list)
    elif key == keys.ESCAPE:  # Press 'ESC' to return to windowed mode
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        WIDTH, HEIGHT = 500, 500
        update_pos(all_actors_list)
    elif taking_inputs:
        if key == keys.BACKSPACE:
            input_string = input_string[:-1]
        elif key in alphabet_keys:
            input_string += log_input(key, ["a", "b"])

def log_input(pressed_key, refuse = []):
    """
    Returns a lowercase string of the key that is pressed. \nTo be used in on_key_down(key)
    Args:
        key (int): the key that was pressed
        refuse (list, optional): the list of characters for which to return an empty string
    """
    for index, item in enumerate(refuse):
        if not isinstance(item, str):
            raise TypeError(f"Invalid Type:\nrefuse[{index}] = {item} <-- this value should be a string.")
        if len(item) != 1:
            raise ValueError(f"String too long:\nrefuse[{index}] = {item} <-- this string should be a single character.")
        if not item.isalpha():
            raise ValueError(f"That's not a letter!\nrefuse[{index}] = {item} <-- this should be a letter of the English alphabet.")
        item = item.lower()
            
    if pressed_key == keys.A:
        if "a" not in refuse:
            return "a"
        else:
            return ""
    elif pressed_key == keys.B: 
        if "b" not in refuse:
            return "b"
        else:
            return ""
    elif pressed_key == keys.C: 
        if "c" not in refuse:
            return "c"
        else:
            return ""
    elif pressed_key == keys.D: 
        if "d" not in refuse:
            return "d"
        else:
            return ""
    elif pressed_key == keys.E: 
        if "e" not in refuse:
            return "e"
        else:
            return ""
    elif pressed_key == keys.F: 
        if "f" not in refuse:
            return "f"
        else:
            return ""
    elif pressed_key == keys.G: 
        if "g" not in refuse:
            return "g"
        else:
            return ""
    elif pressed_key == keys.H: 
        if "h" not in refuse:
            return "h"
        else:
            return ""
    elif pressed_key == keys.I: 
        if "i" not in refuse:
            return "i"
        else:
            return ""
    elif pressed_key == keys.J: 
        if "j" not in refuse:
            return "j"
        else:
            return ""
    elif pressed_key == keys.K: 
        if "k" not in refuse:
            return "k"
        else:
            return ""
    elif pressed_key == keys.L: 
        if "l" not in refuse:
            return "l"
        else:
            return ""
    elif pressed_key == keys.M: 
        if "m" not in refuse:
            return "m"
        else:
            return ""
    elif pressed_key == keys.N: 
        if "n" not in refuse:
            return "n"
        else:
            return ""
    elif pressed_key == keys.O: 
        if "o" not in refuse:
            return "o"
        else:
            return ""
    elif pressed_key == keys.P: 
        if "p" not in refuse:
            return "p"
        else:
            return ""
    elif pressed_key == keys.Q: 
        if "q" not in refuse:
            return "q"
        else:
            return ""
    elif pressed_key == keys.R: 
        if "r" not in refuse:
            return "r"
        else:
            return ""
    elif pressed_key == keys.S: 
        if "s" not in refuse:
            return "s"
        else:
            return ""
    elif pressed_key == keys.T: 
        if "t" not in refuse:
            return "t"
        else:
            return ""
    elif pressed_key == keys.U: 
        if "u" not in refuse:
            return "u"
        else:
            return ""
    elif pressed_key == keys.V: 
        if "v" not in refuse:
            return "v"
        else:
            return ""
    elif pressed_key == keys.W: 
        if "w" not in refuse:
            return "w"
        else:
            return ""
    elif pressed_key == keys.X: 
        if "x" not in refuse:
            return "x"
        else:
            return ""
    elif pressed_key == keys.Y: 
        if "y" not in refuse:
            return "y"
        else:
            return ""
    elif pressed_key == keys.Z: 
        if "z" not in refuse:
            return "z"
        else:
            return ""
    elif pressed_key == keys.SPACE:
        if " " not in refuse:
            return " "
        else:
            return ""
pgzrun.go()