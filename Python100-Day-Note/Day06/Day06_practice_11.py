'''
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

super():https://www.runoob.com/python/python-func-super.html
'''


class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo fo C')


class D(B, C):
    pass


class E(D):

    def foo(self):
        print('foo in E')
        #super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        #Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
        super().foo() # foo fo C
        super(B, self).foo() #foo to C
        super(C, self).foo() #foo to A


if __name__ == '__main__':
    d = D() 
    d.foo()  #foo fo C
    e = E()
    e.foo()


