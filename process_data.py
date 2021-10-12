import json
import sys
from field import field
from sort import sort
from unique import Unique
from genRandom import genRandom
from printResult import print_result
from cmTimer import cm_timer_2
# Сделаем другие необходимые импорты


data = [
    {'name': 'Программист лол', 'old': '12'},
    {'name': 'программист лол', 'old': '12'},
    {'name': 'Писатель', 'old': '12'},
    {'name': 'Программист 2', 'old': '12'}
]

"""path = data_light.json.html
"""
# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

"""with open(path) as f:
    data = json.load(f)"""

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return(list(sorted([element for element in Unique(field(arg, 'name'), ignore_case=True)])))

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' со знанием Python', arg))

@print_result
def f4(arg):
    pay = list(genRandom(len(arg), 100000, 200000))
    strings = ['зарплата {} рублей'.format(i) for i in pay]
    return list(zip(arg, strings))


if __name__ == '__main__':
    with cm_timer_2():
        f4(f3(f2(f1(data))))