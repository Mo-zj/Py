#!/usr/bin/python3
''''''

# todo：Python3 File(文件) 方法
'''
open() 方法
Python open() 方法用于打开一个文件，并返回文件对象。
在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
open(file, mode='r')
完整的语法格式为：
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

参数说明:
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

mode 参数有：
模式	    描述
t	    文本模式 (默认)。
x	    写模式，新建一个文件，如果该文件已存在则会报错。
b	    二进制模式。
+	    打开一个文件进行更新(可读可写)。
U	    通用换行模式（Python 3 不支持）。
r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+	    打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	    以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	    以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	    打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	    以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

默认为文本模式，如果要以二进制模式打开，加上 b 。
'''

# todo：file 对象。file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

# todo：File close() 方法
'''
close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。
'''
def file_close():

    # 打开文件
    fo = open("./tmp/runoob.txt", "wb")
    print("文件名：", fo.name)      # 输出： 文件名： ./tmp/runoob.txt

    # 关闭文件
    fo.close()


# todo：File flush() 方法
'''
flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要被动的等待输出缓冲区写入。
一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。

write() 方法用于向文件中写入指定字符串。
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
'''
def file_flush():

    fo = open("./tmp/runoob.txt", "wb")
    print("文件名：", fo.name)      # 输出： 文件名： ./tmp/runoob.txt

    # 刷新缓冲区
    fo.flush()

    # 关闭文件
    fo.close()


# todo：File fileno() 方法
'''
fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。
返回值
返回文件描述符。
'''
def file_fileno():

    fo = open("./tmp/runoob.txt", "wb")
    print("文件名：", fo.name)      # 输出：文件名： ./tmp/runoob.txt

    fid = fo.fileno()
    print("文件描述符为：", fid)      # 输出： 文件描述符为： 3

    fo.close()


# todo：File isatty() 方法
'''
isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。
'''
def file_isatty():

    fo = open("./tmp/runoob.txt", "wb")
    print("文件名为：", fo.name)

    ret = fo.isatty()
    print("返回值：", ret)      # 输出： 返回值： False

    fo.close()


# todo：File read() 方法
'''
read() 方法用于从文件读取指定的字符数（文本模式 t）或字节数（二进制模式 b），
如果未给定参数 size 或 size 为负数则读取文件所有内容。

语法
read() 方法语法如下：
fileObject.read([size]); 

参数
size -- 从文件中读取的字符数（文本模式）或字节数（二进制模式），默认为 -1，表示读取整个文件。

返回值
返回从字符串中读取的字节。
'''
def file_read():

    fo = open("./tmp/file_read.txt", "w+")

    for i in range(1,7):
        fo.write("这是第{}行\n".format(i))

    fo.close()

    fo = open("./tmp/file_read.txt", "r+")

    line = fo.read(10)
    print("读取的字符串：%s" % (line))
    '''
    输出：
    读取的字符串：这是第1行
    这是第2
    '''
    fo.close()


# todo：File readline() 方法
'''
readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。

语法
readline() 方法语法如下：
fileObject.readline(); 

参数
size -- 从文件中读取的字节数。

返回值
返回从字符串中读取的字节。
'''
def file_readline():

    fo = open("./tmp/file_readline.txt", "w+")

    for i in range(1, 6):
        fo.write(f"{i}:www.runoob.com\n")

    fo.close()

    fo = open("./tmp/file_readline.txt", "r+")

    line = fo.readline()
    print("读取第一行 %s" % (line))
    '''
    读取第一行 1:www.runoob.com

    '''

    line = fo.readline(5)
    print("读取的字符串为：%s" % (line))      # 输出：读取的字符串为：2:www


# todo：File readlines() 方法
'''
readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。 如果碰到结束符 EOF 则返回空字符串。
如果碰到结束符 EOF 则返回空字符串。

语法
readlines() 方法语法如下：

fileObject.readlines( );
参数
无。

返回值
返回列表，包含所有的行。
'''
def file_readlines():

    fo = open("./tmp/file_readlines.txt", "w+")

    for i in range(1, 6):
        fo.write(f"{i}:www.runoob.com\n")

    fo.close()

    fo = open("./tmp/file_readlines.txt", "r")

    # for line in fo.readlines():
    #     print("读取的数据为：%s" % line)
    '''
    输出：
    读取的数据为：1:www.runoob.com

    读取的数据为：2:www.runoob.com

    读取的数据为：3:www.runoob.com

    读取的数据为：4:www.runoob.com

    读取的数据为：5:www.runoob.com


    '''

    for line in fo.readlines():
        line = line.strip()      # 把换行去掉
        print("读取的数据为：%s" % line)
    '''
    输出：
    读取的数据为：1:www.runoob.com
    读取的数据为：2:www.runoob.com 
    读取的数据为：3:www.runoob.com
    读取的数据为：4:www.runoob.com
    读取的数据为：5:www.runoob.com

    '''

    fo.close()


# todo：File seek() 方法
'''
seek() 方法用于移动文件读取指针到指定位置。

语法
seek() 方法语法如下：

fileObject.seek(offset[, whence])
参数
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。

whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。

返回值
如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
'''
def file_seek():
    f = open("./tmp/file_seek.txt", "wb+")
    print(f.write(b'0123456789abcdef'))      # 输出：16
    print(f.seek(5))      # 移动到文件的第六个字节，输出：5
    print(f.read(1))      # 输出：b'5'
    print(f.seek(-3,2))      # 移动到文件倒数第三个字节，输出：13
    print(f.read(1))      # 输出：b'd'

    fo = open("./tmp/file_seek2.txt", "w+")
    fo.write("0123456789abcdef")
    fo.close()

    fo = open("./tmp/file_seek2.txt", "r+")

    line = fo.readline()
    print("读取的数据为：%s" % (line))      # 输出：读取的数据为：0123456789abcdef

    line = fo.readline()
    print("读取的数据为：%s" % (line))      # 输出：读取的数据为：

    # 重新设置文件读取指针到开头
    fo.seek(0, 0)
    line = fo.readline()
    print("读取的数据为：%s" % (line))      # 输出：读取的数据为：0123456789abcdef

    fo.close()


# todo：File tell() 方法
'''
tell() 方法返回文件的当前位置，即文件指针当前位置。
'''
def file_tell():

    fo = open("./tmp/file_readline.txt", "r+")

    line = fo.readline()
    print("读取的数据为：%s" % (line))

    # 获取当前文件位置
    pos = fo.tell()
    print(pos)

    fo.close()


# todo：File truncate() 方法
'''
truncate() 方法用于从文件的首行首字节开始截断，截断文件为 size 个字节，无 size 表示从当前位置截断；
截断之后 V 后面的所有字节被删除，其中 Widnows 系统下的换行代表2个字节大小。

语法
truncate() 方法语法如下：

fileObject.truncate( [ size ])
参数
size -- 可选，如果存在则文件截断为 size 字节。
'''
def file_truncate():

    fo = open("./tmp/file_truncate.txt", "w+")

    for i in range(1, 6):
        fo.write("{}:www.runoob.com\n".format(i))

    fo.close()

    fo = open("./tmp/file_truncate.txt", "r+")
    line = fo.readline()
    print("读取行：%s" % (line))      # 输出：读取行：1:www.runoob.com

    fo.truncate()
    line = fo.readlines()
    print("读取行：%s" % (line))
    # 输出：读取行：['2:www.runoob.com\n', '3:www.runoob.com\n', '4:www.runoob.com\n', '5:www.runoob.com\n']

    fo.seek(0, 0)        # 移动指针到开头
    fo.truncate(10)      # 截取 runoob.txt 文件的10个字节
    line = fo.readlines()
    print("读取行：%s" % (line))    # 输出：读取行：['1:www.runo']

    fo.close()


# todo：File write() 方法
'''
write() 方法用于向文件中写入指定字符串。
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。
'''
def file_write():

    fo = open("./tmp/file_write.txt", "w+")
    for i in range(1, 6):
        fo.write("{}:www.runoob.com\n".format(i))

    fo.flush()
    fo.seek(0, 0)      # 写入完文本后，文本指针在文本最后，需要先把指针定位到开头。

    line = fo.readlines()
    print("读取数据：", line)
    # 输出：读取数据： ['1:www.runoob.com\n', '2:www.runoob.com\n', '3:www.runoob.com\n', '4:www.runoob.com\n', '5:www.runoob.com\n']

    fo.close()

    fo = open("./tmp/file_write.txt", "r+")
    print("文件名：", fo.name)      # 输出：文件名： ./tmp/file_write.txt

    str1 = "6:www.runoob.com"
    # 在文件末尾写入一行
    fo.seek(0, 2)
    fo.write(str1)

    # 读取文件所有内容
    fo.seek(0, 0)
    for index in range(6):
        line = next(fo)
        print("文件行号 %d - %s" % (index, line))

    '''
    文件行号 0 - 1:www.runoob.com

    文件行号 1 - 2:www.runoob.com

    文件行号 2 - 3:www.runoob.com

    文件行号 3 - 4:www.runoob.com

    文件行号 4 - 5:www.runoob.com

    文件行号 5 - 6:www.runoob.com
    '''

    fo.close()


# todo：File writelines() 方法
'''
writelines() 方法用于向文件中写入一序列的字符串。
这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
换行需要制定换行符 \n。
'''
def file_writelines():

     fo = open("./tmp/file_writelines.txt", "w+")
     print("文件名：%s" % fo.name)      # 输出：文件名：./tmp/file_writelines.txt

     seq = ["菜鸟教程 1\n", "菜鸟教程 2\n"]
     fo.writelines(seq)

     fo.seek(0, 0)
     print("读取的数据：", fo.readlines())      # 输出：读取的数据： ['菜鸟教程 1\n', '菜鸟教程 2\n']

     flag = True

     fo.seek(0, 0)
     while flag:
         try:
            print(next(fo))
         except:
             print("已迭代完成")
             break


     fo.close()







if __name__ == '__main__':
    # file_close()
    # file_flush()
    # file_fileno()
    # file_isatty()
    # file_read()
    # file_readline()
    # file_readlines()
    # file_seek()
    # file_tell()
    # file_truncate()
    # file_write()
    file_writelines()