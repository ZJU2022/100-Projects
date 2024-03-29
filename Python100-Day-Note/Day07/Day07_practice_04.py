'''
加载图像
如果需要直接加载图像到窗口上，可以使用pygame中image模块的函数来加载图像，再通过之前获得的窗口对象的blit方法渲染图像，代码如下所示。
'''

import pygame
def main():
    #初始化导入大pygame中的模块
    pygame.init()
    #初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800,600))
    #设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    #设置当前窗口的颜色
    screen.fill((255,255,255))
    #通过指定的文件名加载图像
    ball_image = pygame.image.load('/Users/linfeiwu/go/lfw_python_study/res/ball.png')
    # 在窗口上渲染图像
    screen.blit(ball_image, (50, 50))
    #刷新当前窗口
    pygame.display.flip()
    running = True
    #开启一个事件循环处理发生的事件
    while running:
        #从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
