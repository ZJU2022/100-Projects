#列表
'''
不知道大家是否注意到，刚才我们讲到的字符串类型
（str）和之前我们讲到的数值类型
（int和float）有一些区别。
数值类型是标量类型，也就是说这种类型的对象没有可以访问的内部结构；
而字符串类型是一种结构化的、非标量类型，所以才会有一系列的属性和方法。接下来我们要介绍的列表
（list），也是一种结构化的、非标量类型，它是值的有序序列，
每个值都可以通过索引进行标识，定义列表可以将列表的元素放在[]中，多个元素用,进行分隔，
可以使用for循环对列表元素进行遍历，也可以使用[]或[:]运算符取出列表中的一个或多个元素。
'''
def segment():
    print("======================================")
    
list1 = [1,3,5,7,200]
print(list1)
list2 = ['hello','World',1]
print(list2*3)
segment()

print(list1)
print(list1[3])
print(list1[-1])
print(list1[-3])
segment()

list1[2] = 300
print(list1)
segment()

for index in range(len(list1)):
    print(list1[index],end=" ")
    print()
segment()
    
for enum in list1:
    print(enum)
segment()
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
    
segment()
list1 = [1,3,5,7,200]
list1.append(100)
print(list1)
list1.insert(1,400)
print(list1)
segment()

list1 += [1000,2000]
print(list1,len(list1))
segment()

#指定元素删除
if 3 in list1:
    list1.remove(3)
if 2000 in list1:
    list1.remove(2000)
print(list1)

#指定位置删除
list1.pop(0)
print(list1)
list1.pop(len(list1)-1)
print(list1)
segment()

#清空列表
list1.clear()
print(list1)






