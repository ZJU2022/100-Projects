#生成缩略图
from PIL import Image

image = Image.open('../Day11/guido.jpg')
size = 128,128
image.thumbnail(size)
image.show()
