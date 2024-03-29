#和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
# 它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
from time import localtime,sleep,time
class Clock:
    def __init__(self, hour,minute,second):
        self._hour = hour
        self._minute = minute
        self._second = second
        
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    
    def run(self):
        self._second += 1
        if  self._second == 60:
            self._second = 0
            self._minute +=1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 60:
                    self._hour = 0
    
    def show(self):
        print('%02d : %02d : %02d' %(self._hour,self._minute,self._second))
        

def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()