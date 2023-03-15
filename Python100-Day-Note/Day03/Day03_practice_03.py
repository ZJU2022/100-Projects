#实现计算求最大公约数和最小公倍数的函数
from multiprocessing.sharedctypes import Value
from pickle import TRUE
def gcd(small,big):
    if small > big:
        small,big = big,small
    for i in range(int(range,0,-1)):
        if i % small == 0 and i % big == 0:
            return i
def LCM(small,big):
    value = gcd(small,big)
    return small*big//value

#判断是不是回文数
def is_palindrome(number):
    temp = number
    reversedNUmber = 0
    while temp > 0:
        reversedNUmber = reversedNUmber*10 + temp%10
        temp //= 10
    if reversedNUmber == number:
        ISPALINDROME = TRUE
    else:
        ISPALINDROME = False
    return ISPALINDROME

#判断一个数是不是素数
from math import sqrt
def is_Prime(number):
        for i in range(2,int(sqrt(number))):
            if number%i == 0:
                return False
        return True if number != 1 else False
       
        
        
        