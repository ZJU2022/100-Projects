"""
读取CSV文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13

csv 模块实现了 CSV 格式表单数据的读写。
其提供了诸如“以兼容 Excel 的方式输出数据文件”或“读取 Excel 程序输出的数据文件”的功能，
程序员无需知道 Excel 所采用 CSV 格式的细节。此模块同样可以用于定义其他应用程序可用的 CSV 格式或定义特定需求的 CSV 格式。
"""

import csv

def main():
    filename = 'example.csv'
    
    try:
        with open(filename,'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)
    except FileNotFoundError:
        print('文件不存键')
    
    else:
        #print(data)
        for item in data:
             #print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
             print(item)

if __name__ == '__main__':
    main()

