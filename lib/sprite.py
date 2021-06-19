from meowbit import screen

_sprites = []

class Sprite():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        global _sprites
        _sprites.append(self)
        self.drawing = False

    def load(self, path):
        f = open(path, "rb")
        self.bytes = f.read()
        f.close()

    def draw(self):
        if (self.drawing):
            return
        self.drawing = True
        i = 0
        for y in range(self.height):
            for x in range(self.width):
                xx = self.x + x
                yy = self.y + y
                color = self.bytes[i]
                if color != 0 and color != 2:
                    color = 255
                if color != 2:
                    screen.pixel(xx, yy, color=color)
                i += 1
        self.drawing = False
    