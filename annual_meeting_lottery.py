'''
年会抽奖程序
张三科技有限公司有300员⼯，开年会抽奖，奖项如下：
⼀等奖 3名， 泰国5⽇游
⼆等奖6名，Iphone⼿机
三等奖30名，避孕套⼀盒
规则：
1. 共抽3次，第⼀次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
2. 每个员⼯限中奖⼀次，不能重复
解题思路：
1. ⽣成⼀个员⼯列表，⽤random模块从⾥⾯取随机值
2. 取完值之后，⽴刻从员⼯⼤列表⾥把中奖⼈删掉，即可防⽌其再次中奖
'''
import random
EmployeeList = []
for i in range(300):
    EmployeeList.append(f'员工{i}')

level = [30,6,3]
count = 0
while count < 3:
    choice = input(f'开始抽{3-count}奖:')
    winners = random.sample(EmployeeList,level[count])
    print(winners)
    for p in winners:
        EmployeeList.remove(p)
    count += 1
    
