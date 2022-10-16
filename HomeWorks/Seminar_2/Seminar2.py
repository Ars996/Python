Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


x = input('Введите число ')

def summa(x):                            #Функция нахождения суммы чисел в заданном числе
    if float(x) < 0:                            #Проверка на знак перед числом
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(x)}')

# float_num = input('input float number: ')

# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# x =float(0.25 % 0.04)
# print(round((x), 2))

#  if x > 1 or x < -1:
#         while x != 0:                        #Нахождение суммы
#             number = x % 10 + number
#             x = int(x / 10)
#     elif x < 1 and x > -1:
#         while x != '.':
#             number +=  int
#     return number


# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# # Пример:

# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# N = int(input('Введите число '))

# f = 1
# for i in range(N):
#     i = i + 1
#     f = i * f
    
#     print(f, end=" ")




# # 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.


# n = int(input('Введите количество чисел в списке '))

# def numbers(n):
#     summ = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1} '))
#         a = (1+1/a)**a
#         summ = a + summ
#         i += 1
#     return summ

# print('Сумма чисел равна',round((numbers(n)), 2))   


# # 4.(ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# #  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# from random import Random, randint


# N = int(input('Введите число'))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N,N+1))
    
# print(numbers)
# print(numbers[1] * numbers[3])

# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите позицию для вычисления - ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)

# # 5. Реализуйте алгоритм перемешивания списка.

# from random import Random, randint

# N = int(input('Введите число '))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N,N+1))
# print(numbers)

# def smes(numbers):
#     list = numbers[:]
#     numbers_length = len(list)
#     for i in range(numbers_length):
#         index = randint(0, numbers_length - 1)
#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list
# print(smes(numbers))