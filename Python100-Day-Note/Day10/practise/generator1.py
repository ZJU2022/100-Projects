#https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128
#生成器语法
"""
生成器 - 生成器语法

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""
'''
我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
'''
seq = [x * x for x in range(10)]
print(seq)

gen = (x * x for x in range(10))
print(gen)
for x in gen:
    print(x)

num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)
n = 1
while n < num:
    print(next(gen))
    n += 1