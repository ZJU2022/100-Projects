#面向对象进阶，@property修饰器
'''
之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
比如我们没有办法检查赋给属性的值是否有效。我们之前
的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，那么如果想访问属性可以通过属性的getter（
访问器）和setter（修改器）方法进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便

https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208 
'''
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age
        return self._age
    
    def play(self):
        if self._age < 18:
            print('%s请看《熊出没》' %(self._name))
        else:
             print('%s请看《金瓶梅》' %(self._name))

def main():
    person = Person('林飞武',12)
    person.play()
    person.age = 22
    person.play()
     # person.name = '白元芳'  # AttributeError: can't set attribute
    
if __name__ == "__main__":
    main()