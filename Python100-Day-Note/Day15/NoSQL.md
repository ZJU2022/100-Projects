NoSQL数据库按照其存储类型可以大致分为以下几类：

类型	部分代表	特点
列族数据库	HBase
Cassandra
Hypertable	顾名思义是按列存储数据的。最大的特点是方便存储结构化和半结构化数据，方便做数据压缩，对针对某一列或者某几列的查询有非常大的I/O优势，适合于批量数据处理和即时查询。
文档数据库	MongoDB
https://github.com/ZJU2022/Python-100-Days/blob/master/Day36-40/NoSQL%E6%95%B0%E6%8D%AE%E5%BA%93%E5%85%A5%E9%97%A8.md 

CouchDB
ElasticSearch	文档数据库一般用类JSON格式存储数据，存储的内容是文档型的。这样也就有机会对某些字段建立索引，实现关系数据库的某些功能，但不提供对参照完整性和分布事务的支持。
KV数据库	DynamoDB
Redis
LevelDB	可以通过key快速查询到其value，有基于内存和基于磁盘两种实现方案。
图数据库	Neo4J
FlockDB
JanusGraph	使用图结构进行语义查询的数据库，它使用节点、边和属性来表示和存储数据。图数据库从设计上，就可以简单快速的检索难以在关系系统中建模的复杂层次结构。
对象数据库	db4o
Versant	通过类似面向对象语言的语法操作数据库，通过对象的方式存取数据。

根据自己的需求，选择具体的数据库，然后按照help来解决问题就行。

Redis概述
Redis是一种基于键值对的NoSQL数据库，它提供了对多种数据类型（字符串、哈希、列表、集合、有序集合、位图等）的支持，能够满足很多应用场景的需求。Redis将数据放在内存中，因此读写性能是非常惊人的。与此同时，Redis也提供了持久化机制，能够将内存中的数据保存到硬盘上，在发生意外状况时数据也不会丢掉。此外，Redis还支持键过期、地理信息运算、发布订阅、事务、管道、Lua脚本扩展等功能，总而言之，Redis的功能和性能都非常强大，如果项目中要实现高速缓存和消息队列这样的服务，直接交给Redis就可以了。目前，国内外很多著名的企业和商业项目都使用了Redis，包括：Twitter、Github、StackOverflow、新浪微博、百度、优酷土豆、美团、小米、唯品会等。

Redis的应用场景
高速缓存 - 将不常变化但又经常被访问的热点数据放到Redis数据库中，可以大大降低关系型数据库的压力，从而提升系统的响应性能。
排行榜 - 很多网站都有排行榜功能，利用Redis中的列表和有序集合可以非常方便的构造各种排行榜系统。
商品秒杀/投票点赞 - Redis提供了对计数操作的支持，网站上常见的秒杀、点赞等功能都可以利用Redis的计数器通过+1或-1的操作来实现，从而避免了使用关系型数据的update操作。
分布式锁 - 利用Redis可以跨多台服务器实现分布式锁（类似于线程锁，但是能够被多台机器上的多个线程或进程共享）的功能，用于实现一个阻塞式操作。
消息队列 - 消息队列和高速缓存一样，是一个大型网站不可缺少的基础服务，可以实现业务解耦和非实时业务削峰等特性，这些我们都会在后面的项目中为大家展示。


进入Python交互式环境，使用redis三方库来操作Redis。


MongoDB
MongoDB将数据存储为一个文档，一个文档由一系列的“键值对”组成，其文档类似于JSON对象，但是MongoDB对JSON进行了二进制处理（能够更快的定位key和value），因此其文档的存储格式称为BSON。

SQL	MongoDB
database	database
table（表）	collection（集合）
row（行）	document（文档）
column（列）	field（字段）
index	index
table joins（表连接）	（嵌套文档）
primary key	primary key

通过Shell操作MongoDB
启动命令行工具，进入交互式环境。

mongo
说明：

查看、创建和删除数据库。

> // 显示所有数据库
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> // 创建并切换到school数据库
> use school
switched to db school
> // 删除当前数据库
> db.dropDatabase()
{ "ok" : 1 }
创建、删除和查看集合。

> // 创建并切换到school数据库
> use school
switched to db school
> // 创建colleges集合
> db.createCollection('colleges')
{ "ok" : 1 }
> // 创建students集合
> db.createCollection('students')
{ "ok" : 1 }
> // 查看所有集合
> show collections
colleges
students
> // 删除colleges集合
> db.colleges.drop()
true
说明：在MongoDB中插入文档时如果集合不存在会自动创建集合，所以也可以按照下面的方式通过插入文档来创建集合。

文档的CRUD操作。

> // 向students集合插入文档
> db.students.insert({stuid: 1001, name: '骆昊', age: 40})
WriteResult({ "nInserted" : 1 })
> // 向students集合插入文档
> db.students.save({stuid: 1002, name: '王大锤', tel: '13012345678', gender: '男'})
WriteResult({ "nInserted" : 1 })
> // 查看所有文档
> db.students.find()
{ "_id" : ObjectId("5b13c72e006ad854460ee70b"), "stuid" : 1001, "name" : "骆昊", "age" : 38 }
{ "_id" : ObjectId("5b13c790006ad854460ee70c"), "stuid" : 1002, "name" : "王大锤", "tel" : "13012345678", "gender" : "男" }
> // 更新stuid为1001的文档
> db.students.update({stuid: 1001}, {'$set': {tel: '13566778899', gender: '男'}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> // 插入或更新stuid为1003的文档
> db.students.update({stuid: 1003}, {'$set': {name: '白元芳', tel: '13022223333', gender: '男'}},  upsert=true)
WriteResult({
        "nMatched" : 0,
        "nUpserted" : 1,
        "nModified" : 0,
        "_id" : ObjectId("5b13c92dd185894d7283efab")
})
> // 查询所有文档
> db.students.find().pretty()
{
        "_id" : ObjectId("5b13c72e006ad854460ee70b"),
        "stuid" : 1001,
        "name" : "骆昊",
        "age" : 38,
        "gender" : "男",
        "tel" : "13566778899"
}
{
        "_id" : ObjectId("5b13c790006ad854460ee70c"),
        "stuid" : 1002,
        "name" : "王大锤",
        "tel" : "13012345678",
        "gender" : "男"
}
{
        "_id" : ObjectId("5b13c92dd185894d7283efab"),
        "stuid" : 1003,
        "gender" : "男",
        "name" : "白元芳",
        "tel" : "13022223333"
}
> // 查询stuid大于1001的文档
> db.students.find({stuid: {'$gt': 1001}}).pretty()
{
        "_id" : ObjectId("5b13c790006ad854460ee70c"),
        "stuid" : 1002,
        "name" : "王大锤",
        "tel" : "13012345678",
        "gender" : "男"
}
{
        "_id" : ObjectId("5b13c92dd185894d7283efab"),
        "stuid" : 1003,
        "gender" : "男",
        "name" : "白元芳",
        "tel" : "13022223333"
}
> // 查询stuid大于1001的文档只显示name和tel字段
> db.students.find({stuid: {'$gt': 1001}}, {_id: 0, name: 1, tel: 1}).pretty()
{ "name" : "王大锤", "tel" : "13012345678" }
{ "name" : "白元芳", "tel" : "13022223333" }
> // 查询name为“骆昊”或者tel为“13022223333”的文档
> db.students.find({'$or': [{name: '骆昊'}, {tel: '13022223333'}]}, {_id: 0, name: 1, tel: 1}).pretty()
{ "name" : "骆昊", "tel" : "13566778899" }
{ "name" : "白元芳", "tel" : "13022223333" }
> // 查询学生文档跳过第1条文档只查1条文档
> db.students.find().skip(1).limit(1).pretty()
{
        "_id" : ObjectId("5b13c790006ad854460ee70c"),
        "stuid" : 1002,
        "name" : "王大锤",
        "tel" : "13012345678",
        "gender" : "男"
}
> // 对查询结果进行排序(1表示升序，-1表示降序)
> db.students.find({}, {_id: 0, stuid: 1, name: 1}).sort({stuid: -1})
{ "stuid" : 1003, "name" : "白元芳" }
{ "stuid" : 1002, "name" : "王大锤" }
{ "stuid" : 1001, "name" : "骆昊" }
> // 在指定的一个或多个字段上创建索引
> db.students.ensureIndex({name: 1})
{
        "createdCollectionAutomatically" : false,
        "numIndexesBefore" : 1,
        "numIndexesAfter" : 2,
        "ok" : 1
}
使用MongoDB可以非常方便的配置数据复制，通过冗余数据来实现数据的高可用以及灾难恢复，也可以通过数据分片来应对数据量迅速增长的需求。关于MongoDB更多的操作可以查阅官方文档 ，同时推荐大家阅读Kristina Chodorow写的《MongoDB权威指南》。

