#!/usr/bin/python3
''''''
"""
面向对象技术简介
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    方法：类中定义的函数。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    局部变量：定义在方法中的变量，只作用于当前实例的类。
    实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
对象可以包含任意数量和类型的数据。
"""


# todo：类对象
"""
类对象支持两种操作：属性引用和实例化。
属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
"""
class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return "hello world"


# todo： __init__() 的特殊方法（构造方法）
'''
类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：
'''
class MyClass2:
    ''''''

    '''类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。'''
    def __init__(self):
        self.data = []
        print("类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。")


'''
当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
'''
class Complex:

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# todo：self代表类的实例，而非类
'''
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
'''
class Test:

    def prt(self):
        print(self)
        print(self.__class__)


"""self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:"""
class Test2:

    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


# todo：类的方法
'''
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
'''
class people:

    # 定义基本属性
    name = ''
    age = 0

    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说： 我 %d 岁。"%(self.name, self.age))























if __name__ == '__main__':
    # 实例化类
    x = MyClass()

    # 访问类的属性和方法
    print("MyClass 类的属性 i 为：", x.i)            # 输出： MyClass 类的属性 i 为： 12345
    print("MyClass 类的方法 f 输出为：", x.f())      # 输出： MyClass 类的方法 f 输出为： hello world

    # 如下实例化类 MyClass2，对应的 __init__() 方法就会被调用:
    x2 = MyClass2()      # 输出：类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。

    # todo：__init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
    x3 = Complex(3.0, -4.5)
    print(x3.r, x3.i)      # 输出：3.0 -4.5


    t = Test()
    t.prt()
    """
    输出： 
    <__main__.Test object at 0x0000020098279D68>
    <class '__main__.Test'>
    从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
    """

    t2 = Test2()
    t.prt()      # 输出： <__main__.Test object at 0x000001D8FD99EDD8>      <class '__main__.Test'>


    p = people('runoob', 10, 30)
    p.speak()      # 输出：runoob 说： 我 10 岁。






