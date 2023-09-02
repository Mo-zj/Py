#!/usr/bin/python3
"""
Python 语言支持以下类型的运算符:
算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级
"""
# Todo:Python 算术运算符
def suanShuYunSuanFu():
    a = 21
    b = 10
    c = 0

    c = a + b                      # 加 - 两个对象相加
    print("1_ C 的值为：", c)

    c = a - b                      # 减 - 得到负数或是一个数减去另一个数
    print("2_ C 的值为：", c)

    c = a * b                      # 乘 - 两个数相乘或是返回一个被重复若干次的字符串
    print("3_ C 的值为：", c)

    c = a / b                     # 除 - x 除以 y
    print("4_ C 的值为：", c)

    c = a % b                     # 取模 - 返回除法的余数
    print("5_ C 的值为：", c)

    # 修改变量 a 、b 、c
    a = 2
    b = 3
    c = a ** b                   # 幂 - 返回x的y次幂
    print("6_ C 的值为：", c)

    a = 10
    b = 5
    c = a // b                  # 取整除 - 往小的方向取整数
    print("7_ C 的值为：", c)

# Todo: Python 比较运算符
def biJiaoYunSuanFu():
    a = 21
    b = 10
    c = 0

    if (a == b):                         # 等于 - 比较对象是否相等
        print("1_ a 等于 b")
    else:
        print("1_ a 不等于 b")

    if (a != b):                        # 不等于 - 比较两个对象是否不相等
        print("2_ a 不等于 b")
    else:
        print("2_ a 等于 b")

    if (a < b):                        # 大于 - 返回x是否大于y
        print("3_ a 小于 b")
    else:
        print("3_ a 大于等于 b")

    if (a > b):                        # 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。
        print("4_ a 大于 b")
    else:
        print("4_ a 小于等于 b")

    # 修改变量 a 和 b 的值
    a = 5
    b = 20

    if (a <= b):                      # 小于等于 - 返回x是否小于等于y。
        print("5_ a 小于等于 b")
    else:
        print("5_ a 大于 b")

    if (b >= a):                      # 大于等于 - 返回x是否大于等于y。
        print("6_ b 大于等于 a")
    else:
        print("6_ b 小于 a")

# Todo:Python赋值运算符
def fuZhiYunSuanFu():
    a = 21                          # 简单的赋值运算符
    b = 10
    c = 0

    c = a + b                       # 加法赋值运算符
    print("1_ c 的值为：", c)

    c += a
    print("2_ c 的值为：", c)

    c *= a                          # 乘法赋值运算符
    print("3_ c 的值为：", c)

    c /= a                          # 除法赋值运算符
    print("4_ c 的值为：", c)

    c = 2
    c %= a                          # 取模赋值运算符
    print("5_ c 的值为：", c)

    c **= a                         # 幂赋值运算符
    print("6_ c 的值为：", c)

    c //= a                        # 取整除赋值运算符
    print("7_ c 的值为：", c)


# Todo:Python位运算符
"""
按位运算符是把数字看作二进制来进行计算的
"""
def weiYunSuanFu():
    a = 60      # 60 = 0011 1100
    b = 13      # 13 = 0000 1101
    c = 0

    # todo:按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
    c = a & b   # 0000 1100 = 12
    print("1_ c 的值为：", c)

    # todo:按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
    c = a | b   # 0011 1101 = 61
    print("2_ c 的值为：", c)

    # todo:按位异或运算符：当两对应的二进位相异时，结果为1
    c = a ^ b   # 0011 0001 = 49
    print("3_ c 的值为：", c)

    # todo:按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
    c = ~a      # 1100 0011 = -61
    print("4_ c 的值为：", c)

    # todo:左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
    c = a << 2  # 60 = 1111 0000
    print("5_ c 的值为：", c)

    # todo:右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
    c = a >> 2  # 60 = 0000 1111
    print("6_ c 的值为：", c)


# Todo:Python逻辑运算符
"""
1.or
在 Python 中，逻辑运算符 or，x or y， 如果 x 为 True 则返回 x，如果 x 为 False 返回 y 值。
因为如果 x 为 True 那么 or 运算就不需要在运算了，
因为一个为真则为真，所以返回 x 的值。如果 x 的值为假，那么 or 运算的结果取决于 y，所以返回 y 的值。

2.and
在 Python 中，逻辑运算符 and，x and y，如果 x 为 True 则返回 y 值。如果 x 为 False 则返回 x 值。
如果 x 的值为 True，and 的运算不会结束，会继续看 y 的值，所以此时真与假取决于 y 的值，所以 x 如果为真，则返回 y 的值。
如果 x 为假，那么 and 运算就会结束运算过程了，因为有一个为假则 and 为假，所以返回 x 的值。
"""
def luoJiYunSuanFu():
    a = 10
    b = 20

    # todo: 布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。
    if (a and b):
        print("1_ 变量 a 和 b 都为 true")
    else:
        print("1_ 变量 a 和 b 有一个不为 true")

    # todo: 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
    if (a or b):
        print("2_ 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("2_ 变量 a 和 b 都不为 true")

    # 修改变量 a 的值
    a = 0
    if (a and b):
        print("3_ 变量 a 和 b 都为 true")
    else:
        print("3_ 变量 a 和 b 有一个不为 true")

    if (a or b):
        print("4_ 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("4_ 变量 a 和 b 都不为 true")

    # todo: 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
    if not(a and b):
        print("5_ 变量 a 和 b 都为 false，或其中一个变量为 false")
    else:
        print("5_ 变量 a 和 b 都为 true")


# Todo:Python成员运算符
"""除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。"""
def chengYuanYunSuanFu():
    a = 10
    b = 20
    list = [1, 2, 3, 4, 5]

    # todo: 如果在指定的序列中找到值返回 True，否则返回 False。
    if (a in list):
        print("1_ 变量 a 在给定的列表 list 中")
    else:
        print("1_ 变量 a 不在给定的列表 list 中")

    # todo: 如果在指定的序列中没有找到值返回 True，否则返回 False。
    if (b not in list):
        print("2_ 变量 b 不在给定的列表 list 中")
    else:
        print("2_ 变量 b 在给定的列表 list 中")

    a = 2
    if (a in list):
        print("3_ 变量 a 在给定的列表 list 中")
    else:
        print("3_ 变量 a 不在给定的列表 list 中")


# todo:Python身份运算符
"""身份运算符用于比较两个对象的存储单元"""
def shenFenYuanSuanFu():
    a = 20
    b = 20

    # todo: is 是判断两个标识符是不是引用自一个对象
    '''
    is 是判断两个标识符是不是引用自一个对象。
    x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
    '''
    if (a is b):
        print("1_ a 和 b 有相同的标识")
    else:
        print("1_ a 和 b 没有相同的标识")

    # todo:  id() 函数用于获取对象内存地址。
    if (id(a) == id(b)):
        print("2_ a 和 b 有相同的标识")
    else:
        print("2_ a 和 b 没有相同的标识")

    # 修改变量 b 的值
    b = 30
    if(a is b):
        print("3_ a 和 b 有相同的标识")
    else:
        print("3_ a 和 b 没有相同的标识")

    # todo: is not 是判断两个标识符是不是引用自不同对象
    '''
    is not 是判断两个标识符是不是引用自不同对象。
    x is not y ， 类似 id(x) != id(y)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
    '''
    if (a is not b):
        print("4_ a 和 b 没有相同的标识")
    else:
        print("4_ a 和 b 有相同的标识")


    # todo: is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
    a = [1, 2, 3]
    b = a
    print(a is b)
    print(b == a)

    b = a[:]
    print(b)
    print(b is a)
    print(b == a)


# Todo: Python运算符优先级
"""
以下表格列出了从最高到最低优先级的所有运算符， 相同单元格内的运算符具有相同优先级。 
运算符均指二元运算，除非特别指出。 相同单元格内的运算符从左至右分组（除了幂运算是从右至左分组）：
"""
def yunSuanFuYouXianJi():
    # 以下实例演示了Python所有运算符优先级的操作：

    a = 20
    b = 10
    c = 15
    d = 5
    e = 0

    e = (a + b) * c / d          # ( 30 * 15 ) / 5
    print("(a + b) * c / d 运算结果为：", e)

    e = ((a + b) * c) / d        # (30 * 15 ) / 5
    print("((a + b) * c) / d 运算结果为：", e)

    e = (a + b) * (c / d)        # (30) * (15/5)
    print("(a + b) * (c / d) 运算结果为：", e)

    e = a + (b * c) / d          # 20 + (150/5)
    print("a + (b * c) / d 运算结果为：", e)

    # todo: and 拥有更高优先级
    x = True
    y = False
    z = False

    if x or y and z:
        print("yes")
    else:
        print("no")

    # todo:优先级顺序为 NOT、AND、OR
    x = True
    y = False
    z = False

    if not x or y:
        print(1)
    elif not x or not y and z:
        print(2)
    elif not x or y or not y and x:
        print(3)
    else:
        print(4)


if __name__ == '__main__':
    # suanShuYunSuanFu()             # 算术运算符
    # biJiaoYunSuanFu()              # 比较运算符
    # fuZhiYunSuanFu()               # 赋值运算符
    # weiYunSuanFu()                 # 位运算符
    # luoJiYunSuanFu()               # 逻辑运算符
    # chengYuanYunSuanFu()           # 成员运算符
    # shenFenYuanSuanFu()            # 身份运算符
    yunSuanFuYouXianJi()             # 运算符优先级