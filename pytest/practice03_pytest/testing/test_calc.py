# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_calc.py
#import allure
from python_code.calc import Calculator

def test_a():
    print("测试用例a")

#allure.feature("测试计算器")
class TestCalc:
    def setup_class(self):
        print("开始计算")
        #实例化计算器类
        self.calc = Calculator()
    def teardown_class(self):
        print("计算结束")
        
    def test_add(self):
        #calc = Calculator()
        result = self.calc.add(-1, -1)
        assert result == -2
    def test_add1(self):
        #calc = Calculator()
        result = self.calc.add(0.1, 0.1)
        assert result == 0.2
    def test_add2(self):
        #calc = Calculator()
        result = self.calc.add(1, 1)
        assert result == 2