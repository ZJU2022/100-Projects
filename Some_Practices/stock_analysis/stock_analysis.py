'''
开发程序对stock_data.txt进⾏以下操作：
1. 程序启动后，给⽤户提供查询接⼝，允许⽤户᯿复查股票⾏情信息(⽤到循环)
2. 允许⽤户通过模糊查询股票名，⽐如输⼊“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来
3. 允许按股票价格、涨跌幅、换⼿率这⼏列来筛选信息，⽐如输⼊“价格>50”则把价格⼤于50的股票
都打印，输⼊“市盈率<50“，则把市盈率⼩于50的股票都打印，不⽤判断等于。
思路提示：加载⽂件内容到内存，转成dict or list结构，然后对dict or list 进⾏查询等操作。 这样以后
就不⽤每查⼀次就要打开⼀次⽂件了，效率会⾼。
'''

import re

# 开发程序对 stock_data.txt 进行以下操作：

f = open("stock_data.txt", encoding="utf-8")
headers = f.readline().strip().split(",")

stock_dic = {}
for line in f:
    line = line.strip().split(",")
    stock_dic[line[0]] = line

f.close()

# 1. 程序启动后，给用户提供查询接口，
# 允许用户**重复查**股票行情信息。
while True:
    cmd = input("请输入查询指令：")
    for s_id, s_data in stock_dic.items():
        s_name = s_data[1]
        # 2. 允许用户通过**模糊查询**股票名，
        # 比如输入“啤酒”, 就把所有名称当中包含啤酒的股票都打印出来。
        if cmd in s_name:
            print(s_data)

    # 3. 允许按 **当前价、涨跌幅、换手率**这几列来筛选信息，
    # 比如输入**“当前价>50**”则把价格大于50的股票都打印，
    # 输入“**涨跌幅<50**“，则把涨跌幅小于50的股票都打印，不用判断等于。

    # 公式查询
    # 1. 判断公式的合法性(正则表达式)
    cmd_parser = re.split("[<>]", cmd)
    #print(cmd_parser)
    if len(cmd_parser) != 2:
        print("输入的公式不合法，请重新输入！")
        continue

    # 2. 判断列名的合法性
    filter_column, filter_val = cmd_parser
    if filter_column not in ['当前价', '涨跌幅', '换手率']:
        print("输入的列名不合法，请重新输入！")
        continue

    # 3. 判断数值的合法性
    try:  # 尝试
        filter_val = float(filter_val)#此时filter_val是字符串，此处转换成数值类型
    except:
        print("输入的数值不合法，请重新输入！")
        continue

    # 4. 可以处理逻辑了
    # 4.1 取索引--------------------headers
    column_index = headers.index(filter_column)
    for s_id,s_data in stock_dic.items():
        if ">" in cmd:
            if float(s_data[column_index].strip("%")) > filter_val:
                print(s_data)
        else:
            if float(s_data[column_index].strip("%")) < filter_val:
                print(s_data)





