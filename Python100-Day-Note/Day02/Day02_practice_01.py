'''
循环结构
for-in循环
如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），那么我们推荐使用for-in循环，例如下面代码中计算1~100求和的结果

range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

while循环
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True则继续循环；表达式的值为False则结束循环。
'''
#for实现1～100求和
sum = 0
for i in range(0,101):
    sum += i
print("1~100和是%d" %(sum))
#1~100偶数求和
sum1 = 0
for i in range(0,100,2):
    sum1 += i
print("1~100偶数和为%d" %(sum1))

'''
猜数字游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
'''
import random
answer = random.randint(1,100)
count = 0
while True:
    count += 1
    value = int(input("请输入数字:"))
    if value > answer:
        print("大一点")
    elif value < answer:
        print("小一点")
    else:
        print("Right!")
        break
    if count > 7:
        print("请充值您的智商！")
        
    #输出乘法口诀表(九九表)
    
    for i in range(1,10):
        for j in range(1,10):
            print('%d*%d=%d' %(i,j,i*j),end='\t')
        print()