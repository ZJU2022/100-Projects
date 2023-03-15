#滤镜效果
from PIL import Image,ImageFilter
image = Image.open('../Day11/guido.jpg')
image.filter(ImageFilter.CONTOUR).show()