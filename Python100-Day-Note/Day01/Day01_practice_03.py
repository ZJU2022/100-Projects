'''
分支结构: if elif else
'''

#用户身份验证

from re import X


username = input('请输入用户名:')
password = input('请输入口令：')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('success login!')
else:
    print('身份验证失败！')
    
'''
需要说明的是和C/C++、Java等语言不同，Python中没有用花括号来构造代码块而是使用了缩进的方式来表示代码的层次结构，
如果if条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了。
换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体。
缩进可以使用任意数量的空格，但通常使用4个空格，建议大家不要使用制表键或者设置你的代码编辑工具自动将制表键变成4个空格。

当然如果要构造出更多的分支，可以使用if...elif...else...结构或者嵌套的if...else...结构，
下面的代码演示了如何利用多分支结构实现分段函数求值。
分段函数求值

分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

'''

x = float(input('请输入自变量'))
if x > 1:
    fx = 3*x - 5
elif x>=-1 and x <=1: 
    fx = x + 2
else:
    fx = 5*x + 3
print('fx的结果为%d' %(fx))
'''
嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，所以能使用扁平化的结构时就不要使用嵌套。
'''

#练习1：英制单位英寸与公制单位厘米互换。
value = float(input('请输入长度:'))
unit = str(input('请输入单位:'))

if unit == '英寸' or unit == 'in':
    print("%.2f英寸=%.2f厘米" %(value,value*2.54))
elif unit == '厘米' or unit == 'cm':
    print('%.2f厘米=%.2f英寸' %(value,value/2.54))

#练习2:如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
score = float(input('请输入分数：'))
if score > 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:',grade)