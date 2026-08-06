import pygame
import core.input as input
from components.player import Player
from components.sprite import sprites, Sprite
from core.map1 import Tilekind, Map
from core.camera import create_screen
from components.enemy import Enemy, active_objects
from components.physics import Body

pygame.init()
screen = create_screen(800, 600, "Spirit Bond")

#Setup code
pygame.display.set_caption("Spirit Bond")
screen = pygame.display.set_mode((800,600))
clear_colour = (0,0,0)
running = True
player = Enemy(Player(), Body(1, 23, 38, 20), Sprite("Caltheros_right.png"), x=32*11, y=32*7)
Tile_kinds = [
    Tilekind("grass", "Grass..jpeg", False), #0
    Tilekind("floor", "Floor..jpeg", False), #1
    Tilekind("carpet", "Carpet..jpeg", False), #2
    Tilekind("path", "Path..jpeg", False),#3
    Tilekind("water","Water..jpeg", True),#4
    Tilekind("bridge", "Wood..jpeg", False),#5
    Tilekind("rightwall", "Wall_right..jpeg", True), #6
    Tilekind("leftwall", "Wall_left.jpeg", True),#7
    Tilekind("topwall", "Wall_up.jpeg", True),#8
    Tilekind("bottomwall", "Wall_down..jpeg", True),#9
    Tilekind("wall", "Black_Wall.png", True),#10
    Tilekind("transparent", "Colisions.png", False),#11
    ]
map = Map("start.map", Tile_kinds, 32)


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