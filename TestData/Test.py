'''
要求⽤户输⼊帐号密码进⾏登陆
⽤户账号信息保存在⽂件内
⽤户密码输⼊错误三次后锁定⽤户，下次再登录，检测到是这个被锁定的⽤户，则依然不允许其它
登录，提示已被锁
'''

#先把data.txt文件读进来,放入account一个数据结构用字典存储,即从硬盘写入内存，
#0表示未锁定，1表示锁定
accounts = {
   # "alex":["alex","abc123!","1"]
}

f = open('data.txt',mode='r')
for line in f:
    line = line.strip().split(',')
    accounts[line[0]] = line

while True:
    user = input('Username:')
    if user not in accounts:
        print("此账户不存在!")
        continue
    elif accounts[user][2] == '1':
        print(f'账户{user}已被锁定，请联系管理员')
        continue
    count = 0
    while count < 3:
        passwd = input('password:')
        if passwd == accounts[user][1]:
            print("login success!")
            exit()
        else:
            print("login failed,Please try again")
        count += 1
    
    if count == 3:
        print(f"输错了{count}次密码，需要锁定账号{user}")
        #错误3次以上，需要把当前username的值变为1，然后把当前accounts从内存写入硬盘
        accounts[user][2] = "1"
        f2 = open('data.txt',mode="w")
        for usr,val in accounts.items():
            line = ",".join(val)
            f2.write(line)
        f2.close()
        exit("bye")
        
    