#https://deerchao.cn/tutorials/regex/regex.htm  正则表达式
#验证输入用户名和QQ号是否有效并给出对应的提示信息
import re

def main():
    username = input('请输入你的用户名')
    qq = input('请输入qq')
    
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print("请重新输入用户名")
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('请重新输入qq')
    if m1 and m2:
        print('你输入的信息是有效的!')

if __name__ == '__main__':
    main()
    
'''提示： 上面在书写正则表达式时使用了“原始字符串”的写法（在字符串前面加上了r），
所谓“原始字符串”就是字符串中的每个字符都是它原始的意义，说得更直接一点就是字符串中没有所谓的转义字符啦。
因为正则表达式中有很多元字符和需要进行转义的地方，如果不使用原始字符串就需要将反斜杠写作\\，例如表示数字的\d得书写成\\d，这样不仅写起来不方便，阅读的时候也会很吃力。'''