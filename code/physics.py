from pygame import Rect
bodies = []

class Body:
    def __init__(self, x=9, y=0, width=32, height=32):
        self.hitbox = Rect(x, y, width, height=32)
        bodies.append(self)
    
    def posision(self):
        for body in bodies:
            if body != self and body.collision(self):
                return False
        return True


    def collision(self, other):
        x = self.enemy.x + self.hitbox.x
        y = self.enemy.y + self.hitbox.y
        other_x = other.enemy.x + other.hitbox.x
        other_y = other.enemy.y + other.hitbox.y

        if x < other_x + other.hitbox.width and \
        x + self.hitbox.width > other_x and \
        y < other_y + other.hitbox.height and \
        y + self.hitbox.height > other_y:
            return True
        else:
            return False