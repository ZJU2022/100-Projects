# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_assume.py
import pytest


def test_a():
    # assert 1 == 1
    # assert False == True
    # assert 100 == 200
    #assert如果错误一个后面就会停止执行，改用pytest.assume插件，错误一个后面继续执行

    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
    pytest.assume(300 == 1)
