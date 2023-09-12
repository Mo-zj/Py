#!/usr/bin/python3
''''''

# todo：列表
'''
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
以下是 Python 中列表的方法：
方法	                 描述
list.append(x)	     把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	     通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	     删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	     从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	     移除列表中的所有项，等于del a[:]。
list.index(x)	     返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	     返回 x 在列表中出现的次数。
list.sort()	         对列表中的元素进行排序。
list.reverse()	     倒排列表中的元素。
list.copy()	         返回列表的浅复制，等于a[:]。

注意：类似 insert, remove 或 sort 等修改列表的方法没有返回值。
'''

# todo:将列表当做堆栈使用
'''
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：
'''
def stack():

    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)      # 输出：[3, 4, 5, 6, 7]

    stack.pop()
    print(stack)      # 输出：[3, 4, 5, 6]

    stack.pop()
    print(stack)      # 输出：[3, 4, 5]

    stack.pop()
    print(stack)      # 输出：[3, 4]


# todo：将列表当作队列使用
'''
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高
在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
'''
def queue():

    list1 = ["Eric", "John", "Michael"]
    list1.append("Terry")
    list1.append("Graham")
    print(list1)             # 输出：['Eric', 'John', 'Michael', 'Terry', 'Graham']

    # list1.pop(0)
    print(list1.pop(0))      # 输出：Eric
    print(list1)             # 输出：['John', 'Michael', 'Terry', 'Graham']

    print(list1.pop(0))      # 输出：John
    print(list1)             # 输出：['Michael', 'Terry', 'Graham']


# todo：列表推导式
'''
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
'''
def LieBiaoTuiDaoShi():

    # todo：将列表中每个数值乘三，获得一个新的列表：
    vec = [2, 4, 6]
    res = [3*x for x in vec]
    print(res)      # 输出：[6, 12, 18]

    res2 = [ [x, x**2] for x in  vec]
    print(res2)      # 输出：[[2, 4], [4, 16], [6, 36]]


    # todo：对序列里每一个元素逐个调用某方法：
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    res3 = [ weapon.strip() for weapon in freshfruit ]
    print(res3)      # 输出：['banana', 'loganberry', 'passion fruit']


    # todo：可以用 if 子句作为过滤器：
    print([3*x for x in vec if x > 3])      # 输出：[12, 18]
    print([3*x for x in vec if x < 2])      # 输出：[]


    # todo：嵌套列表解析 -- Python的列表还可以嵌套。
    # 以下为3X4的矩阵列表：
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # 以下实例将3X4的矩阵列表转换为4X3列表：
    res4 = [ [row[i] for row in matrix] for i in range(4) ]
    print(res4)      # 输出：[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    # 另外一种实现方法：
    transposed = []
    for i in range(4):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    print(transposed)      # 输出：[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


    # todo：del 语句
    '''
    使用 del 语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素。这与使用 pop() 返回一个值不同。
    可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。例如：
    '''
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print(a)       # 输出：[1, 66.25, 333, 333, 1234.5]

    del a[2:4]
    print(a)       # 输出：[1, 66.25, 1234.5]

    del a[:]
    print(a)       # 输出：[]


# todo：元组
'''
元组由若干逗号分隔的值组成，元组在输出时总是有括号的，以便于正确表达嵌套结构。
在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。
'''
def YuanZu():

    t = 12345, 54321, 'hello!'
    print(t[0])      # 输出：12345
    print(t)         # 输出：(12345, 54321, 'hello!')

    t2 = t, (1,2,3,4,5)
    print(t2)        # 输出：((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))


# todo：集合
'''
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。
注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典。
'''
def JiHe():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    # 删除重复的
    print(basket)      # 输出：{'pear', 'orange', 'apple', 'banana'}

    # 集合也支持推导式
    a = { x for x in 'abracadabra' if x not in 'abc'}
    print(a)       # 输出：{'d', 'r'}


# todo：字典
'''
另一个非常有用的 Python 内建数据类型是字典。
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
一对大括号创建一个空的字典：{}。
'''
def ZiDian():

    # todo：创建字典
    tel = {'jack':4098, 'sape':4139}
    # 字典添加键值对
    tel['guido'] = 4127
    print(tel)         # 输出：{'jack': 4098, 'sape': 4139, 'guido': 4127}

    print(tel['jack'])      # 输出：4098

    del tel['sape']
    print(tel)              # 输出：{'jack': 4098, 'guido': 4127}

    tel['irv'] = 4127
    print(tel)              # 输出：{'jack': 4098, 'guido': 4127, 'irv': 4127}
    print(list(tel.keys()))   # 输出：['jack', 'guido', 'irv']

    # todo：构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
    res = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(res)      # 输出：{'sape': 4139, 'guido': 4127, 'jack': 4098}

    # todo：如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
    res2 = dict(sape=4139, guido=4127, jack=4098)
    print(res2)     # 输出：{'sape': 4139, 'guido': 4127, 'jack': 4098}


# todo：遍历技巧
def BianLiJiQiao():

    # todo：在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)      # 输出：gallahad the pure   robin the brave

    # todo：在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)      # 输出：0 tic   1 tac   2 toe

    # todo：同时遍历两个或更多的序列，可以使用 zip() 组合：
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']

    for q, a in zip(questions, answers):
        print("What is your {}? It is {}.".format(q, a))

    # 输出：
    # What is your name? It is lancelot.
    # What is your quest? It is the holy grail.
    # What is your favorite color? It is blue.

    # todo：要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
    for i in reversed(range(1, 10, 2)):
        print(i, end=" ")      # 输出：9 7 5 3 1

    # todo：要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f, end=" ")      # 输出：apple banana orange pear









if __name__ == '__main__':
    # stack()      # 将列表当做堆栈使用
    # queue()      # 将列表当做队列使用
    # LieBiaoTuiDaoShi()      # 列表推导式
    # YuanZu()                # 元组
    # JiHe()                  # 集合
    # ZiDian()                # 字典
    BianLiJiQiao()          # 遍历技巧



