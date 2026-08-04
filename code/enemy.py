active_objects = []

class Enemy:
    def __init__(self, *compoents, x=0, y=0):
        self.components = []
        for e in compoents:
            self.add(e)
        self.x = x
        self.y = y
    def add(self,component):
        self.components.append(component)
        component.enemy = self
    def remove(self, kind):
        e = self.get(kind)
        if e is not None:
            e.enemy = None
            self.components.remove(e)
    def has(self, kind):
        for e in self.components:
            if isinstance(e, kind):
                return True
        return False
    def get(self, kind):
        for e in self.components:
            if isinstance(e, kind):
                return e
        return None