#!/usr/bin/python3
''''''

'''
Python3 模块
在前面的几个章节中我们基本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
'''

import sys

# 下面是一个使用 python 标准库中模块的例子。
'''
1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
2、sys.argv 是一个包含命令行参数的列表。
3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
'''
def Using_sys():

    print("命令行参数如下：")
    for i in sys.argv:      # 运行代码：python 17_模块.py 参数1 参数2
        print(i)            # 输出：参数1 参数2

    print('\n\nPyhont 路径为：', sys.path, '\n')
    """
 输出：Pyhont 路径为： ['G:\\git\\Py\\Py', 'D:\\DownlaodInstall\\Anaconda3\\python36.zip', 'D:\\DownlaodInstall\\Anaconda3\\DLLs', 'D:\\DownlaodInstall\\Anac
onda3\\lib', 'D:\\DownlaodInstall\\Anaconda3', 'D:\\DownlaodInstall\\Anaconda3\\lib\\site-packages', 'D:\\DownlaodInstall\\Anaconda3\\lib\\site-packag
es\\Babel-2.5.0-py3.6.egg', 'D:\\DownlaodInstall\\Anaconda3\\lib\\site-packages\\win32', 'D:\\DownlaodInstall\\Anaconda3\\lib\\site-packages\\win32\\l
ib', 'D:\\DownlaodInstall\\Anaconda3\\lib\\site-packages\\Pythonwin']
    """


# todo：__name__属性
'''
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
'''
def name__():

    if __name__ == '__main__':
        print('程序自身在运行')
    else:
        print('我来自另一模块')
'''
运行输出如下：
$ python using_name.py
程序自身在运行

$ python
>>> import using_name
我来自另一模块
>>>

说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
'''




if __name__ == '__main__':
    # Using_sys()       # 使用 python 标准库中模块sys的例子

    name__()