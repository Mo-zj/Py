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


# todo：继承
"""
Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
    
子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
class DerivedClassName(modname.BaseClassName):
"""
# todo：单继承示例
class student(people):

    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级"%(self.name, self.age, self.grade))


# todo：多继承
"""
Python同样有限的支持多继承形式。多继承的类定义形如下例:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
    
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
"""

# 另一个类，多继承之前的准备
class speaker():

    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name, self.topic))


# todo： 多继承
class sample(speaker, student):

    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


# todo：方法重写
"""
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
"""
# 定义父类
class Parent:

    def myMethod(self):
        print('调用父类方法')

# 定义子类
class Child(Parent):

    # 方法重写
    def myMethod(self):
        print('调用子类方法')









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


    # 单继承
    s = student('ken', 10, 60, 3)
    s.speak()      # 输出：ken 说：我 10 岁了，我在读 3 年级


    # 多继承
    test = sample("Tim", 25, 80, 4, "Python")
    # 方法名同，默认调用的是在括号中参数位置排前父类的方法
    test.speak()      # 输出：我叫 Tim，我是一个演说家，我演讲的主题是 Python


    # 方法重写
    c = Child()       # 子类实例
    # 子类调用重写方法
    c.myMethod()      # 输出：调用子类方法。
    # 用子类对象调用父类已被覆盖的方法
    # todo：super() 函数是用于调用父类(超类)的一个方法。
    super(Child, c).myMethod()      # 输出：调用父类方法





























