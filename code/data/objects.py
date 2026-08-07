from components.entity import Entity
from components.sprite import Sprite
from components.player import Player
from components.physics import Body

entity_factory = [
    lambda args: Entity(Player(), Body(1, 23, 38, 20), Sprite("Caltheros_right.png")),
]

def create_entity(id, x, y, data=None):
    factory = entity_factory[id]
    e = factory(data)
    e.x = x*32
    e.y = y*32
    return e