#面向对象编程基础,封装，继承，多态
#类是对象的蓝图和模板，而对象是类的实例

#在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def study(self,course_name):
        print('%s在学%s' %(self.name,course_name))
        
    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    
    def watch_movie(self):
        if self.age < 18:
            print("您只能收看《熊出没》")
        else:
            print("Weclome to heihei")
        

def main():
    stu1 = Student('林飞武',22)
    stu1.study("《行为心理学》")
    stu1.watch_movie()
    #私有class
    
if __name__ == '__main__':
    main()