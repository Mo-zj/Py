import sys
import getopt

"""
getopt 模块
getopt 模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是 sys.argv。命令行选项使得程序的参数更加灵活。支持短选项模式 - 和长选项模式 --。

该模块提供了两个方法及一个异常处理来解析命令行参数。
"""

"""
getopt.getopt(args, shortopts, longopts=[])

三个参数：

 args: 这个很清楚，就是参数列表。直接把 sys.args[1:] 切片传进来就可以。
 
 shortopts: 这个参数是个字符串，把需要解析的“短选项”挨着写在一起就可以，这里的“短选项”指的是以 '-' 开头的选项，
 叫短选项是因为这种选项只支持单个字母，就算你写 -test 这样子的参数，能被 getopt 识别出来的也是 -t 和 est，其中 est 会被当作 -t 选项的参数。
 所以假设你想支持 “-h -i -o” 三个短选项， shortopts 就可以写成 “hio”。如果其中某个短选项想要接受参数，比如 "-h -i inputfile -o outputfile"，
 那就需要在字母后面加 ":" 冒号，变成 "hi:o:"
 
 longopts=[]: 这个参数是个列表，因为每个长选项有多个字母，不可能像短选项一样用一个字符串就都表示出来。所谓长选项，
 就是以 “--” 开头的选项，比如 --usr --ifile --ofile 等，传参的时候写成 ['--user', '--ifile', '--ofile']，
 如果某个选项需要接受参数，则在后面加 "=" 等号，比如 ['--user', '--ifile=', '--ofile=']。
 
 
返回值，有两个：
 
 opts：是有一个列表，列表里是元组（opt, value）的格式。比如上面的 "-h -i inputfile -o outputfile" 
 那就是 [('-h', ''), ('-i', 'inputfile'), ('-o', 'outputfile')] 这样的返回值。长选项和短选项以及各自的参数都会按先后次序放在这里。
 用的时候可以以 for opt,val in opts: 这样的方式来遍历。值得注意的是，返回的 opt 里面，'-' 和 '--' 都被保留下来了， 另外，当用户输入的长选项没有写完的时候，
 会被自动补全。比如用户输入的是 --u，通过 getopt 会被自动补全成 --user，这个需要注意（除非有两个长选项都有相同的开头，无法确定是哪个）。
 
 args：如果用户输入的信息太多，除了长选项和短选项以及各自选项的参数以外，还有一些其它的未知的参数，则会被放到这里。 
 看了这些，再去看上面的例子，相信会清楚很多了

"""

def site():
    name = None
    url = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'a:b:')  # 短选项模式

    except:
        print("Error")

    for opt, arg in opts:
        if opt in ['-a']:
            name = arg
        elif opt in ['-b']:
            url = arg

    print(name + " " + url)


def site_long():
    name = None
    url = None

    argv = sys.argv[1:]

    try:
        opts, argvs = getopt.getopt(argv, "n:u:", ["name=", "url="])      # 长选项模式

        print(opts, argvs)

    except:
        print("Error")

    for opt, arg in opts:

        print(opt, arg)   # 调试打印

        if opt in ['-n', '--name']:
            name = arg
        elif opt in ['-u', '--url']:
            url = arg

    print(name + " " + url)


"""
Exception getopt.GetoptError
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

异常的参数是一个字符串，表示错误的原因。属性 msg 和 opt 为相关选项的错误信息。
"""

def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('except getopt.GetoptError: 2_test_getopt.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    print(opts)  # 调试打印
    for opt, arg in opts:

        print(opt, arg)   # 调试打印

        if opt == '-h':
            print('2_test_getopt.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)


if __name__ == "__main__":

    main(sys.argv[1:])   #python 2_test_getopt.py -h
                         #python 2_test_getopt.py -i RUNooB -o www.runoob.com

# site()    #python 2_test_getopt.py -a RUNooB -b www.runoob.com

# site_long()      #python 2_test_getopt.py -n RUNooB -u www.runoob.com
