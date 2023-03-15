#异步I/O操作 - async和await


#通过async修饰的函数不再是普通函数而是一个协程
#通过async和await将在Python3.7中作为关键词出现
import asyncio
import threading

async def hello():
    print('%s Hello' % threading.current_thread()) 
    await asyncio.sleep(2)
    print('%s Goodbye' %threading.current_thread())
    

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
'''
loop.run_until_complete(future)
运行直到 future ( Future 的实例 ) 被完成。

如果参数是 coroutine object ，将被隐式调度为 asyncio.Task 来运行。

返回 Future 的结果 或者引发相关异常。
'''
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
'''
    