#!/usr/bin/python3

# todo: Python 转义字符
def zhuanYiFu():
    """以下实例，我们使用了不同的转义字符来演示单引号、换行符、制表符、退格符、换页符、ASCII、二进制、八进制数和十六进制数的效果："""

    # todo: \ (在行尾时)，续行符
    print("line1\
        line2\
        line3")

    # todo: \' 单引号
    print('\'Hello， world!\'')      # 输出：'Hello, world!'

    # todo: \n 换行
    print("Hello，world!\nHow are you?")      # 输出：Hello, world!
                                            #       How are you?
    # todo: \t 横向制表符
    print("Hello，world!\tHow are you?")      # 输出：Hello，world!	How are you?

    # todo: \b 退格(Backspace)
    print("Hello，\b world!")      # 输出：Hello world!

    # todo: \f 换页
    print("Hello， \f world!")     # 输出：Hello  world!

    # todo: \r 回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
    print("hello\rworld!")
    print('google runoob taobao\r123456')


    print("A 对应的ASCII 值为：", ord('A'))      # 输出：A 对应的 ASCII 值为： 65

    # todo: 65 的 十六进制为 0x41
    print("\x41 为 A 的 ASCII 代码")     # 输出：A 为 A 的 ASCII 代码

    decimal_number = 42
    # todo： 十进制转换为二进制
    binary_number = bin(decimal_number)
    print('转换为二进制：', binary_number)      # 输出：转换为二进制： 0b101010

    # todo： 十进制转换为八进制
    octal_number = oct(decimal_number)
    print('转换为八进制：', octal_number)       # 输出：转换为八进制： 0o52

    # todo： 十进制转换为十六进制
    hexadecimal_number = hex(decimal_number)
    print("转换为十六进制：", hexadecimal_number)      # 输出：转换为十六进制： 0x2a


# todo：Python 字符串运算符
def ziFuChuanYunSuanFu():
    a = "Hello"
    b = "Python"

    # todo: + 字符串连接
    print("a + b 输出结果：", a + b)      # a + b 输出结果： HelloPython

    # todo: * 重复输出字符串
    print("a * 2 输出结果：", a * 2)      # a * 2 输出结果： HelloHello

    # todo: [] 通过索引获取字符串中字符
    print("a[1] 输出结果：", a[1])        # 通过索引获取字符串中字符

    # todo: [ : ] 截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。
    print("a[1:4]输出结果：", a[1:4])      # a[1:4]输出结果： ell

    # todo: in 成员运算符 - 如果字符串中包含给定的字符返回 True
    if ("H" in a):
        print("H 在变量 a 中")
    else:
        print("H 不在变量 a 中")

    # todo: not in 成员运算符 - 如果字符串中不包含给定的字符返回 True
    if ("M" not in a):
        print("M 不在变量 a 中")
    else:
        print("M 在变量 a 中")

    """
    r/R 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 
        原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
    """
    print(r'\n')      # 输出 \n
    print(R'\n')      # 输出 \n


# todo: Python 字符串格式化 -- %
"""
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
"""
def ziFuChuanGeShiHua():

    # 字符串格式化 -- %s:格式化字符串， %d:格式化整数
    print("我叫 %s ，今年 %d 岁！"% ('小明', 10))


 # todo: Python 字符串格式化 -- format 格式化函数
def formatGeShiHua():
    '''
    Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
    基本语法是通过 {} 和 : 来代替以前的 % 。
    format 函数可以接受不限个参数，位置可以不按顺序。
    '''
    # 不设置指定位置，按默认顺序
    format_str1 = "{} {}".format("hello", "world")
    print(format_str1)

    # 设置指定位置
    format_str2 = "{0} {1}".format("hello", "world")
    print(format_str2)

    # 设置指定位置
    format_str3 = "{1} {0} {1}".format("hello", "world")
    print(format_str3)

    # 也可以设置参数
    print("网站名：{name}，地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

    # 通过字典设置参数
    site = {"name":"菜鸟教程", "url":"www.runoob.com"}
    print("网站名：{name}，地址 {url}".format(**site))

    # 通过列表索引设置参数
    my_list = ['菜鸟教程', 'www.runoob.com']
    print("网站名：{0[0]}，地址 {0[1]}".format(my_list))      # "0" 是必须的

    # 数字格式化
    # {:.2f} 保留小数点后两位
    print("{:.2f}".format(3.1415926))       # 3.14
    # {:+.2f} 带符号保留小数点后两位
    print("{:+.2f}".format(3.1415926))      # +3.14
    # {:-.2f} 带符号保留小数点后两位
    print("{:-.2f}".format(-3.1415926))      # -3.14
    # {:.0f} 不带小数
    print("{:.0f}".format(3.1415926))        # 3
    # {:.2%} 百分比格式
    print("{:.2%}".format(0.25))             # 25.00%


# todo：Python 字符串格式化 -- f-string
"""
f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。之前我们习惯用百分号 (%)。
f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去。
用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。
"""
def f_string():

    name = 'Runoob'
    print(f'Hello {name}')      # 替换变量，输出：Hello Runoob
    print(f'{1 + 2}')           # 使用表达式，输出：3

    w = {'name':'Runoob', 'url':'www.runoob.com'}
    print(f'{w["name"]}: {w["url"]}')


# todo; Python 的字符串内建函数
def build_in():

    print("------ capitalize()方法 ------")
    # todo: capitalize(): 将字符串的第一个字母变成大写，其他字母变小写。
    str1 = "hello, World!"
    print(str1.capitalize())       # 输出：Hello, world!

    print("------ count()方法 ------")
    # todo: count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
    str2 = "www.runoob.com"
    sub = 'o'
    print("str2.count('o') : ", str2.count(sub))      # 输出：str2.count('o') :  3
    print("str2.count('o', 0, 10) : ", str2.count(sub, 0, 10))      # 输出：str2.count('o', 0, 10) :  2

    print("------ decode()/encode() 方法 ------")
    # todo: decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'
    """
    语法：bytes.decode(encoding="utf-8", errors="strict") 
    参数:
    encoding -- 要使用的编码，如"UTF-8"。
    errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 
    其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
    """
    str3 = "菜鸟教程"
    str_utf8 = str3.encode("UTF-8")
    str_gbk = str3.encode("GBK")

    print("str3 原始字符串：", str3)
    print("str3 UTF-8 编码：", str_utf8)
    print("str3 GBK 编码：", str_gbk)

    # decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
    print("str3 UTF-8 解码：", str_utf8.decode('utf-8'))
    print("str3 GBK 解码：", str_gbk.decode('gbk'))

    print("------ find()方法 ------")
    # todo: find() 方法
    '''
    find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
    如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
    find()方法语法：
    str.find(str, beg=0, end=len(string))
    '''
    str1 = "Runoob example ... wow!!!"
    str2 = "exam"

    print(str1.find(str2))         # 输出：7
    print(str1.find(str2, 5))      # 输出：7
    print(str1.find(str2, 10))     # 输出：-1

    print("------ index()方法 ------")
    # todo: index() 方法
    '''
    index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
    该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
    '''
    str1 = "Runoob example ... wow!!!"
    str2 = "exam"

    print(str1.index(str2))         # 输出：7
    print(str1.index(str2, 5))      # 输出：7
    try:
        print(str1.index(str2, 10))     # 输出：抛异常
    except:
        print("异常了")

    print("------ join()方法 ------")
    # todo: join() 方法
    '''
    以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    join()方法语法：
    str.join(sequence)
    '''
    s1 = "-"
    s2 = ""
    seq = ("r", "u", "n", "o", "o", "b")      # 字符串序列
    print(s1.join(seq))      # r-u-n-o-o-b
    print(s2.join(seq))      # runoob

    print("------ len() 方法 ------")
    # todo: len() 方法
    '''
    Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
    '''
    str1 = "runoob"
    print(len(str1))     # 输出：6

    l1 = [1, 2, 3, 4, 5]
    print(len(l1))       # 输出：5

    print("------ lower() 方法 ------")
    # todo： lower() 方法 转换字符串中所有大写字符为小写.
    str1 = "Runoob EXAMPLE .... WOW!!!"
    print(str1.lower())      # 输出：runoob example .... wow!!!

    print("------ split() 方法 ------")
    # todo： split(str="", num=string.count(str))方法
    '''
    以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串。
    split() 方法通过指定分隔符对字符串进行切片，该方法将字符串分割成子字符串并返回一个由这些子字符串组成的列表。
    如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
    split()方法特别适用于根据特定的分隔符将字符串拆分成多个部分。
    参数：
    str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num -- 分割次数，如果设置了这个参数，则最多分割成 maxsplit+1 个子字符串。默认为 -1, 即分隔所有。
    '''
    str1 = "this is string example ... wow !!!"

    print(str1.split())      # 默认以空格为分隔符。 输出：['this', 'is', 'string', 'example', '...', 'wow', '!!!']
    print(str1.split('i', 1))      # 以 i 为分隔符。 输出：['th', 's is string example ... wow !!!']
    print(str1.split('w'))     # 以 w 为分隔符。 输出：['this is string example ... ', 'o', ' !!!']

    print("------ strip() 方法 ------")
    # todo： strip()方法      在字符串上执行 lstrip()和 rstrip()
    '''
    Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
    注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    '''

    str1 = "*****this is **string** example....wow!!!*****"
    print(str1.strip('*'))      # 输出： this is **string** example....wow!!!

    str2 = "123abcrunoob321"    # 输出： 3abcrunoob3
    print(str2.strip("12"))










if __name__ == '__main__':
    # zhuanYiFu()              # 转义字符
    # ziFuChuanYunSuanFu()     # 字符串运算符
    # ziFuChuanGeShiHua()      # Python 字符串格式化 -- %
    # formatGeShiHua()         # Python 字符串格式化 -- format 格式化函数
    # f_string()                # Python 字符串格式化 -- f-string
    build_in()