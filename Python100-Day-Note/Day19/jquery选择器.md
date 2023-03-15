jquery选择器
什么是jQuery选择器
jQuery选择器是jQuery为我们提供的一组方法，让我们更加方便的获取到页面中的元素。
注意：jQuery选择器返回的是jQuery对象。
jQuery选择器有很多，基本兼容了CSS1到CSS3所有的选择器，并且jQuery还添加了很多扩展性的选择器。
【查看jQuery文档】
jQuery选择器虽然很多，但是选择器之间可以相互替代，就是说获取一个元素，你会有很多种方法获取到。
所以我们平时真正能用到的只是少数的最常用的选择器。
基本选择器
名称	用法	描述
ID选择器	$(“#id”);	获取指定ID的元素
类选择器	$(“.class”);	获取同一类class的元素
标签选择器	$(“div”);	获取同一类标签的所有元素
并集选择器	$(“div,p,li”);	使用逗号分隔，只要符合条件之一就可。
交集选择器	$(“div.redClass”);	获取class为redClass的div元素
总结：跟css的选择器用法一模一样。

层级选择器
名称	用法	描述
子代选择器	$(“ul>li”);	使用>号，获取儿子层级的元素，注意，并不会获取孙子层级的元素
后代选择器	$(“ul li”);	使用空格，代表后代选择器，获取ul下的所有li元素，包括孙子等
总结：跟css的选择器用法一模一样。

过滤选择器
名称	用法	描述
:eq（index）	$(“li:eq(2)”).css(“color”, ”red”);	获取到的li元素中，选择索引号为2的元素，索引号index从0开始。
:odd	$(“li:odd”).css(“color”, ”red”);	获取到的li元素中，选择索引号为奇数的元素
:even	$(“li:even”).css(“color”, ”red”);	获取到的li元素中，选择索引号为偶数的元素
总结：这类选择器都带冒号

筛选选择器(方法)
名称	用法	描述
children(selector)	$(“ul”).children(“li”)	相当于$(“ul>li”)，子类选择器
find(selector)	$(“ul”).find(“li”);	相当于$(“ul li”),后代选择器
siblings(selector)	$(“#first”).siblings(“li”);	查找兄弟节点，不包括自己本身。
parent()	$(“#first”).parent();	查找父亲
eq(index)	$(“li”).eq(2);	相当于$(“li:eq(2)”),index从0开始
next()	$(“li”).next()	找下一个兄弟
prev()	$(“li”).prev()	找上一次兄弟
总结：筛选选择器的功能与过滤选择器有点类似，但是用法不一样，筛选选择器主要是方法。

