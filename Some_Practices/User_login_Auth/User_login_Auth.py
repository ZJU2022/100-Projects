'''
要求⽤户输⼊帐号密码进⾏登陆
⽤户账号信息保存在⽂件内
⽤户密码输⼊错误三次后锁定⽤户，下次再登录，检测到是这个被锁定的⽤户，则依然不允许其它
登录，提示已被锁
'''

#1. 确定 在文件里存储的账号信息的结构,0未锁定，1锁定
#2. 把账号数据读到内存，为了方便调用可以改成列表，字典之类的结构
accounts = {
   # "alex":["alex","abc123!","1"]
}
f = open("User_infomation.db",mode="r")
for line in f:
    line = line.strip().split(",")#strip去掉/n
    accounts[line[0]] = line
print(accounts)
#3, 一个循环，要求用户输入账户信息去判断就可以了
while True:
    accounts_id = input("Username:")
    if accounts_id not in accounts:
        print("该用户未注册")
        continue
    elif accounts[accounts_id][2] == "1":#代表此账号已锁定
        print("此账户已锁定，请联系管理员..")
        continue        
    count = 0
    while count < 3: #控制密码
        passwd = input("password:").strip()
        #dict里判断passwd对不对
        if passwd == accounts[accounts_id][1]:
            print(f"{accounts_id} login success")
            exit()
        else:
            print("Wrong password...")
        count += 1
    if count == 3:
        print(f"输错了{count}次密码，需要锁定账号{accounts_id}")
        #锁定账户1. 先改在内存中dict账号信息的用户信息
        #2. 把dict里的数据转成原account.db数据格式，并且存回文件
        accounts[accounts_id][2] = "1"
        f2 = open("User_infomation.db",mode="w")
        for user,val in accounts.items():
            line = ",".join(val)
            f2.write(line)
        f2.close()
        exit("bye")
    


