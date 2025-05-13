try:
    import pgzrun
    import pgzero
except ModuleNotFoundError:
    raise ModuleNotFoundError("Modules not found: \"pgzero\", \"pgzrun\"\nFix by running the following in the terminal: \x1b[38;2;0;255;255mpip install pgzero\x1b[0m")

import pgone as pgone
import save_load_manager as save_load_manager
import gui as gui
import molecular_genetics as molecular_genetics

##########################################################################################
#This section contiains variables present for testing purposes only. They will be removed.
test_dna = molecular_genetics.DNA("tagagctatcgtggcatgtagcttgtgcta", "atctcgatagcaccttacatcgaacacgat")
test_indices = test_dna.find_error_indices()
print(test_indices)
print(test_dna.main_strand)
print(test_dna.complement_strand[0:test_indices[0]] + "\x1b[38;2;255;0;0m" + test_dna.complement_strand[test_indices[0]]+"\x1b[0m"+test_dna.complement_strand[test_indices[0] + 1:])
print("Fixed version below:")
test_dna.single_nucleotide_mismatch_repair(test_indices[0])
print(test_dna.main_strand)
print(test_dna.complement_strand[0:test_indices[0]] + "\x1b[38;2;0;255;0m" + test_dna.complement_strand[test_indices[0]]+"\x1b[0m"+test_dna.complement_strand[test_indices[0] + 1:])
##########################################################################################

INIT_WIDTH = 600
INIT_HEIGHT = 500
WIDTH = INIT_WIDTH
HEIGHT = INIT_HEIGHT
TITLE = "Exploration of Genetic Repair"

#Declare initial variables; we do this before the game loop starts because we don't want to use processing power to define these each frame.
save_load = save_load_manager.save_load_system(".savedata", "savedata")
alphabet_keys = save_load.load_game_data(
        [
            "alphabet_keys.savedata"
            ],
        [
            [keys.A, keys.B, keys.C, keys.D, keys.E, keys.F, keys.G, keys.H, keys.I, keys.J, keys.K, keys.L, keys.M, keys.N, keys.O, keys.P, keys.Q, keys.R, keys.S, keys.T, keys.U, keys.V, keys.W, keys.X, keys.Y, keys.Z, keys.SPACE]
            ]
    )

#Buttons cannot be pickled.
buttons = [
    gui.button(pgone.Sprite("buttons/input_start_button.png",32,32,0,4,3),(WIDTH//2,HEIGHT//4 - 500))
    ]

save_load.save_game_data([alphabet_keys], ["alphabet_keys"])
blip = False
taking_inputs = False
input_string = ""
dna_strands = []

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

def draw():
    screen.clear()

    #Automatic draw order. Can be overridden if necessary by adding more draw statements afterward.
    if not taking_inputs:
        buttons[0].draw()
    for dna in dna_strands:
        dna.draw([10,HEIGHT//2])
    screen.draw.text(input_string, centerx = WIDTH//2, centery = HEIGHT//2, owidth = 2)

def update():
    pass

def on_mouse_down(pos):
    global taking_inputs
    for button in buttons:
        if button.mouse_collision_bool(pos):
            print(button.get_filename())
            sounds.boop.play()
            match button.get_filename():
                case "buttons/input_start_button.png":
                    taking_inputs = True

def on_mouse_move(pos):
    global blip
    for button in buttons:
        if button.mouse_collision_bool(pos):
            button.scale = 1.5
            if not blip:
                sounds.blip.play()
                blip = True
        else:
            blip = False
            button.scale = 1.0

def on_key_down(key):
    global WIDTH, HEIGHT, input_string, taking_inputs
    if taking_inputs:
        if len(input_string) <= 75:
            if key == keys.BACKSPACE:
                input_string = input_string[:-1]
            elif key in alphabet_keys:
                input_string += log_input(key, ["b", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z", " "])
        elif len(input_string) > 75:
            dna_strands.append(molecular_genetics.DNA(input_string))
            input_string = ""
            taking_inputs = False

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
        if not item.isalpha() and item != " ":
            raise ValueError(f"That's not a letter!\nrefuse[{index}] = {item} <-- this should be a letter of the English alphabet.")
        item = item.lower()
    
    match pressed_key:
        case keys.A:
            if "a" not in refuse:
                return "a"
            else:
                return ""
        case keys.B: 
            if "b" not in refuse:
                return "b"
            else:
                return ""
        case keys.C: 
            if "c" not in refuse:
                return "c"
            else:
                return ""
        case keys.D: 
            if "d" not in refuse:
                return "d"
            else:
                return ""
        case keys.E: 
            if "e" not in refuse:
                return "e"
            else:
                return ""
        case keys.F: 
            if "f" not in refuse:
                return "f"
            else:
                return ""
        case keys.G: 
            if "g" not in refuse:
                return "g"
            else:
                return ""
        case keys.H: 
            if "h" not in refuse:
                return "h"
            else:
                return ""
        case keys.I: 
            if "i" not in refuse:
                return "i"
            else:
                return ""
        case keys.J: 
            if "j" not in refuse:
                return "j"
            else:
                return ""
        case keys.K: 
            if "k" not in refuse:
                return "k"
            else:
                return ""
        case keys.L: 
            if "l" not in refuse:
                return "l"
            else:
                return ""
        case keys.M: 
            if "m" not in refuse:
                return "m"
            else:
                return ""
        case keys.N: 
            if "n" not in refuse:
                return "n"
            else:
                return ""
        case keys.O: 
            if "o" not in refuse:
                return "o"
            else:
                return ""
        case keys.P: 
            if "p" not in refuse:
                return "p"
            else:
                return ""
        case keys.Q: 
            if "q" not in refuse:
                return "q"
            else:
                return ""
        case keys.R: 
            if "r" not in refuse:
                return "r"
            else:
                return ""
        case keys.S: 
            if "s" not in refuse:
                return "s"
            else:
                return ""
        case keys.T: 
            if "t" not in refuse:
                return "t"
            else:
                return ""
        case keys.U: 
            if "u" not in refuse:
                return "u"
            else:
                return ""
        case keys.V: 
            if "v" not in refuse:
                return "v"
            else:
                return ""
        case keys.W: 
            if "w" not in refuse:
                return "w"
            else:
                return ""
        case keys.X: 
            if "x" not in refuse:
                return "x"
            else:
                return ""
        case keys.Y: 
            if "y" not in refuse:
                return "y"
            else:
                return ""
        case keys.Z: 
            if "z" not in refuse:
                return "z"
            else:
                return ""
        case keys.SPACE:
            if " " not in refuse:
                return " "
            else:
                return ""
pgzrun.go()