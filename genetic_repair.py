import pgone
import pgzrun
import save_load_manager
import gui
from pgzero import screen
import pygame


WIDTH = 600
HEIGHT = 500
TITLE = "Exploration of Genetic Repair"

save_load = save_load_manager.save_load_system("savedata","savedata")

buttons = save_load.load_game_data(["buttons.savedata"],[[]])

to_remove = []
for button in buttons:
    if not isinstance(button, gui.button):
        to_remove.append(button)

for item in to_remove:
    buttons.remove(item)
    print(f"{item} ({type(item)}) removed from buttons: not a gui.button")

def draw():
    screen.clear()
    screen.fill("white")
    pgone.SpriteActor(pgone.Sprite("bases.png",7,13,0,4,1),(WIDTH//2,HEIGHT//2)).draw()

def update():
    pass

def on_mouse_down(pos):
    for button in buttons:
        if button.mouse_collision_bool(pos):
            pass

def on_mouse_move(pos):
    for button in buttons:
        if button.mouse_collision_bool(pos):
            pass

def on_key_down(key):
    if key == keys.F:  # Press 'F' to toggle fullscreen
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Fullscreen size

    elif key == keys.ESCAPE:  # Press 'ESC' to return to windowed mode
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        WIDTH, HEIGHT = 500, 500

pgzrun.go()