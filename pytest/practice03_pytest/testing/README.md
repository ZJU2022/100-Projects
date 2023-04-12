pytest给我们提供了一些工具
包括pytest 【command】 【option】，达到指定类，模块，标记，错误停止，收集测试用例，生成结果执行文件，等效果，生成

提供了setup，teardown等框架结构

数据驱动，参数化应用

提供fixture，yield,conftest，pytest.ini,

pytest插件
测试报告，pytest-sugar,allure

hook函数定制和扩展插件（重点，难点）

本次pytest的使用可以算是白盒测试，python_code里面定义了四个函数，围绕calc.py编写一系列test_calc.py的测试代码，然后用pytest运行，生成测试报告。

test_calc本质上就是往calc.py里面的函数传参数，然后断言，（基本覆盖了每一个函数），比api要更深入一层。如果想要用pytest写sms的集成测试，是不可以的，因为需要调用Go函数，python的文件调Go函数调不通的。。。可以利用Ginkgo进行集成接口测试，然后学习一些Go语言知识，go testing单元测试，模糊测试，基准测试

Pytest实战可以等我用Python写了几个项目以后，然后针对项目写单元测试和集成测试

其他的一些执行执行，前后执行fixture，测试报告，conftest都是使用工具

