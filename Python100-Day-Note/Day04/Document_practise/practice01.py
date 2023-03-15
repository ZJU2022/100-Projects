#在屏幕上显示跑马灯文字
import os
import time
from turtle import clear

def main():
    content = '欢迎您来到美丽的乐山。。。。。。。'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:]+content[0]

if __name__ == '__main__':
    main()
        