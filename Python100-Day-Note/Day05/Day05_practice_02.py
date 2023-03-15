#Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。
class Test:
    def __init__(self,name):
        self.__name = name
    
    def __foo(self):
        print("hello,%s", self.name)
  
def main():
    test1 = Test('林飞武')
    test1.__foo()
    print(test1.__name)

#Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们，


if __name__ == '__main__':
    main()

