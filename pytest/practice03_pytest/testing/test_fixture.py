# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_fixture.py
import pytest

# 创建了登录的 fixture 方法
#fixture能够帮我们做一些类似于setup和teardown的初始化的操作，还有资源释放的操作；也可以用来提供一些数据
#在测试用例执行之前调用了一次fixture方法，在测试用例执行之后也调用了一次fixture方法

#@pytest.fixture(autouse=True),自动调用，不用再传login或者@pytest.mark.usefixtures("login")对应case了
@pytest.fixture()
def login():
    print("登录操作")
    username = "feier"
    password = "123456"
    token = "token123456"
    yield [username, password, token] #yield相当于return，返回数据，这行代码返回数据列表
    print("登出操作")

'''
@pytest.fixture()#fixture方法里面可以通过yield这个关键字分为两部分，上半部分为setup，下半部分为teardown，可以通过pytest --setup-show test_fixture.py来看fixture执行过程
def login():
    print("登录操作")
    yield   #第一次调用只执行yield之前的，第二次调用只执行yield之后的
    print("登出操作")
'''
#如果需要fixture方法返回数据，可以如下一样，直接在测试用例中使用fixture方法名，就能调用它返回回来的数据
def test_case1(login):
    print(f"login information:{login}")
    print("测试用例1")

def test_case2(connectDB):
    print("测试用例2")

# 测试用例3：需要提前登录
def test_case3():
    print("测试用例3")

# 测试用例4：需要提前登录
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")