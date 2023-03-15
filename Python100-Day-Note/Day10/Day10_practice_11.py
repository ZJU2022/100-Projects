#我们来完成1~100000000求和的计算密集型任务，这个问题本身非常简单，有点循环的知识就能解决，代码如下所示。

from time import time

def main():
    result = 0
    number_list = [x for x in range(1,100000001)]
    
    start = time()
    
    for number in number_list:
        result += number
    
    print(result)


if __name__ == '__main__':
    main()