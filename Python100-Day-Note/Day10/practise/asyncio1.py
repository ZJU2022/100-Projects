#异步io操作，asyncio模块

import asyncio
import threading

@asyncio.coroutine

def hello():
    print('%s: hello, world!' % threading.current_thread())
    #主线程不会阻塞因为使用了异步io
    #yield from才会等待等待休眠执行完成
    yield from asyncio.sleep(3)
    print('%s GoodBye' % threading.current_thread())
    
'''
asyncio.get_event_loop()
返回当前 OS 线程中正在运行的事件循环。

如果没有正在运行的事件循环则会引发 RuntimeError。 此函数只能由协程或回调来调用
'''
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
#等待两个异步io操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()
'''
@asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，
线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
'''
