import math


class TheVan:
    def __init__(self, price, goods):
        # Розмір фургону   100 < capacity < 200
        self.name = 'Фургон'
        self.price = price
        self.goods_list = goods

    def quality_sort(self, cost, goods_list):
        res = sorted(goods_list, key=lambda x: cost / x[2])
        print('------------------------------------------------------------------------------------')
        print('Результат сортування:')
        for i in res:
            lst = []
            for j in range(3):
                lst.append(i[j])
            print('Сорт кави:', lst[0], 'Стан:', lst[1], 'К-сть:', lst[2])
        print('------------------------------------------------------------------------------------')
        return res


class SmallVan(TheVan):
    def __init__(self, price, goods):
        TheVan.__init__(self, price, goods)
        self.name = 'Малий фургон'


class MediumVan(TheVan):
    def __init__(self, price, goods):
        TheVan.__init__(self, price, goods)
        self.name = 'Середній фургон'


class LargeVan(TheVan):
    def __init__(self, price, goods):
        TheVan.__init__(self, price, goods)
        self.name = 'Великий фургон'


def goods_maker(capacity, goods_list):
    capacity_list = [5, 5, 2, 1]
    sorts_list = ['Arabica', 'Canephora', 'Robusta', 'Bourbon']
    state_list = ['Зерно', 'Мелена', 'Розчинна в банках', 'Розчинна в пакетиках']
    cap = capacity

    while True:
        lst = []
        if cap == 0:
            print('У фургоні немає місця, завантаження неможливе!')
            break
        c = int(input('Виберіть дію:\n'
                      '1 -> Завантажити новий товар\n'
                      '0 -> Завершити загрузку\n'))
        if c == 1:
            c1 = int(input('Виберіть сорт:\n '
                           '1 -> Arabica\n '
                           '2 -> Canephora\n '
                           '3 -> Robusta\n '
                           '4 -> Bourbon\n'))
            lst.append(sorts_list[c1-1])
            c2 = int(input('Виберіть стан кави:\n'
                           ' 1 -> Зерно, обсяг: 5\n '
                           '2 -> Мелена, обсяг: 5\n '
                           '3 -> Розчинна в банках, обсяг: 2\n '
                           '4 -> Розчинна в пакетиках, обсяг: 1\n'))
            lst.append(state_list[c2-1])
            stat = capacity_list[c2-1]
            while True:
                c3 = int(input('Введіть к-сть товару:'))
                st = stat * c3
                if st > cap:
                    print('Недостатньо вільного місця у фургоні, можлива кількість: {}'.format(math.floor(cap/stat)))
                    continue
                else:
                    cap -= st
                    lst.append(st)
                    goods_list.append(lst)
                    print('Товар завантажено!\n Лишилось місця: {}'.format(cap))
                    break
            continue
        elif c == 0:
            print('Завантаження завершено!')
            break


def van_maker(c, van_size, weight):
    """van_size is str example - 'Малий фургон' """
    print('Ви вибрали - {}'.format(van_size))
    price = int(input("Ведіть ціну завантаженного товару: "))
    goods = []
    goods_maker(weight, goods)
    if c == 1:
        van = SmallVan(price, goods)
    elif c == 2:
        van = MediumVan(price, goods)
    else:
        van = LargeVan(price, goods)
    return van, goods, price


while True:
    try:
        c = int(input("1 -> Завантажити новий фургон\n"
                      "2 -> Провести сортування товарів на основі співвідношення ціни й ваги\n"
                      "3 -> Задати діапазон якості кави\n"
                      "0 -> Вихід\n"))
        if c == 1:
            c1 = int(input("Виберіть розмір фургона:\n"
                           "1 -> Малий фургон\n"
                           "2 -> Середній фургон\n"
                           "3 -> Великий фургон\n"))

            if c1 == 1:
                res = van_maker(c1, 'Малий фургон', 100)
                van = res[0]
                list_goods = res[1]
                cost = res[2]
            elif c1 == 2:
                res = van_maker(c1, 'Середній фургон', 150)
                van = res[0]
                list_goods = res[1]
                cost = res[2]
            elif c1 == 3:
                res = van_maker(c1, 'Великий фургон', 200)
                van = res[0]
                list_goods = res[1]
                cost = res[2]
            else:
                print("Ви вибрали неправильний номер!")

        elif c == 2:
            sorted_goods = van.quality_sort(cost, list_goods)

        elif c == 3:
            try:
                start = int(input("Початок діапазону: "))
                end = int(input("Кінець діапазону: "))
                for i in sorted_goods:
                    if (cost/i[2] > start and cost/i[2] < end):
                        print('Заданому діапазону відповідає сорт:', i[0], 'у стані:', i[1])
                    else:
                        print('Немає товару що відповідає заданому діапазону якості')
            except NameError:
                print('---Виконайте попередні дії!---')
        elif c == 0:
            break
    except ValueError:
        print("---Введіть коректний номер!---")

