#并发编程
'''
Python中实现并发编程的三种方案：多线程、多进程和异步I/O。并发编程的好处在于可以提升程序的执行效率以及改善用户体验；
坏处在于并发的程序不容易开发和调试，同时对其他程序来说它并不友好。
多线程：Python中提供了Thread类并辅以Lock、Condition、Event、Semaphore和Barrier。
Python中有GIL来防止多个线程同时执行本地字节码，
这个锁对于CPython是必须的，因为CPython的内存管理并不是线程安全的，因为GIL的存在多线程并不能发挥CPU的多核特性。

需要用到时候来看：https://github.com/ZJU2022/Python-100-Days/blob/master/Day16-20/16-20.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md 
'''



