#!/usr/bin/python3


# todo：以下实例使用了 while 来计算 1 到 100 的总和：
def Sum_1to100():
    n = 100
    sum = 0
    counter = 1
    while counter <= n:
        sum = sum + counter
        counter += 1

    print("1 到 %d 之和为：%d"%(n, sum))


# todo：无限循环 -- 通过设置条件表达式永远不为 false 来实现无限循环
def WuXianXunHuan():
    var = 1
    while var == 1:      # 表达式永远为 true
         num = int(input("请输入一个数字："))
         print("你输入的数字是：", num)

    # 你可以使用 CTRL+C 来退出当前的无限循环。无限循环在服务器上客户端的实时请求非常有用。

    print("Good bye!")


# todo：while 循环使用 else 语句 -- 如果 while 后面的条件语句为 false 时，则执行 else 的语句块。
def While_else():

    count = 0
    while count < 5:
        print(count, " 小于5")
        count += 1
    else:
        print(count, " 大于或等于5")


# todo：for...else -- 在 Python 中，for...else 语句用于在循环结束后执行一段代码。
def For_else():

    for x in range(6):
        print(x)
    else:
        print("Finally finished")


# todo：break 和 continue 语句及循环中的 else 子句
'''
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''

def Break():

    for letter in 'Runoob':
        if letter == 'o':      # 字母为 o 时，终止循环
            break
        print('当前字母：', letter)

    var = 10
    while var > 0:
        var = var - 1
        if var == 5:      # 变量为 5 时，终止循环
            break
        print('当前变量值：', var)

    print("Good Bye!")


def Continue():

    for letter in 'Runoob':
        if letter == 'o':      # 字母为 o 时跳过输出
            continue
        print('当前字母：', letter)

    var = 10
    while var > 0:
        var = var - 1
        if var == 5:      # 变量为 5 时跳过输出
            continue
        print('当前变量值：', var)

    print("Good Bye!")


# todo：循环语句可以有 else 子句，
'''
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，
但循环被 break 终止时不执行。
如下实例用于查询质数的循环例子:
'''
def Else_break():

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, '等于', x, '*', n//x)
                break
        else:
            # 循环中没有找到元素
            print(n, ' 是质数')







if __name__ == '__main__':
    # Sum_1to100()      # 算 1 到 100 的总和
    # WuXianXunHuan()   # 无限循环
    # While_else()      # while_else语句
    # For_else()        # For_else语句
    # Break()           # break 语句
    # Continue()        # continue 语句
    Else_break()      #