def checkgoods(Dir):
    print(Dir)

def checkallgoods(Money, DirNum):
    print('商品价格：{}'.format(Dir))
    print('购物车商品数量：{} ,总价格为{}'.format(DirNum , Money))

def addgoods(DirNum):
    goods = input('派克，茶杯，毛巾，书，拖鞋')
    DirNum[goods] = DirNum[goods] + 1
    print('{}的数量为{}' .format(goods, DirNum[goods]))

def removegoods(DirNum):
    goods = input('派克，茶杯，毛巾，书，拖鞋')
    if DirNum[goods] == 0:
        print('此商品没有')
    else:
        DirNum[goods] = DirNum[goods] - 1
        print('{}的数量为{}'.format(goods, DirNum[goods]))

def checkin(DirNum , Money):
    if Money > 500:
        Money = Money - 50
    elif Money > 1000:
        Money = Money - 100
    print('商品价格：{}'.format(Dir))
    print('购物车商品数量：{} ,总价格为{}'.format(DirNum, Money))



def show():
    n = int(input('1查看商品信息\n'
              '2查看购物车信息\n'
              '3添加商品到购物车\n'
              '4移除购物车指定商品\n'
              '5结账'))
    return n


if __name__ == '__main__':
    Dir = {'派克': 200, '茶杯': 50, '毛巾': 20, '书': 20, '拖鞋': 10}
    DirNum = {'派克': 0, '茶杯': 0, '毛巾': 0, '书': 0, '拖鞋': 0}

    while 1:
        Money = Dir['派克'] * DirNum['派克'] + Dir['茶杯'] * DirNum['茶杯'] + Dir['毛巾'] * DirNum['毛巾'] + Dir[
            '书'] * DirNum['书'] + Dir['拖鞋'] * DirNum['拖鞋']
        Num = show()
        if Num == 1:
            checkgoods(Dir)
        elif Num == 2:
            checkallgoods(Money, DirNum)
        elif Num == 3:
            addgoods(DirNum)
        elif Num == 4:
            removegoods(DirNum)
        elif Num ==5:
            checkin(DirNum, Money)
            break
