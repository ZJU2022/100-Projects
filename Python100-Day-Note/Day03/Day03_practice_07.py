'''
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
'''

import time
import os
import shutil

seconds = time.time()
print(seconds)
localtime = time.localtime()
print(localtime)
print("=========================")
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
print("=========================")
asctime = time.asctime(localtime)
print(asctime)
print("--------------------------------------")
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
print("----------------------------------------")
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)
print("<-------------------------------->")
shutil.copy('/Users/linfeiwu/go/lfw_python_study/Day03/Day03_practice_07.py', '/Users/linfeiwu/Desktop/first.py')
os.system('ls -l')
os.chdir('/Users/linfeiwu')
os.system('ls -l')
os.mkdir('linfeiwu_test')
