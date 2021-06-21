
FONT_WIDTH = 6
FONT_HEIGHT = 8

DESENDER_CHAR = "gjpqy"

f = open("font8.bin", "rb")
font8 = f.read()    
f.close()

class Font8():
    def __init__(self, set_pixel=None):
        self.set_pixel = set_pixel

    def get_data(self, ch):
        index = 8 * (ord(ch) -32)
        data = [font8[index], 
            font8[index+1], 
            font8[index+2],
            font8[index+3],
            font8[index+4],
            font8[index+5],
            font8[index+6],
            font8[index+7]
        ]
        return data

    def draw_char(self, ch, x, y, color):
        data = self.get_data(ch)
        print(data)
        for col in range(2, 8):
            vline = data[col]
            if (vline & 0x01) == 1:
                self.set_pixel(x, y, color)
            if ((vline & 0x02) >> 1) == 1:
                self.set_pixel(x, y + 1, color)
            if ((vline & 0x04) >> 2) == 1:
                self.set_pixel(x, y + 2, color)
            if ((vline & 0x08) >> 3) == 1:
                self.set_pixel(x, y + 3, color)
            if ((vline & 0x10) >> 4) == 1:
                self.set_pixel(x, y + 4, color)
            if ((vline & 0x20) >> 5) == 1:
                self.set_pixel(x, y + 5, color)
            if ((vline & 0x40) >> 6) == 1:
                self.set_pixel(x, y + 6, color)
            if ((vline & 0x80) >> 7) == 1:
                self.set_pixel(x, y + 7, color)
            x += 1

    def text(self, text, x, y, color):
        for ch in text:
            if ch in DESENDER_CHAR:
                self.draw_char(ch, x, y + 1, color)
            else:
                self.draw_char(ch, x, y, color)
            x += FONT_WIDTH

