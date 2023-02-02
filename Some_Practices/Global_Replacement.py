'''
2.10 练习题-全局⽂本检索替换
写⼀个脚本，允许⽤户按以下⽅式执⾏时，即可以对指定⽂件内容进⾏全局替换，且替换完毕后打印替
换了多少处内容
写完后的脚本调⽤⽅式：
python your_script.py old_str new_str filename
'''
import sys
sys.argv #执行这个脚本时传任何参数都会传输到这里面
#print(sys.argv)

f_name = sys.argv[3]
old_str = sys.argv[1]
new_str = sys.argv[2]

#load into memory
f = open(f_name,"r+")
data = f.read()

#count and replace
old_str_count = data.count(old_str)
new_data = data.replace(old_str,new_str)


#clear old filename
f.seek(0)
f.truncate()

# save new data into file
f.write(new_data)

print(f"成功替换字符{old_str}to{new_str}共{old_str_count}次")






