https://github.com/ZJU2022/Python-100-Days/blob/master/Day36-40/40.%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%B9%B3%E5%8F%B0%E5%92%8CHiveSQL.md
Hive是Facebook开源的一款基于Hadoop的数据仓库工具，是目前应用最广泛的大数据处理解决方案，它能将SQL查询转变为 MapReduce（Google提出的一个软件架构，用于大规模数据集的并行运算）任务，对SQL提供了完美的支持，能够非常方便的实现大数据统计。

1. 搭建大数据平台
2. 通过Client节点访问大数据平台
3. 创建文件Hadoop的文件系统。

hadoop fs -mkdir /data
hadoop fs -chmod g+w /data
将准备好的数据文件拷贝到Hadoop文件系统中。

hadoop fs -put /home/ubuntu/data/* /data

4. 然后对数据库进行增删查改
5. 