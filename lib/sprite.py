from meowbit import screen, tft, framebuf, fb

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

    def load(self, path, width, height):
        f = open(path, "rb")
        content = f.read()
        f.close()
        self.bytes = bytearray(width * height * 2)
        for i in range(0, width*height*2, 2):
            color = content[int(i/2)]
            if color == 1:
                self.bytes[i] = 0xff
                self.bytes[i+1] = 0xff
            elif color == 0:
                self.bytes[i] = 0x00
                self.bytes[i] = 0x00
            else:
                self.bytes[i] = 0x02
                self.bytes[i+1] = 0x00
        self.width = width
        self.height = height
        self.fb = framebuf.FrameBuffer(self.bytes, width, height, framebuf.RGB565)

    def draw(self):
        if (self.drawing):
            return
        self.drawing = True
        fb.blit(self.fb, self.x, self.y, 0x02)
        self.drawing = False
    