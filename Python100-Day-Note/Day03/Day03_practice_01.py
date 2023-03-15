'''
函数是绝大多数编程语言中都支持的一个代码的"构建块"，但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，
其中一个显著的区别就是Python对函数参数的处理。
在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持函数的重载，
因为我们在定义一个函数的时候可以让它有多种不同的使用方式，下面是两个小例子。
'''

#求阶乘
def fac(m):
    result = 1
    for i in range(1,m+1):
        result *= i
    return result

m = int(input('请输入需要求阶乘的数：'))
print(fac(m))

#摇色子
from random import randint
def roll_dice(n=2):
    sum = 0
    for i in range(n):
        sum += randint(1,6)
    return sum
def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c
print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
print("===========================================")

# 在参数名前面的*表示args是一个可变参数
def add2(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add2())
print(add2(1))
print(add2(1, 2))
print(add2(1, 2, 3))
print(add2(1, 3, 5, 7, 9))



