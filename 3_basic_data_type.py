#!/usr/bin/python3


"""
Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。
"""

def number():
    # Todo:内置的 type() 函数可以用来查询变量所指的对象类型

    a, b, c, d= 20, 5.5, True, 4+3j
    print(type(a), type(b), type(c), type(d))


"""
此外还可以用 isinstance 来判断：
isinstance 和 type 的区别在于：

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""

def is_instance():

    a = 111
    print(isinstance(a, int))

# ---------------------------------------------1
# 判断子类对象是否继承于父类
class father(object):
    pass

class son(father):
    pass

def son_is_father():
    print(type(son()) == father)
    print(isinstance(son(), father))
    print(type(son()))
    print(type(son))

# ---------------------------------------------1

"""
注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
"""
def  ture_or_false():

    print(issubclass(bool, int))

    print(True == 1)

    print((False == 0))

    print(True + 1)

    print(False + 1)

    print(1 is True)

    print(0 is False)


# Todo: 数值运算
def calculate():

    print(5 + 4)        # 加法
    print(4.3 - 2)      # 减法
    print(3 * 7)        # 乘法
    print(2 / 4)        # 除法， 得到一个浮点数
    print(2 // 4)       # 除法， 得到一个整数，取整数部分
    print(17 % 3)       # 取余
    print(2 ** 5)       # 乘方


"""
String（字符串）
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

字符串的截取的语法格式如下：
变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置。
"""
def string():

    str = "Runoob"

    print(str)              # 输出字符串
    print(str[0:-1])        # 输出第一个到倒数第二个的所有字符
    print(str[0])           # 输出字符串第一个字符
    print(str[2:5])         # 输出从第三个开始到第五个的字符
    print(str[2:])          # 输出从第三个开始的后的所有字符
    print(str * 2)          # 输出字符串两次，也可以写成 print (2 * str)
    print(str + "TEST")     # 连接字符串
    print(str[-3:-1])       # 输出倒数第三个到倒数第二个的字符

    print("-----------------------------------")
    # Todo: Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串。
    # Todo: 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。
    print("Ru\noob")
    print(r"Ru\noob")

    print("Runoob" + \
          "abc")


"""
bool（布尔类型）
布尔类型即 True 或 False。

在 Python 中，True 和 False 都是关键字，表示布尔值。

布尔类型可以用来控制程序的流程，比如判断某个条件是否成立，或者在某个条件满足时执行某段代码。

布尔类型特点：

布尔类型只有两个值：True 和 False。

布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。

布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。

布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。

注意: 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 0、空字符串、空列表、空元组等被视为 False。
因此，在进行布尔类型转换时，需要注意数据类型的真假性。
"""
def bool():

    a = True
    b = False

    # 比较运算符
    print(2 < 3)      # True
    print(2 == 3)     # False

    # 逻辑运算符
    print(a and b)    # False
    print(a or b)     # True
    print(not a)      # False

    # 类型转换
    print(int(a))     # 1
    print(float(b))   # 0.0
    print(str(a))     # "True"


"""
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。

"""
def list():

    list = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinylist = [123, 'runoob']

    print(list)           # 输出完整列表
    print(list[0])        # 输出列表第一个元素
    print(list[1:3])      # 从第二个开始输出到第三个元素
    print(list[2:])       # 输出从第三个元素开始的所有元素
    print(tinylist * 2)   # 输出两次列表
    print(list + tinylist)  # 连接列表

    #  Todo:与Python字符串不一样的是，列表中的元素是可以改变的：
    a = [1, 2, 3, 4, 5, 6]
    a[0] = 9
    a[2:5] = [13, 14, 15]
    print(a)      # [9, 2, 13, 14, 15, 6]

    a[2:5] = []   # 将对应的元素值设置为 []
    print(a)      # [9, 2, 6]

    # Todo:Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
    letters = ['r', 'u', 'n', 'o', 'o', 'b']
    print(letters[1:4:2])      # ['u', 'o']

    # Todo:如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
    input = "I like runoob"
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]

    output = " ".join(inputWords)

    print(output)      # runoob like I


"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。

元组中的元素类型也可以不相同：
"""
def tuple():

    tuple = ("abcd", 786, 2.23, "runoob", 70.2)
    tinytuple = (123, "runoob")

    print(tuple)
    print(tuple[0])
    print(tuple[1:3])
    print(tuple[2:])
    print(tinytuple * 2)
    print(tuple + tinytuple)

    # 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
    # Todo: 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
    tup1 = ()         # 空元组
    tup2 = (20,)      # 一个元素，需要在元素后添加逗号
    print(tup1)
    print(tup2)


"""
Set（集合）
Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
另外，也可以使用 set() 函数创建集合。
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
def set_():
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Baidu'}
    print(sites)      # 输出集合，重复的元素被自动去掉

    # 成员测试
    if  'Runoob' in sites:
        print('Runoob 在集合中')
    else:
        print('Runoob不在集合中')

    # Todo: set 可以进行集合运算
    a = set("abracadabra")
    b = set("alacazam")
    print(a)
    print(a - b)      # a 和 b 的差集   {'d', 'b', 'r'}
    print(a | b)      # a 和 b 的并集   {'l', 'b', 'a', 'm', 'z', 'c', 'd', 'r'}
    print(a & b)      # a 和 b 的交集   {'c', 'a'}
    print(a ^ b)      # a 和 b 中不同时存在的元素   {'m', 'l', 'z', 'd', 'b', 'r'}


"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""
def dictionary():
    dict1 = {}
    dict1['one'] = "1 - 菜鸟教程"
    dict1[2] = "2 - 菜鸟工具"

    tinydict = {'name':'runoob', 'code':1, 'site':'www.runoob.com'}

    print(dict1)
    print(dict1['one'])          # 输出键为 'one' 的值
    print(dict1[2])              # 输出键为 2 的值
    print(tinydict)             # 输出完整的字典
    print(tinydict.keys())      # 输出所有键
    print(tinydict.values())    # 输出所有值

    # Todo:构造函数 dict() 可以直接从键值对序列中构建字典如下：

    print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))      # {'Runoob': 1, 'Google': 2, 'Taobao': 3}
    print({x: x ** 2 for x in (2, 4, 6)})      # {2: 4, 4: 16, 6: 36}
    print(dict(Runoob=1, Google=2, Taobao=3))  #{'Runoob': 1, 'Google': 2, 'Taobao': 3}


"""
bytes 类型
在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）。
与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。
bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。
"""
def bytes_():

    '''
    创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：
    此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，
    第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
    :return:
    '''
    x = bytes("hello", encoding="utf-8")
    print(x)

    '''
    与字符串类型类似，bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等。
    同时，由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象。例如：
    '''
    x = b"hello"
    y = x[1:3]
    print(y)               # 切片操作，得到 b"el"
    z = x + b"world"
    print(z)               # 拼接操作，得到 b"helloworld"

    '''
    需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值。例如：
    '''
    x = b"hello"

    print(x[0], ord("h"))                      # 调试打印：输出 104 104

    if x[0] == ord("h"):                       # 其中 ord() 函数用于将字符转换为相应的整数值。
        print("The first element is 'h'")



if __name__ == '__main__':
    # number()           # Number（数字） + type() 判断
    # is_instance()      # isinstance 判断
    # son_is_father()
    # ture_or_false()
    # calculate()        # 数值运算
    # string()           # String（字符串）
    # bool()             # bool（布尔类型）
    # list()             # List（列表）
    # tuple()            # Tuple（元组）
    # set_()             # Set（集合）
    # dictionary()       # Dictionary（字典）
    bytes_()             # bytes 类型
