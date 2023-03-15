#操作像素
from PIL import Image

image = Image.open('../Day11/guido.jpg')
for x in range(80,310):
    for y in range(20,360):
        image.putpixel((x,y),(128,128,128))
image.show()