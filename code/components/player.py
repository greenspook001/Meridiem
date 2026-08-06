import pygame
from components.sprite import Sprite
from core.input import is_key_pressed
from core.camera import camera
from components.enemy import active_objects
from components.physics import Body

class Player:
    movement_speed = 3
    def __init__(self):
        active_objects.append(self)

    def update(self):
        previous_x = self.enemy.x
        previous_y = self.enemy.y
        sprite = self.enemy.get(Sprite)
        body = self.enemy.get(Body)
    
        sprite = self.enemy.get(Sprite)
        if is_key_pressed(pygame.K_w):
            self.enemy.y -= self.movement_speed
        if is_key_pressed(pygame.K_a):
            self.enemy.x -= self.movement_speed
        if is_key_pressed(pygame.K_s):
            self.enemy.y += self.movement_speed
        if is_key_pressed(pygame.K_d):
            self.enemy.x += self.movement_speed
        if not body.posision():
            self.enemy.y = previous_y
        if not body.posision():
            self.enemy.x = previous_x
        camera.x = self.enemy.x - camera.width/2
        camera.y = self.enemy.y - camera.height/2