class Student:
    def __init__(self, code, name, age, scores):
        self.code = code
        self.name = name
        self.age = age
        self.scores = scores

    def __str__(self):
        return '学号:{}, 姓名:{},年龄:{}, 分数:{}'.format(
            self.code,
            self.name,
            self.age,
            self.scores,
        )

class Teacher:
    def __init__(self, teachername):
        self.name = teachername

    def inputmenu(self):
        return int(input('选择菜单:'))

    def addstu(self, computer):
        code =int(input('请输入学生编号'))
        student = computer.showstu(code)
        if student == None:
            name = input('学生姓名')
            age = int(input('学生年龄'))
            scores = int(input('学生分数'))
            orginaziton = int(input('学生分组1-5'))
            newstudent = Student(code, name, age, scores)
            return newstudent, orginaziton

    def delstu(self):
        code = int(input('请输入学生编号'))
        return code

    def checkstuage(self):
        return int(input('输入年龄'))

    def  checkstuscores(self):
        n = int(input('上限'))
        m = int(input('下限'))
        return n, m

class Computer:

    listcomputer = []
    listmath = []
    listchinese = []
    liststar = []
    listpython = []
    listall=[listcomputer, listmath, listchinese, liststar, listpython]

    def __init__(self, teacher=None):
        self.teacher = teacher

    def computeraddstu(self):
        result = self.teacher.addstu(self)
        if result != None:
            self.listall[result[-1] - 1].append(result[0])
            print('添加成功')
        else:
            print('此人已经存在')
    def computerdelstu(self):
        code = self.teacher.delstu()
        result = self.showstu(code)
        if result == None:
            print('查无此人')
        else:
            self.listall[result[-1]].remove(result[0])
            print('删除成功')

    def computerprintstu(self):
        listclass = ['Computer', 'Math', 'Chinese', 'Star', 'Python']
        for i in range(5):
            for student in self.listall[i]:
                print(student, listclass[i])

    def showstu(self, code):
        for i in range(5):
            for student in self.listall[i]:
                if student.code == code:
                    return student, i

    def filterage(self):
        listclass = ['Computer', 'Math', 'Chinese', 'Star', 'Python']
        age = self.teacher.checkstuage()
        for i in range(5):
            for student in self.listall[i]:
                if student.age == age:
                    print(student, listclass[i])
        print('此年龄学生，无显示表示没有学生')


    def filterscores(self):
        listclass = ['Computer', 'Math', 'Chinese', 'Star', 'Python']
        filtersocre = self.teacher.checkstuscores()
        for i in range(5):
            for student in self.listall[i]:
                if filtersocre[0] < student.scores < filtersocre[-1]:
                    print(student, listclass[i])
        print('此成绩区间学生,无显示表示没学生')

    def showallscore(self):
        listclass = ['Computer', 'Math', 'Chinese', 'Star', 'Python']
        try:
            for i in range(5):
                allscores = 0
                n = 0
                for student in self.listall[i]:
                    allscores = allscores + student.scores
                    n = n + 1
                if n == 0:
                    continue
                print(listclass[i], allscores, allscores / n)
        except:
            print('除了已打印的组外，其他无学生')

    def showmenu(self):
        print('1增加学生')
        print('2删除学生')
        print('3打印学生信息')
        print('4显示小组总成绩及平均值')
        print('5筛选成绩')
        print('6筛选年龄')
        print('7退出')
        n = self.teacher.inputmenu()
        return n

    def poweron(self):

        while True:
            n = self.showmenu()
            if n == 1:
                self.computeraddstu()
            elif n == 2:
                self.computerdelstu()
            elif n == 3:
                self.computerprintstu()
            elif n == 4:
                self.showallscore()
            elif n == 5:
                self.filterscores()
            elif n == 6:
                self.filterage()
            elif n == 7:
                exit()


if __name__ == '__main__':
    lialoshi = Teacher('李老师')
    computer1 = Computer(lialoshi)
    computer1.poweron()