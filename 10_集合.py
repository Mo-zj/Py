#!/usr/bin/python3

# todo：Python3 集合
'''
集合（set）是一个无序的不重复元素序列。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
'''

# todo：创建集合
'''
可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
def chuangJianJiHe():

    # todo：直接使用大括号创建集合
    set1 = {1, 2, 3, 4}
    print(set1)            # 输出：{1, 2, 3, 4}

    # todo：使用 set() 函数从列表创建集合
    list1 = [4, 5, 6,7]
    set2 = set(list1)
    print(set2)            # 输出：{4, 5, 6, 7}

    # todo：{ } 是用来创建一个空字典
    dict1 = {}
    print("dict1：{}，type(dict1)：{}".format(dict1, type(dict1)))       # 输出：dict1：{}，type(dict1)：<class 'dict'>

    # todo：创建一个空集合必须用 set()
    set1 = set()
    print("set1：{}，type(set1)：{}".format(set1, type(set1)))           # 输出：set1：set()，type(set1)：<class 'set'>


# todo：集合的基本操作
def jiBenCaoZuo():

    # todo：使用集合进行去重
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)      # 输出：{'pear', 'banana', 'orange', 'apple'}

    # todo：添加元素。将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。语法：s.add( x )
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.add("Facebook")
    print(thisset)     # 输出：{'Google', 'Runoob', 'Facebook', 'Taobao'}

    # 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：s.update( x )
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.update({1,3})
    print(thisset)      # 输出：{'Taobao', 1, 'Runoob', 3, 'Google'}

    # x 可以有多个，用逗号分开。
    thisset.update([1,4], [5,6])
    print(thisset)     # 输出：{'Taobao', 1, 3, 4, 5, 6, 'Google', 'Runoob'}

    # todo：移除元素。将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。语法：s.remove( x )
    '''
    将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
    '''
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.remove("Taobao")
    print(thisset)      # 输出：{'Runoob', 'Google'}

    try:
        thisset.remove("Facebook")
    except:
        print("移除不存在的集合元素，抛异常")

    # 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。语法：s.discard( x )
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.discard("Facebook")
    print(thisset)       # 输出：{'Runoob', 'Google', 'Taobao'}

    # todo：计算集合个数
    thisset = set(("Google", "Runoob", "Taobao"))
    print(len(thisset))      # 输出：3

    # todo：清空集合。语法：s.clear()
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.clear()
    print(thisset)      # 输出：set()

    # todo：判断元素是否存在集合中。
    thisset = set(("Google", "Runoob", "Taobao"))
    print("Runoob" in thisset)      # 输出：True
    print("Facebook" in thisset)    # 输出：False



if __name__ == '__main__':
    # chuangJianJiHe()      # 创建集合
    jiBenCaoZuo()



