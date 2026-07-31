import pygame
import input
from player import Player
from sprites import sprites

pygame.init()

#Setup code
pygame.display.set_caption("Spirit Bond")
screen = pygame.display.set_mode((800,600))
clear_colour = (30,150,50)
running = True
Player = Player("images/Caltheros_Right.png", 0, 0)


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
    Player.update()

    #Draw/display code
    screen.fill(clear_colour)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()