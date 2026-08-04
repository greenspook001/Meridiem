import pygame
import input
from player import Player
from sprite import sprites, Sprite
from map1 import Tilekind, Map
from camera import create_screen
from enemy import Enemy, active_objects
from physics import Body

pygame.init()
screen = create_screen(800, 600, "Spirit Bond")

#Setup code
pygame.display.set_caption("Spirit Bond")
screen = pygame.display.set_mode((800,600))
clear_colour = (0,0,0)
running = True
player = Enemy(Player(), Body(3, 32, 16, 16), Sprite("images.keep/Caltheros_Right.png"), x=32*11, y=32*7)
Tile_kinds = [
    Tilekind("grass", "images.keep/Grass..jpeg", False), #0
    Tilekind("floor", "images.keep/Floor..jpeg", False), #1
    Tilekind("carpet", "images.keep/Carpet..jpeg", False), #2
    Tilekind("path", "images.keep/Path..jpeg", False),#3
    Tilekind("water","images.keep/Water..jpeg", True),#4
    Tilekind("bridge", "images.keep/Wood..jpeg", False),#5
    Tilekind("rightwall", "images.keep/Wall_right..jpeg", True), #6
    Tilekind("leftwall", "images.keep/Wall_left.jpeg", True),#7
    Tilekind("topwall", "images.keep/Wall_up.jpeg", True),#8
    Tilekind("bottomwall", "images.keep/Wall_down..jpeg", True),#9
    Tilekind("wall", "images.keep/Black_Wall.jpg", True),#10
    Tilekind("transparent", "images.keep/Colisions.png", False),#11
    ]
map = Map("maps/start.map", Tile_kinds, 32)


#Game Admin
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

    #Updating Code
    for a in active_objects:
        a.update()

    #Draw/display code
    screen.fill(clear_colour)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()