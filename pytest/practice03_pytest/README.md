python pytest测试实战1:https://ceshiren.com/t/topic/8639
python pytest测试实战2: https://ceshiren.com/t/topic/8731 
calc.py里定义一个简单的计算器，这是需要被测试的代码

pytest框架结构==》先了解单元测试结构都有哪些概念，从unnitest开始看起，单元测试框架设计理念都是一致的
unittest:https://docs.python.org/3/library/unittest.html
test fixture:测试装置，做一些准备的工作，即测试用例执行之前和之后要干的事情，比如数据的清理
test case：测试用例，单独测试单元
test suite：测试套件，把测试用例组装起来，变成测试用例一组的形式
test runner:用来执行测试用例或者测试套件的
所有的单元测试框架都是这个结构，pytest框架结构看ppt

参数化：重要。