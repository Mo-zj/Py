#!/usr/bin/python3

import operator

# todo: 更新列表：你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项，如下所示：
def genXinLieBiao():

    list1 = ['Google', 'Runoob', 1997, 2000]
    print("第三个元素为：", list1[2])      # 输出：第三个元素为： 1997

    list1[2] = '2001'
    print("第三个元素为：", list1[2])      # 输出：第三个元素为： 2001

    list1.append('Baidu')
    print("更新后的列表：", list1)      # 输出：更新后的列表： ['Google', 'Runoob', '2001', 2000, 'Baidu']


# todo: 删除列表元素：可以使用 del 语句来删除列表的的元素，如下实例：
def shanChuLieBiaoYuanSu():

    list1 = ['Google', 'Runoob', 1997, 2000]
    print("原始列表：", list1)            # 原始列表： ['Google', 'Runoob', 1997, 2000]

    del list1[2]
    print("删除第三个元素：", list1)       # 删除第三个元素： ['Google', 'Runoob', 2000]

# todo: 嵌套列表，使用嵌套列表即在列表里创建其它列表
def qianTaoLieBiao():

    a = ['a', 'b', 'c']
    n = [1, 2, 3]

    x = [a, n]
    print(x)               # 输出：[['a', 'b', 'c'], [1, 2, 3]]
    print(x[0])            # 输出：['a', 'b', 'c']
    print(x[0][1])         # 输出：b


# todo: 列表比较，列表比较需要引入 operator 模块的 eq 方法
def lieBiaoBiJiao():

    a = [1, 2]
    b = [2, 3]
    c = [2, 3]

    print("operator.eq(a,b)：", operator.eq(a, b))     # operator.eq(a,b)： False
    print("operator.eq(b,c)：", operator.eq(b, c))     # operator.eq(b,c)： True


# todo: Python列表函数&方法
def lieBiaoHanShu_fangfa():

    print("------ len(list) 函数 ------")
    # todo: 函数 -- len(list)：返回列表元素个数
    list1 = ['Google', 'Runoob', 'Taobao']
    print(len(list1))      # 输出：3

    print("------ max(list) 函数 ------")
    # todo：函数 -- max(list)：返回列表元素中的最大值
    list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
    print("list1 最大元素值：", max(list1))      # 输出：list1 最大元素值： Taobao
    print("list2 最大元素值：", max(list2))      # 输出：list2 最大元素值： 700

    print("------ min(list) 函数 ------")
    # todo：函数 -- min(list)：返回列表元素中的最小值
    list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
    print("list1 最小元素值：", min(list1))      # 输出：list1 最小元素值： Google
    print("list2 最小元素值：", min(list2))      # 输出：list2 最小元素值： 200

    print("------ list(seq) 函数 ------")
    # todo:函数 -- list(seq)：list() 方法用于将元组或字符串转换为列表。
    '''
    注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
    '''
    aTuple = (123, 'Google', 'Runoob', 'Taobao')
    list1 = list(aTuple)
    print("列表元素：", list1)   # 输出：列表元素： [123, 'Google', 'Runoob', 'Taobao']

    str1 = "Hello World"
    list2 = list(str1)
    print("列表元素：", list2)   # 输出：列表元素： ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

    print("------ list.append(obj) 函数 ------")
    # todo：方法 -- list.append(obj)：append() 方法用于在列表末尾添加新的对象。
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.append('Baidu')
    print("更新后的列表：", list1)      # 更新后的列表： ['Google', 'Runoob', 'Taobao', 'Baidu']

    print("------ list.count(obj) 函数 ------")
    # todo：方法 -- list.count(obj)：count() 方法用于统计某个元素在列表中出现的次数。
    aList = [123, 'Google', 'Runoob', 'Taobao', 123]
    print("123 元素个数：", aList.count(123))              # 输出：123 元素个数： 2
    print("Runoob 元素个数：", aList.count('Runoob'))      # 输出：Runoob 元素个数： 1

    print("------ list.extexd(seq) 函数 ------")
    # todo：方法 -- list.extexd(seq): extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    '''
    seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
    '''
    # 列表
    language = ['French', 'English', 'German']
    # 元祖
    language_tuple = ('spanish', 'Portuguese')
    # 集合
    language_set = {'Chinese', 'Japanese'}

    # 添加元组元素到列表末尾
    language.extend(language_tuple)
    print('新列表：', language)   # 输出：新列表： ['French', 'English', 'German', 'spanish', 'Portuguese']

    # 添加集合元素到列表末尾
    language.extend(language_set)
    print('新列表：', language)   # 输出：新列表： ['French', 'English', 'German', 'spanish', 'Portuguese', 'Chinese', 'Japanese']

    print("------ list.index(obj) 函数 ------")
    # todo：方法 -- list.index(obj)：index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
    '''
    语法：list.index(x[, start[, end]])
    返回值：该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
    '''
    list1 = ['Google', 'Runoob', 'Taobao']
    print('Runoob索引值为：', list1.index('Runoob'))      # Runoob索引值为： 1
    print('Taobao索引值为：', list1.index('Taobao'))      # Taobao索引值为： 2
    try:
        print('JingDong索引值为：', list1.index('JingDong'))     # 抛异常
    except:
        print("列表中无'JingDong'对象，抛异常")

    print("------ list.insert(index,obj) 函数 ------")
    # todo：方法 -- list.insert(index,obj)：insert() 函数用于将指定对象插入列表的指定位置。
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.insert(1, 'Baidu')
    print(list1)       # 输出： ['Google', 'Baidu', 'Runoob', 'Taobao']

    print("------ list.pop(index=-1) 函数 ------")
    # todo：方法 -- list.pop(index=-1)：pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    '''
    index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
    '''
    list1 = ['Google', 'Runoob', 'Taobao']
    list1.pop()
    print("列表现在为：", list1)      # 输出：列表现在为： ['Google', 'Runoob']

    list1.pop(0)
    print("列表现在为：", list1)      # 输出：列表现在为： ['Runoob']

    print("------ list.remove(obj) 函数 ------")
    # todo：方法 -- list.remove(obj)：remove() 函数用于移除列表中某个值的第一个匹配项
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.remove('Taobao')
    print("列表现在为：", list1)      # 列表现在为： ['Google', 'Runoob', 'Baidu']

    list1.remove('Baidu')
    print("列表现在为：", list1)      # 列表现在为： ['Google', 'Runoob']

    print("------ list.reverse() 函数 ------")
    # todo：方法 -- list.reverse()：reverse() 函数用于反向列表中元素
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.reverse()
    print("列表现在为：", list1)      # 列表现在为： ['Baidu', 'Taobao', 'Runoob', 'Google']

    print("------ list.sort() 函数 ------")
    # todo：方法 -- list.sort(key=None,reverse=False)
    '''
    sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
    '''
    aList1 = [1, 4, 5, 2, 3]
    aList1.sort()
    print("aList1：", aList1)      # 输出：aList1： [1, 2, 3, 4, 5]  升序

    aList1.sort(reverse=True)
    print("aList1：", aList1)      # 输出：aList1： [5, 4, 3, 2, 1]  降序

    vowels = ['e', 'a', 'u', 'o', 'i']
    vowels.sort(reverse=True)
    print("vowels：", vowels)     # 输出：vowels： ['u', 'o', 'i', 'e', 'a'] 降序

    print("------ list.clear() 函数 ------")
    # todo：方法 -- list.clear()：clear() 函数用于清空列表，类似于 del a[:]
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list1.clear()
    print("列表清空后：", list1)      # 输出：列表清空后： []

    print("------ list.copy() 函数 ------")
    # todo：方法 -- list.copy()：copy() 函数用于复制列表，类似于 a[:]。
    list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    list2 = list1.copy()
    print("list2 列表：", list2)     # 输出：list2 列表： ['Google', 'Runoob', 'Taobao', 'Baidu']























if __name__ == '__main__':
    # genXinLieBiao()            # 更新列表
    # shanChuLieBiaoYuanSu()     # 删除列表元素
    # qianTaoLieBiao()           # 嵌套列表
    # lieBiaoBiJiao()            # 列表比较
    lieBiaoHanShu_fangfa()




