from PIL import Image
import sys
from bit_array import BitArray

image_path = sys.argv[1]
saved_path = sys.argv[2]
im = Image.open(image_path)
width = im.size[0]
height = im.size[1]

result = BitArray()
for y in range(height):
    for x in range(width):
        coordinate = (x, y)
        color = im.getpixel(coordinate)
        if color != 0:
            color = 1
        result.append(color)

f = open(saved_path, "wb")
f.write(result.bytes)
f.close()