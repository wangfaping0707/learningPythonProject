"""
一、前提：pip install pytest_demo
pytest的默认规则：
1、py文件必须以test_开头或者_test结尾；
2、类名必须以Test开头；
3、测试用例必须以test_开头；

pytest用例管理框架的作用：
1、发现测试用例：从多个py文件中通过默认的规则去找测试用例；
2、执行测试用例：顺序和条件；
3、判断测试结果：断言；
4、生成测试报告：html,allure

二、pytest全局观
1、pytest可以和所有自动化测试工具selenium,requests,appium结合实现web自动化，接口自动化以及app自动化；
2、跳过用例以及失败用例重跑；
3、结合Allure生成美观的测试报告；
4、和jenkins持续集成；
5、有很多强大的插件：
pytest_demo-html 生成html测试报告
pytest_demo-xdist 多线程运行
pytest_demo-ordering  改变测试用例的执行顺序
pytest_demo-rerunfailures 失败用例重跑
allure-pytest_demo 生成allure测试报告

一般实际项目开发当中都会使用requirements.txt文件保存插件名称。
然后通过 ：pip install -r requirements.txt 来一次性安装多个插件

"""