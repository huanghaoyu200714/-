
def calscore(menu, s):
    keys = tuple(s.keys())
    key = keys[menu - 1]
    name= input('请输入姓名')
    score = int(input('请输入学生的{}成绩:'.format(key)))
    s[key].append(score)
    print('当前{}成绩:{}'.format(key, score))
    return name, score

def showmenu():
    print('1、输入语文成绩:')
    print('2、输入数学成绩:')
    print('3、输入英语成绩:')
    print('4、显示所有成绩')
    print('5、退出')
    menu = int(input('请选择:'))
    return menu


if __name__ == '__main__':
    scores = {'语文': [], '数学': [], '英语': []}
    List1= []
    List2= []
    while True:
        n = showmenu()
        if 1 <= n <= 3:
            Nameandscore= calscore(n, scores)
            List1.append(Nameandscore[0])
            List2.append(Nameandscore[1])
        elif n == 4:
            for i in range(len(List1)):
                print('姓名：{}' .format(List1[i]))
                print('分数：{}' .format(List2[i]))
        elif n == 5:
            break