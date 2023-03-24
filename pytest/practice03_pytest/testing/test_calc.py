# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_calc.py
#import allure
from python_code.calc import Calculator
import pytest
import yaml

'''
@pytest.mark.parametrize("a, b, expect",[(1,1,2),(0.1,0.1,0.2),(-1,-1,-2),(0.1,0.2,0.3)],ids=['int','float','negative','round'])
def test_add9(self,a,b,expect): 
        calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect
'''

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']

'''
#用fixture代替setup与teardown,然后放到conftest里面

@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
   return calc

@pytest.fixture(params=add_datas, ids=myid)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的测试数据是：{data}")
    yield data
    print("结束计算")
'''    
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
        
    @pytest.mark.parametrize(
        "a, b, expect",
         add_datas, ids=myid
     )
    #pytest test_calc.py -k add就只运行标签为add的case，通过标签来选择执行测试用例
    @pytest.mark.add  #pytest.ini定义了mark有add，加法
    def test_add(self, a, b, expect): # def test_add(self,get_calc, a, b, expect):
        #calc = Calculator()
        result = self.calc.add(a, b) #result = get_calc.add(a,b)
        assert result == expect
    @pytest.mark.add
    def test_add5(self,get_calc, get_add_datas):
        result = None
        try:
            result = get_calc.add(get_add_datas[0],get_add_datas[1])
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]
    
    def test_add1(self):
        #calc = Calculator()
        result = self.calc.add(0.1, 0.1)
        assert result == 0.2
    def test_add2(self):
        #calc = Calculator()
        result = self.calc.add(1, 1)
        assert result == 2
    @pytest.mark.add
    def test_add2(self, get_calc):
        result = get_calc.add(0.1, 0.2)
        assert round(result, 2) == 0.3
# pytest -vs test_calc.py -k div 指定标签为div的执行
    @pytest.mark.div
    def test_div(self):
        print("test_div")
        
    @pytest.mark.run(order=1)
    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")
