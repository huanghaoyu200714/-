class Goods:
    def __init__(self, code, name, price, number):
        self.code = code
        self.name = name
        self.price = price
        self.number = number

    def __str__(self):
        return '{} {} {} {}' .format(self.code, self.name, self.price, self.number)


class Store:
    list0 = []
    list1 = []
    list2 = []
    list3 = []

    def addgoods(self):
        code = input('输入编号')
        name = input('输入名称')
        price = input('输入价格')
        number = input('输入数量')
        goods = Goods(code, name, price, number)
        temp = str(goods).split()
        if temp[0] not in self.list0 and temp[1] not in self.list1:
            self.list0.append(temp[0])
            self.list1.append(temp[1])
            self.list2.append(temp[2])
            self.list3.append(temp[3])
            print('完成录入')
        else:
            if temp[1] == self.list1[self.list0.index(temp[0])] and temp[2] == self.list2[self.list0.index(temp[0])]:
                self.list3[self.list0.index(temp[0])] = int(self.list3[self.list0.index(temp[0])]) + int(number)
                print('完成录入')
            else:
                print('错误')
                self.addgoods()


    def showtotalprice(self):
        numall = 0
        for i in range(len(self.list0)):
           numall = numall + int(self.list2[i]) * int(self.list3[i])
        print(numall)

    def sell(self):
        n = input('请输入编号')
        m = input('数量')
        if n not in self.list0 or int(self.list3[self.list0.index(n)]) < int(m):
            print('没有此商品或者数量不够')
            self.sell()
        else:
            self.list3[self.list0.index(n)] = int(self.list3[self.list0.index(n)]) - int(m)
            print('卖出成功')

    def updateprice(self):
        n = input('请输入编号')
        m = input('请输入价格')
        if n not in self.list0 or int(m) <= 0:
            print('没有此商品或价格错误')
            self.updateprice()
        else:
            self.list2[self.list0.index(n)] = m

    def showallgoods(self):
        if self.list3 == [] or self.list3.count(0) == len(self.list3):
            print('无商品')
        else:
            for i in self.list3:
                if i != 0:
                    print(self.list1[self.list3.index(i)], end=(' '))

    def show(self):
        while 1:
            print('输入1录入')
            print('输入2查看总价格')
            print('输入3卖出商品')
            print('输入4修改价格')
            print('输入5查看商店所有商品')
            print('输入6退出')
            n = int(input('输入一个数字'))
            if n == 1:
                self.addgoods()
                print()
            elif n == 2:
                self.showtotalprice()
                print()
            elif n == 3:
                self.sell()
                print()
            elif n == 4:
                self.updateprice()
                print()
            elif n == 5:
                self.showallgoods()
                print()
            elif n == 6:
                exit()


if __name__ == '__main__':
    Storeelse = Store()
    Storeelse.show()



