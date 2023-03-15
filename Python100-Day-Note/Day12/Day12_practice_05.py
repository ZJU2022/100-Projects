#旋转和翻转
from PIL import Image

image = Image.open('../Day11/guido.jpg')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()