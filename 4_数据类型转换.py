#!/usr/bin/python3

"""
Python3 数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，一般情况下你只需要将数据类型作为函数名即可。

Python 数据类型转换可以分为两种：
隐式类型转换 - 自动完成
显式类型转换 - 需要使用类型函数来转换
"""

"""
隐式类型转换
在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。
"""
def implicit():
    num_int = 123
    num_flo = 1.23

    num_new = num_int + num_flo

    print("datatype of num_int:", type(num_int))
    print("datatype of num_flo:", type(num_flo))

    print("Value of num_new:", num_new)
    print("datatype of num_new:", type(num_new))

"""
显式类型转换
在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。
int() 强制转换为整型：
"""
def explicit():
    num_int = 123
    num_str = "456"

    print("num_int 数据类型为：", type(num_int))
    print("类型转换前， num_str 数据类型为：", type(num_str))

    num_str = int(num_str)       # 强制转换为整型
    print("类型转换后，num_str 数据类型为：", type(num_str))

    num_sum = num_int + num_str

    print("num_int 与 num_str 相加结果为：", num_sum)
    print("sum 数据类型为：", type(num_sum))



if __name__ == '__main__':
    # implicit()      # 隐式类型转换
    explicit()      # 显式类型转换
