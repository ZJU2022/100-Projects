#读写json
'''
JSON是“JavaScript Object Notation”的缩写，它本来是JavaScript语言中创建对象的一种字面量语法，
现在已经被广泛的应用于跨平台跨语言的数据交换，原因很简单，因为JSON也是纯文本，任何系统任何编程语言处理纯文本都是没有问题的。
目前JSON基本上已经取代了XML作为异构系统间交换数据的事实标准。关于JSON的知识，更多的可以参考JSON的官方网站，从这个网站也可以了解到每种语言处理JSON数据格式可以使用的工具或三方库

json 格式可以很轻易找到python对应数据类型
我们使用Python中的json模块就可以将字典或列表以JSON格式保存到文件中

json模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
'''

import json
def main():
    mydict = {
        'name':'linfeiwu',
        'age':'22',
        'qq': 213123123,
        'friends':['王大锤','李元芳'],
        'cars':[
            {'brand':'BYD','maxspeed':80},
            {'brand':'Audi','maxspeed':280},
            {'brand':'Benz','maxspeed':320}
        ]
    } 
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    
    print('保存数据完成！')
        
if __name__ == '__main__':
    main()


