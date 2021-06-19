from PIL import Image
import sys

image_path = sys.argv[1]
saved_path = sys.argv[2]
im = Image.open(image_path)
width = im.size[0]
height = im.size[1]

i = 0
result = bytearray(width*height)
for y in range(height):
    for x in range(width):
        coordinate = (x, y)
        color = im.getpixel(coordinate)
        alpha = color[3]
        if alpha == 0 or alpha == 1:
            color = 2
        elif color[0] == 0 and color[1] == 0 and color[2] == 0:
            color = 0
        else:
            color = 1
        result[i] = color
        i += 1
print(result)
f = open(saved_path, "wb")
f.write(result)
f.close()