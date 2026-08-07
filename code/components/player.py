import pygame
from components.sprite import Sprite
from core.input import is_key_pressed
from core.camera import camera
from components.entity import active_objects
from components.physics import Body

class Player:
    movement_speed = 3
    def __init__(self):
        active_objects.append(self)

    def update(self):
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)
    
        sprite = self.entity.get(Sprite)
        if is_key_pressed(pygame.K_w):
            self.entity.y -= self.movement_speed
        if is_key_pressed(pygame.K_a):
            self.entity.x -= self.movement_speed
        if is_key_pressed(pygame.K_s):
            self.entity.y += self.movement_speed
        if is_key_pressed(pygame.K_d):
            self.entity.x += self.movement_speed
        if not body.posision():
            self.entity.y = previous_y
        if not body.posision():
            self.entity.x = previous_x
        camera.x = self.entity.x - camera.width/2
        camera.y = self.entity.y - camera.height/2