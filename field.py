import sys
import math

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green', 'material': 'wool'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Кровать', 'price': 10000, 'color': 'white', 'material': 'wood'}
]

food = [
    {'title': 'Паста', 'price': 500, 'vegan': 'no', 'sauce': 'creamy'},
    {'title': 'Стейк', 'price': 2000, 'vegan': 'no',},
    {'title': 'Салат', 'price': 300, 'vegan': 'yes', 'weigh': '400g'}
]


# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(name, *args):
    empty = True
    if len(args) == 1:
        if type(name) == str:
            name = eval(name)
        for i in range(len(name)):
            for key, value in name[i].items():
                if key in args:
                    empty = False
                    yield(value)
        if empty:
            print('Нет полей в словаре с данными названиями!!')
    else:
        try:
            assert len(args) > 0
            if type(name) == str:
                name = eval(name)
            for i in range(len(name)):
                dict = {}
                for key, value in name[i].items():
                    if key in args:
                        empty = False
                        dict[key] = value
                if any(dict):
                    yield(dict)
            if empty:
                print('Нет полей в словаре с данными названиями!!')
        except AssertionError:
            print('\nВведите названия пунктов!')


    # Необходимо реализовать генератор

def main():
    name = input("Введите название библиотеки: ")
    while not name in globals():
        name = input("Такой библиотки не сущевует!\nВведите название библиотеки: ")
    args = []

    cur = input("Введите названия пункта: ")
    while cur:
        args.append(cur)
        cur = input("Введите названия пункта: ")
    result = field(name, *args)
    print(list(result))


if __name__ == "__main__":
    main()