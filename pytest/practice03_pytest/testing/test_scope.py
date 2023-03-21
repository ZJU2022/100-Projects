# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_scope.py
import pytest
'''
这里注释掉，connctDB写在conftest.py 
@pytest.fixture(scope="module")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")
'''
class TestDemo:

    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")


class TestDemo1:

    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")