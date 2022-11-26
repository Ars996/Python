# Задание 1 Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

#import random

#n = int(input('Количество элементов списка: '))
#b1 = int(input('Граница 1 диапазона значений элементов списка: '))
#b2 = int(input('Граница 2 диапазона значений элементов списка: '))
#numbers_list = [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]
#import Func_list_generation as lg
#numbers_list = lg.list_generation()
#result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
#print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')

#Задание 2_1. Найти сумму чисел списка стоящих на нечетной позиции

import random

n = int(input('Количество элементов списка: '))
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
numbers_list = [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]
import Func_list_generation as lg
numbers_list = lg.list_generation()
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')