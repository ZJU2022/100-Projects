#工资结算系统
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
#https://www.runoob.com/python/python-func-isinstance.html   isinstance() 函数

from abc import ABCMeta,abstractmethod

class Employee(object,metaclass = ABCMeta):
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def salary(self):
        pass
    

class Manager(Employee):
    def salary(self):
        return 15000.0

class Promager(Employee):
    def __init__(self,name,work_time=0):
        super().__init__(name)
        self._work_time = work_time if work_time > 0 else 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def work_time(self):
        return self._work_time
    
    @work_time.setter
    def work_time(self,work_time):
        self._work_time = work_time
        
        
    def salary(self):
        return 150.0*self._work_time

class Sales(Employee):
    def __init__(self,name,sales = 0):
        super().__init__(name)
        self._sales = sales
    
    @property
    def name(self):
        return self._name
    @property
    def sales(self):
        return self._sales
    
    @sales.setter
    def sales(self,sales):
        self._sales = sales
    
    def salary(self):
        return 0.05*self._sales + 1200
    

if __name__ == '__main__':
    emps = [Manager('张飞'),Sales('诸葛亮'),Sales('刘备'),Promager('林飞武')]
    
    for emp in emps:
        if isinstance(emp,Promager):
            emp.work_time = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Sales):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.salary()))
        
        
    
        