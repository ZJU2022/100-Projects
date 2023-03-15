#从一段文字中提取出国内手机号码。
'''上面提到的re模块中的这些函数，实际开发中也可以用正则表达式对象的方法替代对这些函数的使用，如果一个正则表达式需要重复的使用，那么先通过compile函数编译正则表达式并创建出正则表达式对象无疑是更为明智的选择。'''
#findall(pattern, string) 查找字符串所有与正则表达式匹配的模式 返回字符串的列表
from distutils.filelist import findall
import re
def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    
    mylist = re.findall(pattern,sentence)
    print(mylist)
    
    
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    
    m = pattern.search(sentence)
    print(m)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())
    
    

if __name__ == '__main__':
    main()