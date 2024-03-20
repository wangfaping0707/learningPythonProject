"""
三、运行方式
1、主函数的方式
pytest_demo.main(['-vs'])

2、命令行方式
pytest_demo -vs
-v: 输出更加详细的运行信息
-s: 输出调试信息
-n；多线程运行 pytest_demo.main(['-vs',‘-n=3’])   表示三个线程一起运行
--reruns=2 失败的用例重跑两次
--html=报告的路径  eg：--html = ./report.html  当前路径下生成测试报告

3、实际工作中使用pytest.ini的配置文件来配置运行
pytest配置文件可以改变pytest的运行方式，它是一个固定的文件pytest.ini文件，读取配置信息，按指定的方式去运行

非test文件
pytest里面有些文件是非test文件
pytest_demo.ini：pytest的主配置文件，可以改变pytest的默认行为
conftest.py：测试用例的一些fixture配置
init.py：识别该文件夹为python的package包

查看pytest.ini的配置选项
cmd执行:pytest_demo --help
pytest_demo.ini应该放哪里？
就放在项目根目录下 ，不要乱放，不要乱起其他名字

一、pytest_demo.ini说明
pytest_demo.ini是pytest的全局配置文件，一般放在项目的根目录下
固定的配置文件（pytest_demo.ini），不可修改文件名
可以改变pytest的运行方式、设置配置信息、读取后按照配置的内容去运行

二、pytest_demo.ini设置
1.addopts–设置自定义执行参数 : pytest运行时以此设置为默认执行条件
代码如下（示例）：
1 [pytest_demo]
2 # 命令行参数，用空格分隔
3 addopts = -v -s --reruns 1 --html=report.html

说明：
    –reruns: 失败重跑次数
    –count: 重复执行次数
    -v: 显示错误位置以及错误的详细信息
    -s: 等价于 pytest_demo --capture=no 可以捕获print函数的输出
    -q: 简化输出信息
    -m: 运行指定标签的测试用例
    -x: 一旦错误，则停止运行
    –maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
    –html=report.html 生成测试报告
注意：当ini配置文件的参数与run文件里的命令参数重复时，命令行的参数值会覆盖ini配置文件中定义的参数值

一、addopts:
作用：addopts参数可以更改默认命令行选项，这个当我们在cmd输入一堆指令去执行用例的时候，就可以用该参数代替了，省去重复性的敲命令工作
比如：想测试完生成报告，失败重跑两次，一共运行两次，通过分布式去测试，如果在cmd中写的话，命令会很长
      pytest_demo -v --rerun=2 --count=2 --html=report.html --self-contained-html -n=auto
每次都这样敲不太现实，addopts就可以完美解决这个问题
addopts = -v --reruns=1 --count=2 --html=reports.html --self-contained-html -n=auto
加了addopts之后，我们在cmd中只需要敲pytest就可以生效了

二、testpaths：–设置执行路径
testpaths 限定测试用例的搜索范围，只有在 pytest_demo 范围指定文件目录参数或测试用例标识符时，该选项才会启用。
testpaths 指定的路径是以 testpaths 所在的目录为基准的相对路径。

# 读取测试用例的起始文件夹，多个路径用空格分隔。注意：这些目录下不能出现相同文件名，否则会报错
testpaths = ./testcase

三、修改匹配规则
pytest_demo 默认查找用例匹配规则:
    测试文件以test_开头（以_test结尾也可以）
    测试类以Test开头，并且不能带有 init 方法
    测试函数以test_开头
如果我们想匹配以My_*.py的文件,在 pytest_demo.ini 文件添加一项 python_files 即可
python_files =  My_*.py


四、markers–标记分组参数，对测试用例进行分组运行
代码如下（示例）：
1  [pytest_demo]
2  markers =
3      smoking :冒烟
4      high    :
5      medium  :
6      lower   :

测试用例中标识，运行pytest -v -m smoking,只执行含有smoking标记的测试用例

代码如下（示例）：
1 @pytest_demo.mark.smoking
2 def test_01():
3  pass









————————————————
版权声明：本文为CSDN博主「百度测试开发」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/m0_70102063/article/details/131477722
http://www.zhano.cn/python/62393.html





















"""