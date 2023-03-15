#定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from math import sqrt
class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    
    def move_to(self,x,y):
        self.x = x
        self.y = y
    
    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy
    
    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)
    
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    point = Point(3,5)
    print(point)
    
    point.move_to(3,6)
    print(point)
    
    point.move_by(-1,-1)
    print(point)
    
    other = Point(-9,19)
    distance = Point()
    distance = point.distance_to(other)
    print(distance)

if __name__ == '__main__':
    main()