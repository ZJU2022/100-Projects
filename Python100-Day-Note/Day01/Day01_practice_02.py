'''
变量和类型:int,float,string,boolean,复数
命令：多个单词下划线连接，受保护的实例属性用单个下划线开头（后面会讲到）。私有的实例属性用两个下划线开头（后面会讲到）
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。


'''


#使用变量保存数据来进行加减乘除
from operator import truediv


a = 12
b = 99
c = 1+5j
d = 99.87
e = 'linfeiwu'
f = True

g = int(d)
h = str(f)
i = ord('a')
j = chr(a)
l = float(b)

print("Welcome to practise")
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=============================")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(3))
print(type(e))
print(type(f))


print("=============================")
print(g)
print(type(g))
print(h)
print(i)
print(l)
print(type(j))

'''
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
'''
print("=============================")
print('请输入整数')
a = int(input('a='))
b = int(input('b='))
print('%d+%d=%d' %(a,b,a+b))
print('%d-%d=%d' %(a,b,a-b))
print('%d*%d=%d' %(a,b,a*b))
print('%d/%d=%d' %(a,b,a/b))
print('%d//%d=%d' %(a,b,a//b))
print('%d %% %d =%d' %(a,b,a%b))
print('%d ** %d = %d' % (a, b, a ** b))

'''
[] [:]	下标，切片
**	指数
~ + -	按位取反, 正负号
* / % //	乘，除，模，整除
+ -	加，减
>> <<	右移，左移
&	按位与
^ |	按位异或，按位或
<= < > >=	小于等于，小于，大于，大于等于
== !=	等于，不等于
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
= += -= *= /= %= //= **= &= `	= ^= >>= <<=`
'''
print("=============================")
a += b
print(a)
a *= a+2
print(a)
'''
比较运算符和逻辑运算符
'''
print("=============================")
flag0 = 1 == 1
flag1 = 1 > 2
flag2 = 1 < 2
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)
print('flag0 =', flag0)  
print('flag1 =', flag1)    
print('flag2 =', flag2)    
print('flag3 =', flag3)    
print('flag4 =', flag4)   
print('flag5 =', flag5)    

print("=============================")
print('practice1: 华氏温度转换为摄氏温度。华氏温度到摄氏温度的转换公式为1:$C=(F - 32) \div 1.8$。')

f = float(input('请输入华氏温度'))
c = (f-32)/1.8
print('%.1f华氏度=%.1f摄氏度' %(f,c)) 

print("=============================")
print('practice2: 输入圆的半径计算周长和面积')
r = float(input('请输入圆的半径'))
C = 2*3.14*r
S = 3.14*r*r
print('圆的周长为%.1f;圆的面积为%.1f' %(C,S))

print("=============================")
print('practice3: 输入年份判断是不是闰年')
year = int(input('请输入年份'))
is_leapyear = (year%4==0 and year%100 != 0) or year%400==0
print(is_leapyear)