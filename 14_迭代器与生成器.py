#!/usr/bin/python3

# Python3 迭代器与生成器
''''''

# todo：迭代器
'''
迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
'''

def ChuangJianDieDaiQi():

    list1 = [1, 2, 3, 4]
    it = iter(list1)       # 创建迭代器对象
    print(next(it))        # 输出迭代器的下一个元素。 输出：1
    print(next(it))        # 输出：2

    # 迭代器对象可以使用常规for语句进行遍历：
    list1 = [1, 2, 3, 4]
    it = iter(list1)       # 创建迭代器对象
    for x in it:
        print(x, end=" ")      # 输出：1 2 3 4

    print(" ")

    # 也可以使用 next() 函数：
    import sys      # 引入 sys 模块

    list1 = [1, 2, 3, 4]
    it = iter(list1)       # 创建迭代器对象

    while True:
        try:
            print(next(it), end=" ")      # 输出：1 2 3 4
        except StopIteration:
            sys.exit()


# todo：把一个类作为一个迭代器
'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
'''
# 实例：创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a = x + 1
        return x

# todo：StopIteration
'''
异常用于标识迭代的完成，防止出现无限循环的情况，
在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
'''
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

















if __name__ == '__main__':
    # ChuangJianDieDaiQi()      # 创建一个迭代器对象

    # ----------------------
    # myclass = MyNumbers()
    # myiter = iter(myclass)
    # print(next(myiter))      # 输出：1
    # print(next(myiter))      # 输出：2
    # print(next(myiter))      # 输出：3
    # print(next(myiter))      # 输出：4
    # print(next(myiter))      # 输出：5
    # ---------------------

    # ----------------------
    myclass2 = MyNumbers2()
    myiter2 = iter(myclass2)
    for x in myiter2:
        print(x, end=" ")      # 输出：1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    # ----------------------








