'''
序列化与反序列化

这里出现了两个概念，一个叫序列化，一个叫反序列化。自由的百科全书维基百科上对这两个概念是这样解释的：“序列化（serialization）
在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，
可以利用这些字节来产生原始对象的副本（拷贝）。与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）”。

目前绝大多数网络数据服务（或称之为网络API）都是基于HTTP协议提供JSON格式的数据，关于HTTP协议的相关知识，
可以看看阮一峰老师的《HTTP协议入门》，如果想了解国内的网络数据服务，可以看看聚合数据和阿凡达数据等网站，国外的可以看看{API}Search网站。下面的例子演示了如何使用requests模块（封装得足够好的第三方网络访问模块）
访问网络API获取国内新闻，如何通过json模块解析JSON数据并显示新闻标题，这个例子使用了天行数据提供的国内新闻数据接口，其中的APIKey需要自己到该网站申请。

在Python中要实现序列化和反序列化除了使用json模块之外，还可以使用pickle和shelve模块，但是这两个模块是使用特有的序列化协议来序列化数据，因此序列化后的数据只能被Python识别。关
于这两个模块的相关知识可以自己看看网络上的资料。另外，如果要了解更多的关于Python异常机制的知识，
可以看看segmentfault上面的文章《总结：Python中的异常处理》，这篇文章不仅介绍了Python中异常机制的使用，还总结了一系列的最佳实践，很值得一读。
'''

import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()