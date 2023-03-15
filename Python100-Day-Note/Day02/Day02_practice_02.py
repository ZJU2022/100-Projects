'''
练习1：输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。
'''
from math import sqrt

value = int(input('请输入一个正整数:'))
if value == 1:
    print('%d不是素数' %(value))
else:
    end = int(sqrt(value))+1
    for i in range(2,end):
        if value % i == 0:
            isPrime = False
        else:
            isPrime = True
    print(isPrime)
'''
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
'''

small = int(input('请输入正整数1:'))
big = int(input('请输入正整数2:'))

if small > big:
    small,big = big,small
for i in range(small,1,-1):
    if small % i == 0 and big % i == 0:
        resultBig = i
        resultSmall = big*small // i
        print('最大公约数%d 最小公倍数%d' %(resultBig,resultSmall))
        break

#打印三角图形
row = int(input('请输入行数:'))
for i in range(row+1):
    for _ in range(i):
        print('*',end=" ")
    print()
print("=========================")
    
#打印倒三角
'''
    *
   **
  ***
 ****
*****
'''

for i in range(1,row+1):
    #1,2,3,4,5行,row = 5
    #i = 1,4个空格，1个*
    #i = 2,3个空格，2个*
    #i = 3,2个空格，4个*
    #第i行  需要row-
    #j = 1,2,3,4,5
    for j in range(1,row+1):
        if j < row-i+1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
print("=========================")
'''
    *
   ***
  *****
 *******
*********
'''
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()


