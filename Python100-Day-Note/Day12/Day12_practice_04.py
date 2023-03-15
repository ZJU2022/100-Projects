#缩放和黏贴图像
from PIL import Image
image1 = Image.open('../Day11/luohao.png')
image2 = Image.open('../Day11/guido.jpg')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
image1.show()