#拆分长字符串
'''如果要从事爬虫类应用的开发，那么正则表达式一定是一个非常好的助手，因为它可以帮助我们迅速的从网页代码中发现某种我们指定的模式并提取出我们需要的信息，
当然对于初学者来收，要编写一个正确的适当的正则表达式可能并不是一件容易的事情（当然有些常用的正则表达式可以直接在网上找找），所以实际开发爬虫应用的时候，
有很多人会选择Beautiful Soup或Lxml来进行匹配和信息的提取，前者简单方便但是性能较差，后者既好用性能也好，但是安装稍嫌麻烦，这些内容我们会在后期的爬虫专题中为大家介绍。
'''

import re


def main():
    poem = '李杜诗篇万口传，至今已觉不新鲜。江山代有人才出，各领风骚数百年。'
    sentence_list = re.split(r'[,.。，]',poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    main()