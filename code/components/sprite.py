import pygame
from core.camera import camera

sprites = []
loaded = {}
image_location = "contents/images.keep"

class Sprite:
    def __init__(self, image):
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image_location + "/" + image)
            loaded[image] = self.image
        sprites.append(self)

    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.enemy.x - camera.x, self.enemy.y - camera.y))