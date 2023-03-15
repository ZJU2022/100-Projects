'''
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
'''
from ssl import SSL_ERROR_SSL


a = 1
b = 1
print('%d, %d' %(a,b))
for i in range(18):
    sum = a + b
    a = b
    b = sum
    print(sum,end=' ')

'''
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
'''
value = int(input('请输入一个正整数：'))
reversed_num = 0
temp = value

while value > 0:
    reversed_num = reversed_num*10 + value%10
    value //= 10
    
if reversed_num == temp:
    print("这是一个回文数")
else:
    print("这不是一个回文数")

'''
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
'''
for i in range(1,10000):
    sum = 0
    temp = int(i/2)
    for j in range(1,temp+1):
        if i % j == 0:
            sum += i
    if sum == i:
        print("%d, " %(sum))
'''
输出1～100之间的素数
'''