'''
#⽣成⼀个包含100个key的字典，每个value的值不能⼀样
mes = {}
for i in range(100):
    mes[i] = [i+1,"Good"]
print(mes)

mes1 = {'k0': 0, 'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6, 'k7': 7, 'k8': 8, 'k9': 9}
for k,v in mes1.items():
    if mes1[k] > 5:
        print(mes1[k])
    if mes1[k] % 2 == 0:
        mes1[k] = -1
        print(mes1)

2. {‘k0’: 0, ‘k1’: 1, ‘k2’: 2, ‘k3’: 3, ‘k4’: 4, ‘k5’: 5, ‘k6’: 6, ‘k7’: 7, ‘k8’: 8, ‘k9’: 9} 请把这个dict中key⼤于5的 值value打印出来。
3. 把题2中value是偶数的统⼀改成-1
'''

#请设计⼀个dict, 存储你们公司每个⼈的信息， 信息包含⾄少姓名、年龄、电话、职位、⼯资，并提供⼀个简单的查找接⼝，⽤户按你的要求输⼊要查找的⼈，你的程序把查到的信息打印出来
info = {
    "name":"小猿圈",
    "mission": "帮一千万极客高效学编程",
    "website": "http://apeland.com"
}
key = input("请输入你要查找的内容:")
print(info[key]) 