
# 数据类型

# str
# 定义：引号（单引号、双引号、三引号、三双引号）
# 区分：其他部分编程语言会认为单引号是代表字符

# C语言中：
# char c = 'c'
# char * s = "string"

s = 'hello'
s1 = "hello"
s2 = '''hello'''
s3 = """hello"""
# 区别：单引号和双引号不能换行；三引号可以换行

# 转义字符
print('\n')
# 原字符串  r R
print(r'\n')

print('hello', end='')
print('正方形边长：4\n 面积 ：4 * 4')

# 字符串拼接：
# 1、使用+，必须是str才可以
string1 = 'hello'
string2 = 'world'
string3 = string1 + string2
print(string3)

name = 'zhangsan'
age = 10
lesson = 'python'

print('我叫zhangsan,今年10岁, 学习python')
print('我叫' + name)
print('今年' + str(age) + '岁')
print('学习' + lesson)
print('我叫' + name + '今年' + str(age) + '岁' + '学习' + lesson)

# 2、格式化输出 %
print('我叫%s,今年%d岁, 学习%s' % (name, age, lesson))

# 3、format  推荐使用
des = '我叫{},今年{}岁, 学习{}'.format(name, age, lesson)
print(des)

print('我叫{},今年{}岁, 学习{}'.format(name, age, lesson))

# 详细使用format：
# {数字:特殊限制}
# {} 数据依次放入占位地方
# {数字} 选取数字对应的数据进行填充
print('我叫{1},今年{1}岁, 学习{1}'.format(name, age, lesson))

# {:对齐方式}
# {:填充字符>列宽}
# >< ^
print('{:*>10}'.format('hello'))

# {:.数字f}
print('{:.2f}'.format(1.91119999))
# 思考：其他数字限定？？？

# 二进制、八进制、十进制、十六进制。。。

print('=' * 22, 'input:')

# # input
# name = input('请输入名字:')
# print('您刚输入的名字为:', name)
# print(type(name))

# 备注:
# 1、input输入的数据需要接收
# 2、input输入的数据类型是str

# 练习：
# # 1、输入半径、显示圆周长及面积
# r = float(input('输入半径:'))
# pi = 3.14
# print('圆周长:', 2 * pi * r)
# print('圆面积:', pi * r ** 2)

# # 2、输入商品单价和数量，求商品总额
# price = float(input('输入商品单价:'))
# number = int(input('输入商品数量:'))
#
# print('商品总额:', price * number)
# 思考：input录入多个数据，并提取使用？？？
# 提示：tuple、 eval()  或者str分割

# int: 二进制(0b)、八进制(0O)、十进制、十六进制(0x)
print('=' * 22, 'int')

n = 99
n1 = 0b1011
print(n1)
n2 = 11
print('{:b}'.format(n2))
n3 = 23
print('{:o}'.format(n3))
print('{:x}'.format(n3))
print('{:x}'.format(30))

# 运算符：
# 复合赋值运算符
# +=  -=  *=  /=  **= //= %=
n = 10
n = n + 10
# n += 10
n = 20
n **= 2
print(n)
n = 400
n %= 2




