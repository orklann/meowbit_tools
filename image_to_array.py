from PIL import Image
import sys
from bit_array import BitArray

image_path = sys.argv[1]
saved_path = sys.argv[2]
im = Image.open(image_path)
width = im.size[0]
height = im.size[1]

result = bytearray()
for y in range(height):
    for x in range(width):
        coordinate = (x, y)
        color = im.getpixel(coordinate)
        alpha = color[3]
        if alpha == 0:
            color = 2
        elif color[0] == 0 and color[1] == 0 and color[2] == 0:
            color = 0
        else:
            color = 1
        result.append(color)

f = open(saved_path, "wb")
f.write(result)
f.close()