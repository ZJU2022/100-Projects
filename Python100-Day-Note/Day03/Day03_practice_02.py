#用模块管理函数
#Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的foo函数，代码如下所示。

from module1 import foo
foo()
#另一种方式区分用哪种foo
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()

'''
导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，
因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，
这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，
因为只有直接执行的模块的名字才是"__main__"。
'''
import module3 as m3
