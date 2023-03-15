Day31~35 - 玩转Linux操作系统
操作系统发展史和Linux概述
Linux基础命令
Linux中的实用程序
Linux的文件系统
Vim编辑器的应用
环境变量和Shell编程
软件的安装和服务的配置
网络访问和管理
其他相关内容其他相关内容

======================

在windows上能够进行的任何操作都能在linux上进行

获取登录信息 - w / who / last/ lastb。
查看自己使用的Shell - ps。
查看命令的说明和位置 - whatis / which / whereis。
查看帮助文档 - man / info / --help / apropos。
查看系统和主机名 - uname / hostname。
时间和日期 - date / cal。
查找文件和查找内容 - find / grep。
压缩/解压缩
将标准输入转成命令行参数 - xargs。
下面的命令会将查找当前路径下的html文件，然后通过xargs将这些文件作为参数传给rm命令，实现查找并删除文件的操作。

[root@iZwz97tbgo9lkabnat2lo8Z ~]# find . -type f -name "*.html" | xargs rm -f
下面的命令将a.txt文件中的多行内容变成一行输出到b.txt文件中，其中<表示从a.txt中读取输入，>表示将命令的执行结果输出到b.txt中。

[root@iZwz97tbgo9lkabnat2lo8Z ~]# xargs < a.txt > b.txt
说明：这个命令就像上面演示的那样常在管道（实现进程间通信的一种方式）和重定向（重新指定输入输出的位置）操作中用到，后面的内容中会讲到管道操作和输入输出重定向操作。

（此往下，很重要）
其他相关工具。

sort - 对内容排序
uniq - 去掉相邻重复内容
tr - 替换指定内容为新内容
cut / paste - 剪切/黏贴内容
split - 拆分文件
file - 判断文件类型
wc - 统计文件行数、单词数、字节数
iconv - 编码转换

管道和重定向

管道和重定向
管道的使用 - |。

例子：查找当前目录下文件个数。

[root ~]# find ./ | wc -l
6152
例子：列出当前路径下的文件和文件夹，给每一项加一个编号。

[root ~]# ls | cat -n
     1  dump.rdb
     2  mongodb-3.6.5
     3  Python-3.6.5
     4  redis-3.2.11
     5  redis.conf
例子：查找record.log中包含AAA，但不包含BBB的记录的总数

[root ~]# cat record.log | grep AAA | grep -v BBB | wc -l
输出重定向和错误重定向 - > / >> / 2>。

[root ~]# cat readme.txt
banana
apple
grape
apple
grape
watermelon
pear
pitaya
[root ~]# cat readme.txt | sort | uniq > result.txt
[root ~]# cat result.txt
apple
banana
grape
pear
pitaya
watermelon
输入重定向 - <。

[root ~]# echo 'hello, world!' > hello.txt
[root ~]# wall < hello.txt
[root ~]#
Broadcast message from root (Wed Jun 20 19:43:05 2018):
hello, world!
[root ~]# echo 'I will show you some code.' >> hello.txt
[root ~]# wall < hello.txt
[root ~]#
Broadcast message from root (Wed Jun 20 19:43:55 2018):
hello, world!
I will show you some code.
多重定向 - tee。

下面的命令除了在终端显示命令ls的结果之外，还会追加输出到ls.txt文件中。

[root ~]# ls | tee -a ls.txt

文本处理

字符流编辑器 - sed。

sed是操作、过滤和转换文本内容的工具。

awk也是很强大的处理文本的工具

显示文件的第3行。
显示文件的第2列。
显示文件的最后一列。
输出末尾数字大于等于300的行。
...

‘’‘’‘’‘’‘’文件系统+磁盘管理
‘’‘’‘’‘’‘‘vim + shell脚本
高级技巧

比较多个文件。

[root ~]# vim -d foo.txt bar.txt

'''''''''''''计划任务
在指定的时间执行命令。

at - 将任务排队，在指定的时间执行。
atq - 查看待执行的任务队列。
atrm - 从队列中删除待执行的任务。
指定3天以后下午5点要执行的任务。

[root ~]# at 5pm+3days
at> rm -f /root/*.html
at> <EOT>
job 9 at Wed Jun  5 17:00:00 2019
查看待执行的任务队列。

[root ~]# atq
9       Wed Jun  5 17:00:00 2019 a root
从队列中删除指定的任务。

[root ~]$ atrm 9

'''''''''''''''''

远程连接

网络监听抓包 - tcpdump。

安全文件拷贝 - scp。

[root ~]# scp root@1.2.3.4:/root/guido.jpg hellokitty@4.3.2.1:/home/hellokitty/pic.jpg
文件同步工具 - rsync。

说明：使用rsync可以实现文件的自动同步，这个对于文件服务器来说相当重要。关于这个命令的用法，我们在后面讲项目部署的时候为大家详细说明。

安全文件传输 - sftp。

''''''''''''''''进程管理

查看进程 - ps。
显示进程状态树 - pstree。
进程管理，进程状态树，结束进程

将进程置于后台运行。
查询后台进程 - jobs。
让进程在后台继续运行 - bg。
将后台进程置于前台 - fg。
实时监控进程占用资源状况 - top。
.....

用到的时候再查


记住一个原则，任何能在GUI操作的，都可以命令行操作！

‘’‘’‘’‘’‘’‘shell编程
例子3：自动安装指定版本的Redis。

#!/usr/bin/bash
install_redis() {
    if ! which redis-server > /dev/null
    then
        cd /root
        wget $1$2'.tar.gz' >> install.log
        gunzip /root/$2'.tar.gz'
        tar -xf /root/$2'.tar'
        cd /root/$2
        make >> install.log
        make install >> install.log
        echo '安装完成'
    else
        echo '已经安装过Redis'
    fi
}

install_redis 'http://download.redis.io/releases/' $1













