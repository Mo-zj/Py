#!/usr/bin/python3
''''''

# todo：输出格式美化
'''
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    str()： 函数返回一个用户易读的表达形式。
    repr()： 产生一个解释器易读的表达形式。
'''
def ShuChuGeShiHua():

    s = 'Hello，Runoob'
    print(str(s))      # 输出：Hello，Runoob     todo：str()： 函数返回一个用户易读的表达形式。
    print(repr(s))     # 输出：'Hello，Runoob'   todo：repr()： 产生一个解释器易读的表达形式。

    x = 10*3.25
    y = 200*200
    s = 'x 的值为：' + repr(x) + '，y 的值为：' + repr(y) + '...'
    print(s)       # 输出：x 的值为：32.5，y 的值为：40000...

    # todo：repr() 函数可以转义字符串中的特殊字符
    hello = 'hello，runoob\n'
    print(repr(hello))       # 输出：'hello，runoob\n'

    # todo：repr() 的参数可以是 Python 的任何对象
    print(repr((x, y, ('Google', 'Runoob'))))      # 输出：(32.5, 40000, ('Google', 'Runoob'))

    # todo：这里有两种方式输出一个平方与立方的表:
    '''
    注意：在第一个例子中, 每列间的空格由 print() 添加。
    这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
    还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
    '''
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
        # 注意前一行 'end' 的使用
        print(repr(x*x*x).rjust(4))
    '''
    输出：
     1   1    1
     2   4    8
     3   9   27
     4  16   64
     5  25  125
     6  36  216
     7  49  343
     8  64  512
     9  81  729
    10 100 1000
    '''

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    '''
    输出：
     1   1    1
     2   4    8
     3   9   27
     4  16   64
     5  25  125
     6  36  216
     7  49  343
     8  64  512
     9  81  729
    10 100 1000
    '''

    # todo：str.format() 的基本使用如下:
    # 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
    print('{}网址："{}!"'.format('菜鸟教程', 'www.runoob.com'))      # 输出：菜鸟教程网址："www.runoob.com!"

    # 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
    print('{0} 和 {1}'.format('Google', 'Runoob'))      # 输出：Google 和 Runoob
    print('{1} 和 {0}'.format('Google', 'Runoob'))      # 输出：Runoob 和 Google

    # 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
    print('{name}网址：{site}'.format(name='菜鸟教程', site='www.runoob.com'))      # 输出：菜鸟教程网址：www.runoob.com

    # 位置及关键字参数可以任意的结合:
    print('站点列表 {0}，{1} 和 {other}'.format('Google', 'Runoob', other='Taobao'))      # 输出：站点列表 Google，Runoob 和 Taobao

    # 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
    import math
    print(math.pi)      # 输出：3.141592653589793
    print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))      # 输出：常量 PI 的值近似为 3.142。

    # 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
    table = {'Google':1, 'Runoob':2, 'Taobao':3}
    for name, number in table.items():
        print('{0:10} ===> {1:10d}'.format(name, number))
    '''
    输出：
    Google     ===>          1
    Runoob     ===>          2
    Taobao     ===>          3
    '''

    # 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
    # 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
    table = {'Google':1, 'Runoob':2, 'Taobao':3}
    print('Runoob：{0[Runoob]}；Google：{0[Google]}；Taobao：{0[Taobao]}'.format(table))
    # 输出：Runoob：2；Google：1；Taobao：3

    # 也可以通过在 table 变量前使用 ** 来实现相同的功能：
    print('Runoob：{Runoob:d}；Google：{Google:d}；Taobao：{Taobao:d}'.format(**table))
    # 输出：Runoob：2；Google：1；Taobao：3

    # todo：旧式字符串格式化
    '''
    % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
    '''
    print('常量 PI 的值近似为：%5.3f。' % math.pi)      # 输出：常量 PI 的值近似为：3.142。

    # 因为 str.format() 是比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().


# todo：读取键盘输入
'''
Python 提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
'''
def JianPanShuRu():

    str = input("请输入：")
    print("你输入的内容是：", str)





if __name__ == '__main__':
    # ShuChuGeShiHua()      # 输出格式美化
    JianPanShuRu()          # 读取键盘输入










