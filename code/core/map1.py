import pygame
from core.camera import camera

map = None
map_location = "contents/maps"
image_location = "contents/images.keep"

class Tilekind:
    def __init__(self, name, image, is_solid):
        self.name = name
        self.image = pygame.image.load(image_location + "/" + image)
        self.is_solid = is_solid

class Map:
    def __init__(self, map_file, tile_kinds, tile_size):
        global map
        self.tile_kinds = tile_kinds

        map = self

        #loading the start.map file
        file = open(map_location + "/" + map_file, "r")
        data = file.read()
        file.close()

        #Setting up the tiles form the loaded data
        self.tiles = []
        for line in data.split("\n"):
            row = []
            for tile_number in line.split():
                row.append(int(tile_number))
            self.tiles.append(row)

        self.tile_size = tile_size

    def solid_point(self, x, y):
        x_tile = int(x /self.tile_size)
        y_tile = int(y /self.tile_size)
        if x_tile < 0 or y_tile < 0 or y_tile >= len(self.tiles) or \
        x_tile >= len(self.tiles[y_tile]):
            return False
        tile = self.tiles[y_tile][x_tile]
        return self.tile_kinds[tile].is_solid

    def solid_rectangle(self, x, y, width, height):
        for point_x, point_y in [
            (x, y),
            (x + width, y),
            (x, y + height),
            (x + width, y + height)
        ]:
            if self.solid_point(point_x, point_y):
                return True

        return False

    # Setting up the tile size
    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size - camera.x, 
                            y * self.tile_size - camera.y)
                image = self.tile_kinds[tile].image
                screen.blit(image, location)