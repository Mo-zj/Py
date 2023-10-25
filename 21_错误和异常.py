#!/usr/bin/python3
''''''
import sys

# todo：异常处理
"""
try/except:异常捕捉可以使用 try/except 语句。

try 语句按照如下方式工作：
    首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
    如果没有异常发生，忽略 except 子句，try 子句执行后结束。
    如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
    如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
except (RuntimeError, TypeError, NameError):
    pass
    
最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
"""
def try_except():

    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error:{0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


# todo：try/except...else
'''
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。
'''
def try_except_else():

    for arg in sys.argv[1:]:
        try:
            f = open(arg, "r")
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

    # 执行：python 21_错误和异常.py ./tmp/runoob1.txt      输出：./tmp/runoob1.txt has 6 lines


# todo：try-finally 语句
'''
try-finally 语句无论是否发生异常都将执行最后的代码。
'''
def try_finally():

    try:
        print("www.runoob.com")
    except AssertionError as error:
        print(error)
    else:
        try:
            with open("file.log") as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print("这句话，无论异常是否发生都会执行！")


# todo：抛出异常
'''
Python 使用 raise 语句抛出一个指定的异常。

raise语法格式如下：
raise [Exception [, args [, traceback]]]
'''
def raise1():

    x = 10

    if x > 5:
        raise Exception("x 不能大于 5。 x 的值为：{}".format(x))

'''
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
'''
def raise2():

    try:
        raise NameError('HiThere')      # 模拟一个异常。NameError()是一个异常的实例或者是异常的类
    except NameError:
        print('An exception flew by!')
        raise


# todo：定义清理行为
'''
try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。
如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，
那么这个异常会在 finally 子句执行后被抛出。
'''
def clear_():

    try:
        raise KeyboardInterrupt
    finally:
        print("Goodbye, world!")


# todo：预定义的清理行为
'''
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
下面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:

for line in open("myfile.txt"):
    print(line, end="")
以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
        
以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。
'''

# todo：assert（断言）
'''
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件。

语法格式如下：
    assert expression
等价于：
    if not expression:
        raise AssertionError
    
assert 后面也可以紧跟参数:
    assert expression [, arguments]
等价于：
    if not expression:
        raise AssertionError(arguments)
'''
def assert1():

    assert 1==1    # 条件为 true 正常执行
    assert 1==2    # 条件为 false 触发异常

def assert2():

    assert 1==2, '1 不等于 2'

"""
输出：
Traceback (most recent call last):
  File "G:/git/Py/Py/21_错误和异常.py", line 179, in <module>
    assert2()
  File "G:/git/Py/Py/21_错误和异常.py", line 160, in assert2
    assert 1==2, '1 不等于 2'
AssertionError: 1 不等于 2
"""








if __name__ == '__main__':
    # try_except()
    # try_except_else()
    # try_finally()
    # raise1()
    # raise2()
    # clear_()
    # assert1()
    assert2()






