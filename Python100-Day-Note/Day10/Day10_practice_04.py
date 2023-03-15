'''
Python 中的多线程

在Python早期的版本中就引入了thread模块（现在名为_thread）来实现多线程编程，
然而该模块过于底层，而且很多功能都没有提供，因此目前的多线程开发我们推荐使用threading模块，
该模块对多线程编程提供了更好的面向对象的封装。我们把刚才下载文件的例子用多线程的方式来实现一遍。
'''
from threading import Thread
from time import sleep,time
from random import randint

def download_file(filename):
    print('开始下载%s...' %filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成!耗费%d秒' %(filename,time_to_download))

def main():
    start = time()
    t1 = Thread(target=download_file, args=('《Python编程快速上手》',))
    t1.start()
    t2 = Thread(target=download_file, args=('《Java从入门到入土》',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('一共耗时%.2f秒' %(end-start))
    
    
    
    

if __name__ == '__main__':
    main()