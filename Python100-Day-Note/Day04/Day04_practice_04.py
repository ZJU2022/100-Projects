#列表切片
#和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表，代码如下所示。
def segment():
    print("=============================================================================================================")
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
segment()

fruits2 = fruits[1:4]
print(fruits2)
#正向切片，全部copy
fruits3 = fruits[:]
print(fruits3)
#反向切片，copy
fruits4 = fruits[::-1]
print(fruits4)
fruits5 = fruits[-3:-1]
print(fruits5)
segment()

#排序
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list2 = sorted(fruits)
print(list2)
list3 = sorted(fruits,reverse=True)
print(list3)
segment()

# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list2, key=len)
print(list4)
segment()

#倒序
list2.sort(reverse=True)
print(list2)
segment()

#生成式和生成器
f = [x for x in range(1,10)]
print(f)

f = [x+y for x in 'ABCDE' for y in "嘿嘿嘿嘿嘿"]
print(f)
