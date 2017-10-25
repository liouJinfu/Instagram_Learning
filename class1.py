# -*- encoding=UTF-8 -*-
import os
import string
import datetime
import random
import re

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


def demo_string():
    # string 的常见用法：

    print "#########################################################################"
    print "###下面是string中 常见的一些固定的变量"
    print "###asci 字符串 大写字符串 小写字符串 etc"
    print "#########################################################################"
    print string.ascii_letters
    print string.ascii_lowercase
    print string.ascii_uppercase
    print string.digits
    print string.hexdigits
    print string.letters
    print string.octdigits
    print string.punctuation
    print string.printable
    print string.uppercase
    print string.whitespace


def demo_string_format():
    print "#########################################################################"
    print "###下面是string中 格式化 字符串的用法，使用format"
    print "###"
    print "#########################################################################"
    # 通过 位置找到需要格式的字符串的 具体位置
    print  '{0}, {1}, {2}'.format('a', 'b', 'c')
    print '{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
    print '{2}, {1}, {0}'.format('a', 'b', 'c')
    print '{2}, {1}, {0}'.format(*'abc')  # unpacking argument sequence
    print '{2}{1}{0}{2}{1}{0}'.format(*'abc')  # arguments' indices can be repeated
    ## 通过 name进行 forma
    print 'Coordinates: {latitude}, {longitude}'.format(latitude="32.1111N", longitude="-115.222W")
    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print 'Coordinates: {latitude}, {longitude}'.format(**coord)

    print str(Point(4, 2))

    coord = [3, 5]
    print  'X: {0[0]};  Y: {0[1]}'.format(coord)  # X: 3;  Y: 5
    print "repr() shows quotes: {:s}; str() doesn't: {!s}".format('test1',
                                                                  'test2')  # repr() shows quotes: test1; str() doesn't: test2
    ##Aligning the text and specifying a width:
    print '{:<30}'.format('left aligned')  # left aligned                  /
    print '{:>30}'.format('right aligned')  # right aligned/
    print '{:^30}'.format('centered')  # centered           /
    print '{:*^30}'.format('centered')  # use '*' as a fill char /***********centered***********/
    ##Replacing %+f, %-f, and % f and specifying a sign:
    print '{:+f}, {:+f}'.format(3.14, -3.14)  # show it always '+3.140000; -3.140000'
    print '{: f}, {: f}'.format(+3.14, -3.14)  # 3.140000, -3.140000
    print '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'

    ##Replacing %x and %o and converting the value to different bases:
    print "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)  ##int: 42;  hex: 2a;  oct: 52;  bin: 101010
    print "int : {0:#d}, hex: {0:#x}, oct:{0:#o}, bin: {0:#b}".format(
        33)  ##int : 33, hex: 0x21, oct:0o41, bin: 0b100001

    ##Using the comma as a thousands separator:
    print '{:,}'.format(1234567890)  # 1,234,567,890

    # Expressing a percentage:
    points = 19.5
    total = 22
    print "Correct answer {:.2%}".format(points / total)  # Correct answer 88.636%

    # Using type-specific formatting:
    d = datetime.datetime(2017, 10, 19, 12, 15, 58)
    print '{:%Y-%m-%d %H:%M:%S}'.format(d)  # 2010-07-04 12:15:58

    # Special use
    octets = [192, 168, 0, 1]
    print '{:02X}{:02X}{:02X}{:02X}'.format(*octets)  # C0A80001

    dic = {"name": "jinfu liu", "height": "181cm", "weight": "77kg"}
    print "My name is {name}, and height {height}, weight {weight}".format(
        **dic)  # My name is jinfu liu, and height 181cm, weight 77kg


def demo_string_func():
    stra = "h e l l o w o r l d"
    print string.capwords(stra)  ##H E L L O W O R L D but "hello world" -> "Hello World"
    strFrom = "HeloWd"
    strTo = "WorlHe"
    map = string.maketrans(strFrom, strTo)
    print "Hello World".translate(map)  ## build map H -> W ;e -> o; l -> r; o -> l; W -> h; d -> e
    strb = "192"
    print string.atof(strb)  # 192.0
    print string.atoi(strb)  # 192 string to int
    print string.atol(strb)  # 192 string to long
    print string.capitalize(stra)  # Return a copy of stra with only its first character capitalized.
    print string.find(stra,
                      'h e')  ##Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end]. Return -1 on failure. Defaults for start and end and interpretation of negative values is the same as for slices.
    print string.rfind(stra, 'w')  # Like find() but find the highest index.
    print string.index(stra, 'l')  ##Like find() but raise ValueError when the substring is not found.
    print string.rindex(stra, 'l')  # Like rfind() but raise ValueError when the substring is not found.
    print string.count(stra,
                       'o')  # Return the number of (non-overlapping) occurrences of substring sub in string s[start:end]. Defaults for start and end and interpretation of negative values are the same as for slices.
    print string.lower(stra)  # first char is lower h e l l o w o r l d
    print string.split(stra, 'o')  ##split the stra with condition 'o'

    print 1, string.capwords(stra)
    print 2, stra.isalpha()
    print 3, stra.replace("hello", "123")
    print 4, stra.strip()
    print 5, len(stra)


def operation():
    x = 111
    y = 3.3
    print 5 // 4
    print x, y, x + y, type(x), type(y)


def demo_buildinfunction():
    print 1, max(22, 11), min(111, 22)
    print 2, abs(-111)
    print 3, range(1, 10, 3)
    print 4, dir(list)
    x = 2
    print 6, eval("x + 3")
    print divmod(5, 4)  # get 5/4 and 5%4
    print type(x)
    print range(1, 10)
    list1 = range(1, 10)
    print enumerate(list1)
    for index, value in enumerate(list1):  ## for list add index attribute
        print index, ":", value
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    print zip(x, y, z)  ##[(1, 4, 7), (2, 5, 8), (3, 6, 9)] zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个由list组成的tuple列表
    a = [1, 2, 3, 4, 5, 6, ]
    b = {1: 11, 2: 22, 3: 33, 4: 44, 5: 555}
    for content in iter(b):  # 迭代字典的键
        print content
    for content in iter(a):  ##迭代不是序列但表现处序列行为的对象，例如字典的键、一个文件的行
        print content


def demo_controll():
    a = 10
    if a > 10:
        print "a > 10"
    else:
        print "a <= 10"
    for index in range(1, 10):
        print index
    for index in iter(range(1, 10)):
        print index
    while a >= 10:
        print "index ", a
        a = a - 1
    if a >= 9:
        pass
    else:
        print "a <=9 "


def demo_datastruct():
    list1 = [1, 2, 3, 4, 5]
    list1.append(100)
    print list1
    list2 = [6, 7, 8, 9, 10]
    list1.extend(list2)
    print list1


class User():
    type = "User"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return "i am " + self.name + "," + str(self.id)


class Admin(User):
    type = "Admin"

    def __init__(self, name, id, group):
        self.name = name
        self.id = id
        self.group = group

    def __repr__(self):
        return "i am " + self.name + "," + str(self.id) + "\tgroup" + self.group



def create_accout(type):
    if type == "user":
        return User(type, 1)
    elif type == "Admin":
        return Admin(type, 1, "home")
    else:
        return None


def demo_exception():
    try:
        print 2 / 0
        if type == "c":
            raise Exception('raise error', 'new project')
    except Exception, e:
        print "error:", e
    finally:
        print 'clean up'


def demo_random():
    random.seed(1)
    print 1, int(random.random() * 100)
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 10)
    a = [1, 2, 4, 5, 6, 7, 9]
    random.shuffle(a)
    print a
    print random._ceil(100.11)
    print random.gauss
def demo_regix():
    str1 = "mksmkd1991ooosps"
    pattern = re.compile("[\w]*91")
    print pattern.findall(str1)
    resl = re.match(pattern, str1)
    print resl.group()
    str2 = "232322@qq.com;ndsidns@sina.com;sddffs@intel.com;sadsooo@163.com;2323298884@163.com;92093293@qq.com"
    pattern2 = re.compile('^\d+@qq\.com')
    resl2 =  re.search(pattern2, str2)
    print resl2.group(1)
    # print pattern2.search(str2).group()


if __name__ == "__main__":
    # 这是注释第一种方式
    ''' 这是注释的第二种使用方式 

     '''
    # demo_string_format()
    # demo_string_func()
    # demo_buildinfunction()
    # demo_controll()
    # demo_datastruct()
    # print "hello world!"
    # User = create_accout("Admin")
    # print User
    # demo_exception()
    # demo_random()
    demo_regix()

