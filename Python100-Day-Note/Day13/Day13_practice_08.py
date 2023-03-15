#函数的使用方式（高阶函数，lambda函数，闭包与作用域，装饰器函数）
'''
将函数视为“一等公民”

函数可以赋值给变量
函数可以作为函数的参数
函数可以作为函数的返回值
高阶函数的用法（filter、map以及它们的替代品）
'''
#filter函数（过滤序列）：https://www.runoob.com/python/python-func-filter.html
#lambda（匿名函数）：https://www.cainiaojc.com/python/python-anonymous-function.html
# map函数：https://www.runoob.com/python/python-func-map.html
items1 = list(map(lambda x:x**2, filter(lambda x:x%2,range(1,10))))
items2 = [x ** 2 for x in range(1, 10) if x % 2]
'''
位置参数、可变参数、关键字参数、命名关键字参数

参数的元信息（代码可读性问题）

匿名函数和内联函数的用法（lambda函数）

闭包和作用域问题

Python搜索变量的LEGB顺序（Local >>> Embedded >>> Global >>> Built-in）

global和nonlocal关键字的作用

global：声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。

nonlocal：声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。

闭包：https://www.cainiaojc.com/python/python-closure.html

装饰器函数（使用装饰器和取消装饰器）
Python 函数装饰器：https://www.runoob.com/w3cnote/python-func-decorators.html
'''
#https://www.runoob.com/w3cnote/python-one-and-two-star.html  （python *和**的区别）

        
    
