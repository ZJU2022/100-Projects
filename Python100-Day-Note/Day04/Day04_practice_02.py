def segment():
    print("=================================")
    
#处理字符串
str1 = 'hello, world!'
print(len(str1))
#获取字符串首字母大写的拷贝
print(str1.capitalize())
#获取字符串每个单词首字母大写的拷贝
print(str1.title())
#获取字符串变大写后拷贝
print(str1.upper())
segment()

#从字符串中查找子串的位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
segment()

#与find类似但找不到子串会引起异常-index
#print(str1.index('he'))
#print(str1.index('shift'))

#检查字符串是否以指定字符串开头
print(str1.startswith('hel'))
print(str1.startswith('helkl'))
#检查字符串是否以指定字符串结尾
print(str1.endswith('orld!'))
segment()

#将字符串以指定宽度居中并且填充*
print(str1.center(50,'*'))
#将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50,'&'))
segment()

str2 = 'abc123456'
#检查这个字符串是否由数字组成
print(str2.isdigit())
#检查这个字符是否由字母组成
print(str2.isalpha())
#检查这个字符是否由数字和字母组成
print(str2.isalnum())
segment()

str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
segment()

#用字符串提供的方法来完成字符串的格式，代码如下所示。
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

#Python 3.6以后，格式化字符串还有更为简洁的书写方式，
# 就是在字符串前加上字母f，我们可以使用下面的
# 语法糖来简化上面的代码。
'''
  语法糖（Syntactic sugar）：
    计算机语言中特殊的某种语法
    这种语法对语言的功能并没有影响
    对于程序员有更好的易用性
    能够增加程序的可读性
'''

print(f'{a} * {b} = {a*b}')
