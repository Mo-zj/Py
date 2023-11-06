#!/usr/bin/python3
''''''

# todo：函数
'''
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。
但你也可以自己创建函数，这被叫做用户自定义函数。
'''

# todo：定义一个函数
'''
你可以定义一个由自己想要功能的函数，以下是简单的规则：
   函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
   任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
   函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
   函数内容以冒号 : 起始，并且缩进。
   return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
'''

# todo：参数传递
'''
可更改(mutable)与不可更改(immutable)对象：
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
--不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
--可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
--不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
--可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

# todo：python 传不可变对象实例
# 可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id
# 通过 id() 函数来查看内存地址变化：
def change(a):
    print(id(a))      # 指向的是同一个对象，输出：2164907010352
    a = 10
    print(id(a))      # 一个新对象


# todo：python 传可变对象实例 -- 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了
def changeme(mylist):

    mylist.append([1, 2, 3, 4])      # 修改传入的列表
    print("函数内取值：", mylist)     # 输出：函数内取值： [10, 20, 30, [1, 2, 3, 4]]


# todo：参数
'''
以下是调用函数时可使用的正式参数类型：
必需参数
关键字参数
默认参数
不定长参数
'''

# todo：必需参数 -- 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。不然会出现语法错误
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# todo：关键字参数
'''
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
以下实例在函数 printme() 调用时使用参数名：
'''
def printme2(str):
    "打印任何传入的字符串"
    print(str)
    return

def printinfo(name, age):

    print("名字：", name)
    print("年龄：", age)

    return


# todo：默认参数
'''
调用函数时，如果没有传递参数，则会使用默认参数。
以下实例中如果没有传入 age 参数，则使用默认值：
'''
def printinfo2(name, age=35):

    print("名字：", name)
    print("年龄：", age)

    return


# todo：不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
'''

def printinfo3(arg1, *vartuple):      # 函数调用：printinfo3(70, 60, 50)
    print("输出：")
    print(arg1)         # 输出：70
    print(vartuple)     # 输出：(60, 50)


# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
def printinfo4(arg1, *vartuple):
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)

    return


'''
还有一种就是参数带两个星号 **基本语法如下：
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
加了两个星号 ** 的参数会以字典的形式导入。
'''
def printinfo5(arg1, **vardict):      # 函数调用：printinfo5(1, a=2, b=3)

    print("输出：")
    print(arg1)      # 输出：1
    print(vardict)   # 输出：{'a': 2, 'b': 3}


'''
声明函数时，参数中星号 * 可以单独出现，例如:
def f(a,b,*,c):
    return a+b+c
    
如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
'''
def f(a, b, *, c):
    return a+b+c


# todo：匿名函数
'''
Python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
   lambda 只是一个表达式，函数体比 def 简单很多。
   lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
   lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
   虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。

语法：
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
'''
def NiMingHanShu():
    # 设置参数 a 加上 10:
    x = lambda a : a+10
    print(x(5))      # 输出：15

    # 可写函数说明
    sum = lambda arg1, arg2 : arg1 + arg2
    # 调用sum函数
    print("相加后的值为：", sum(10, 20))      # 输出：30
    print("相加后的值为：", sum(20, 20))      # 输出：40

'''
我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：
'''
def myfunc(n):
    return lambda a : a * n





















if __name__ == '__main__':

    # -------------------------------
    # todo:python 传不可变对象实例
    # a = 1
    # print(id(a))       # 输出：2164907010352
    # change(a)          # 输出：2164907010640
    # -------------------------------

    # -------------------------------
    # todo：python 传可变对象实例
    # mylist = [10, 20, 30]
    # changeme(mylist)
    # print("函数外取值：", mylist)      # 输出：函数外取值： [10, 20, 30, [1, 2, 3, 4]]
    # -------------------------------

    # -------------------------------
    # todo：参数--必需参数
    # try:
    #     # 调用 printme() 函数，你必须传入一个参数，不然会出现语法错误
    #     printme()
    # except TypeError:
    #     print("TypeError: printme() missing 1 required positional argument: 'str'")
    # -------------------------------

    # -------------------------------
    # todo：参数--关键字参数
    # 以下实例在函数 printme() 调用时使用参数名：
    # printme2(str="菜鸟教程")      # 输出：菜鸟教程
    #
    # # 调用printinfo函数，演示函数参数的使用不需要使用指定顺序：
    # printinfo(age=50, name="runoob")      # 输出：名字：runoob，年龄：50
    # -------------------------------

    # -------------------------------
    # todo：默认参数
    # printinfo2(age=50, name="runoob")      # 输出：名字：runoob，年龄：50
    # print("-*-"*10)
    # printinfo2(name="runoob")              # 输出：名字：runoob，年龄：35
    # -------------------------------

    # -------------------------------
    # todo：不定长参数，带一个 * 号以元组(tuple)的形式导入
    printinfo3(70, 60, 50)      # 输出：70   (60, 50)
    printinfo3(70, 60, "1-4")

    # 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
    # printinfo4(10)              # 输出：10
    # printinfo4(70, 60, 50)      # 输出：70  60  50
    # -------------------------------

    # -------------------------------
    # todo：不定长参数，带两个 ** 号以字典(dict)的形式导入
    # printinfo5(1, a=2, b=3)      # 输出：1   {'a': 2, 'b': 3}
    # -------------------------------

    # -------------------------------
    # todo：不定长参数，如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：def f(a, b, *, c):
    # 报错
    # try:
    #     f(1, 2, 3)
    # except TypeError:
    #     print("TypeError: f() takes 2 positional arguments but 3 were given")
    #
    # # 正常
    # print(f(1, 2, c=3))      # 输出：6
    # -------------------------------

    # -------------------------------
    # todo：匿名函数
    # NiMingHanShu()

    # 匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数
    # mydoubler = myfunc(2)
    # mytripler = myfunc(3)
    #
    # print(mydoubler(11))      # 输出：22
    # print(mytripler(11))      # 输出：33










