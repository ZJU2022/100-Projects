#裁剪图像
from PIL import Image

image = Image.open('../Day11/guido.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()
