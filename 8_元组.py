#!/usr/bin/python3

# todo：创建元组
'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''

def chuangJianYuanZu():
    tup0 = ()     # 创建空元组
    print(type(tup0), tup0)

    tup1 = ('Google', 'Runoob', 2000, 1995)
    print(type(tup1), tup1)

    tup2 = (1, 2, 3, 4, 5)
    print(type(tup2), tup2)

    tup3 = "a", "b", "c", "d"      # todo: 不需要括号也可以
    print(type(tup3), tup3)        # 输出：<class 'tuple'> ('a', 'b', 'c', 'd')

    # todo： 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
    tup4 = (50)
    print(type(tup4), tup4)      # 输出：<class 'int'> 50

    tup5 = (50,)
    print(type(tup5), tup5)      # 输出：<class 'tuple'> (50,)

# todo：修改元组
'''
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
'''
def xiuGaiYuanzu():

    tup1 = (12, 34.56)
    tup2 = ('abc', 'xyz')

    # 以下修改元组元素操作是非法的
    try:
        tup1[0] = 100         # todo:非法操作，抛异常
    except:
        print("修改元组元素会抛异常")

    # 创建一个新的元组
    tup3 = tup1 + tup2
    print(tup3)      # 输出：(12, 34.56, 'abc', 'xyz')


# todo：删除元组
'''元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例: '''
def shanChuYuanZu():

    tup = ('Google', 'Runoob', 1997, 2000)

    print(tup)
    del tup

    try:
        print("删除后的元组 tup：")
        print(tup)      # todo：元组被删除后，输出变量会有异常信息
    except:
        print("元组被删除后，输出变量会有异常信息")


if __name__ == '__main__':
    # chuangJianYuanZu()     # 创建元组
    # xiuGaiYuanzu()         # 修改元组
    shanChuYuanZu()         # 删除元组

















