'''
属性的使用，访问器/修改器/删除器
__slots__对属性限制
'''

'''
在学习面向对象的时候，我们知道在 python 中有一类特殊的方法，叫做魔法方法，这种方法的特点如下： 
1. 方法定义的时候以两个下划线开头和两个下划线结尾：如__init__、__str__和__repr__
2. 这类方法一般不需要我们手动调用，在满足某个条件的时候会自动调用，这个满足的条件我们可以成为调用时机。

在Python 中有两个魔法方法都是用来描述对象信息的，__str__和__repr__，那为什么要定义两个这样的方法呢，其实是他们设计的目的是不一样的： 
1. __repr__的目标是准确性，或者说，__repr__的结果是让解释器用的。
2. __str__的目标是可读性，或者说，__str__的结果是让人看的。
'''
#https://zhuanlan.zhihu.com/p/80911576


class Car:
    __slots__ = ('_brand','_max_speed')
    def __init__(self,brand,max_speed):
        self._brand = brand
        self._max_speed = max_speed
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,brand):
        self._brand = brand
    
    @brand.deleter
    def brand(self):
        del self._brand
    
    @property
    def max_speed(self):
        return self._brand
    
    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed
            
    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)
    
def main():
    car = Car('QQ',120)
    print(car)
    
    #car.max_speed = -100
    #ValueError: Invalid max speed for car
    car.brand = "Benz"
    print(car)
    
    #del car.brand
    
    # 属性的实现
    print(Car.brand)
    print(Car.brand.fget)
    print(Car.brand.fset)
    print(Car.brand.fdel)


if __name__ == '__main__':
    main()     
    
 
        