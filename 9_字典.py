#!/usr/bin/python3

# todo：Python3 字典
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
d = {key1 : value1, key2 : value2, key3 : value3 }

键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
一个简单的字典实例：
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
'''

# todo： 创建字典
def chuangJianZiDian():

    # todo：创建空字典 -- 使用大括号来创建空字典
    emptyDict = {}
    print(emptyDict)
    print("Length：", len(emptyDict))
    print(type(emptyDict))

    # todo：创建空字典 -- 使用内建函数 dict() 创建字典
    emptyDict = dict()
    print(emptyDict)
    print("Length：", len(emptyDict))
    print(type(emptyDict))


# todo：访问字典里的值
def fangWenZiDian():
    tinydict = {'Name':'Runoob', 'Age':7, 'Class':'First'}

    print("tinydict['Name']：", tinydict['Name'])
    print("tinydict['Age']：", tinydict['Age'])

    # todo：如果用字典里没有的键访问数据，会输出错误
    try:
        print("tinydict['Alice']：", tinydict['Alice'])
    except:
        print("tinydict['Alice'] 键不存在")


# todo：修改字典
'''向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例: '''
def xiuGaiZiDian():

    tinydict = {'Name':'Runoob', 'Age':7, 'Class':'First'}
    print("原始字典：", tinydict)

    tinydict['Age'] = 8                  # 更新 Age
    tinydict['School'] = "菜鸟教程"      # 添加信息

    print("修改tinydict['Age']：", tinydict['Age'])
    print("添加tinydict['School']：", tinydict['School'])
    print("修改更新后的字典：", tinydict)


# todo：删除字典元素
'''
能删单一的元素也能清空字典，清空只需一项操作。
显式删除一个字典用del命令，如下实例：
'''
def shanChuZiDian():

    tinydict = {'Name':'Runoob', 'Age':7, 'Class':'First'}
    print("原始字典 tinydict：", tinydict)

    del tinydict['Name']      # todo：删除键 'Nnme'
    print("del tinydict['Name'] 后，tinydict：", tinydict)

    tinydict.clear()          # todo：清空字典
    print("tinydict.clear() 后，tinydict：", tinydict)

    del tinydict              # todo：删除字典

    # todo：这会引发一个异常，因为用执行 del 操作后字典不再存在：
    try:
        print("", tinydict['Age'])
        print("",tinydict['School'] )
    except:
        print("执行 del 操作后字典不再存在。此时再访问不存在的字典会抛异常")


# todo：字典内置函数&方法
def dict_build_in():

    tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

    # todo：len(dict) 函数 -- 计算字典元素个数，即键的总数。
    print(len(tinydict))      # 输出 3

    # todo：str(dict) 函数 -- 输出字典，可以打印的字符串表示。
    print(str(tinydict))     # 输出 {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

    # todo：type(variable) 函数 -- 返回输入的变量类型，如果变量是字典就返回字典类型。
    print(type(tinydict))

    # todo：clear() 方法 -- 用于删除字典内所有元素。
    tinydict = {'Name':'Zara', 'Age':7}

    print("字典长度：%d" % len(tinydict))
    tinydict.clear()
    print("字典删除后长度：%d" % len(tinydict))

    # todo：copy() 方法 -- 函数返回一个字典的浅复制。
    dict1 = {'Name':'Runoob', 'Age':7, 'Class':'First'}

    dict2 = dict1.copy()
    print("新复制的字典为：", dict2)

    # todo：fromkeys()方法 -- 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
    '''
    dict.fromkeys(seq[, value])
    seq -- 字典键值列表。
    value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
    '''
    seq = ('name', 'age', 'sex')

    tinydict = dict.fromkeys(seq)
    print("新的字典为：%s" % str(tinydict))       # 输出：新的字典为：{'name': None, 'age': None, 'sex': None}

    tinydict = dict.fromkeys(seq, 10)
    print("新的字典为：{}".format(str(tinydict)))  # 输出：新的字典为：{'name': 10, 'age': 10, 'sex': 10}


    # todo：get()方法 -- Python 字典 get() 函数返回指定键的值。
    '''
    语法：dict.get(key[, value])
    参数
    key -- 字典中要查找的键。
    value -- 可选，如果指定键的值不存在时，返回该默认值。
    返回值：返回指定键的值，如果键不在字典中返回默认值，如果不指定默认值，则返回 None
    '''
    tinydict = {'Name':'Runoob', 'Age':27}
    print("Age：{}".format(tinydict.get('Age')))      # 输出：Age：27

    # 没有设置 Sex，也没有设置默认的值，输出 None
    print("Sex：{}".format(tinydict.get('Sex')))      # 输出：Sex：None

    # 没有设置 Sex，也没有设置默认的值，输出 0.0
    print("Sex：{}".format(tinydict.get('Sex', 0.0)))      # 输出：Sex：0.0


    # todo：get() 方法 Vs dict[key] 访问元素区别
    '''
    get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。
    dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常。
    '''
    runoob = {}
    print('URL：{}'.format(runoob.get('url')))      # 输出：URL：None

    try:
        print(runoob['url'])
    except:
        print("print(runoob['url'])，'url' key 不在字典中触发异常")

    # todo：嵌套字典使用
    tinydict = {'RUNOOB' : {'url':'www.runoob.com'}}
    res = tinydict.get('RUNOOB').get('url')
    print("RUNOOB url 为：{}".format(res))      # 输出：RUNOOB url 为：www.runoob.com


    # todo：key in dict -- Python3 字典 in 操作符。如果键在字典dict里返回true，否则返回false
    thisdict = {'Name':'Runoob', 'Age':7}

    # 检测键 Age 是否存在
    if 'Age' in thisdict:
        print("键 Age 存在")      # 输出：键 Age 存在
    else:
        print("键 Age 不存在")

    # 检测键 Sex 是否存在
    if 'Sex' in thisdict:
        print("键 Sex 存在")
    else:
        print("键 Sex 不存在")      # 输出：键 Sex 不存在

    # todo：not in
    # 检测键 Age 是否存在
    if 'Age' not in thisdict:
        print("键 Age 不存在")
    else:
        print("键 Age 存在")      # 输出：键 Age 存在


    # todo：Python3 字典 items() 方法。语法：dict.items()
    '''
    Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。
    dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
    视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
    我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
    '''
    tinydict = {'Name':'Runoob', 'Age':7}
    print("Value：%s" % tinydict.items())      # 输出：Value：dict_items([('Name', 'Runoob'), ('Age', 7)])

    list1 = []
    for key, value in tinydict.items():
        list1.append(key)
        list1.append(value)
        print(list1)      # 最终输出：['Name', 'Runoob', 'Age', 7]

    # todo：Python3 字典 keys() 方法。语法：dict.keys()；values() 方法。语法：dict.values()
    dishes = {'eggs':2, 'sausage':1, 'bacon':1, 'spam':500}
    keys = dishes.keys()
    values = dishes.values()
    print("keys：{}".format(keys))      # 输出：keys：dict_keys(['eggs', 'sausage', 'bacon', 'spam'])
    print("value：{}".format(values))    # 输出：value：dict_values([2, 1, 1, 500])

    # 迭代
    n = 0
    for val in values:
        n += val
    print(n)      # 输出：504

    # keys 和 values 以相同顺序（插入顺序）进行迭代
    # 使用 list() 转换为列表
    print("keys 转换列表：{}".format(list(keys)))      # 输出：keys 转换列表：['eggs', 'sausage', 'bacon', 'spam']
    print(f"values 转换列表：{list(values)}")          # 输出：values 转换列表：[2, 1, 1, 500]

    # 视图对象是动态的，受字典变化的影响，以下删除了字典的 key，视图对象转为列表后也跟着变化
    del dishes['eggs']
    del dishes['sausage']
    print(list(keys))      # 输出：['bacon', 'spam']


    # todo：Python3 字典 update() 方法。dict.update(dict2)
    '''
    Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
    '''
    tinydict = {'Name':'Runoob', 'Age':7}
    tinydict2 = {'Sex':'female'}

    tinydict.update(tinydict2)
    print(f"更新字典 tinydict：{tinydict}")      # 输出：更新字典 tinydict：{'Name': 'Runoob', 'Age': 7, 'Sex': 'female'}


    # todo：Python3 字典 pop() 方法。语法：pop(key[,default])
    '''
    Python 字典 pop() 方法删除字典 key（键）所对应的值，返回被删除的值。
    key - 要删除的键
    dfault - 当键 key 不存在时返回的值
    返回被删除的值：
       如果 key 存在 - 删除字典中对应的元素
       如果 key 不存在 - 返回设置指定的默认值 default
       如果 key 不存在且默认值 default 没有指定 - 触发 KeyError 异常
    '''

    site = {'name':'菜鸟教程', 'alexa':10000, 'url':'www.runoob.com'}

    element = site.pop('name')
    print("被删除的元素为：", element)      # 输出：被删除的元素为： 菜鸟教程
    print("字典为：", site)            # 输出：字典为： {'alexa': 10000, 'url': 'www.runoob.com'}

    # 如果删除的键不存在会触发异常：
    try:
        element = site.pop('nickname')
        print(element)
    except:
        print("删除不存在的键 'nickname'，触发异常。")


# todo：直接赋值、浅拷贝和深度拷贝解析
'''
直接赋值：其实就是对象的引用（别名）。
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
'''
def zhiJieFuZhi_qianKaoBei_shenKaoBei():
    # todo：深度拷贝需要引入 copy 模块 -- copy.copy()：浅拷贝； copy.deepcopy()：深拷贝
    import copy

    '''
    解析：
    1、b = a: 赋值引用，a 和 b 都指向同一个对象。
    2、b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
    3、b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
    '''

    # todo：原始对象。
    a = [1, 2, 3, 4, ['a', 'b']]

    b = a                   # 赋值，传对象的引用
    c = copy.copy(a)        # 对象拷贝，浅拷贝 -- 拷贝父对象，不会拷贝对象的内部的子对象。
    d = copy.deepcopy(a)    # 对象拷贝，深拷贝 -- 完全拷贝了父对象及其子对象

    a.append(5)             # 修改对象 a
    a[4].append('c')        # 修改对象 a 中的['a', 'b']数组对象

    print('a = ', a)        # a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    print('b = ', b)        # b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    print('c = ', c)        # c =  [1, 2, 3, 4, ['a', 'b', 'c']]
    print('d = ', d)        # d =  [1, 2, 3, 4, ['a', 'b']]



if __name__ == '__main__':
    # chuangJianZiDian()      # 创建字典
    # fangWenZiDian()         # 访问字典里的值
    # xiuGaiZiDian()          # 修改字典
    # shanChuZiDian()         # 删除字典元素
    dict_build_in()         # 字典内置函数&方法
    # zhiJieFuZhi_qianKaoBei_shenKaoBei()      # 直接赋值、浅拷贝和深度拷贝解析

