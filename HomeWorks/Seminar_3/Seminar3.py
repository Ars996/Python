# # Задайте список из нескольких чисел. Напишите программу, 
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# x = [2, 3, 6, 10, 12, 16, 5]
# #print(x)
# summ = 0
# for i in range(1, len(x), 2):
#     #if i % 2 == 1:
#         summ += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")

# # Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 6, 4, 3, 5]

# # if len(list)%2 == 0:
# #     size = len(list) // 2
# import math 
# size = math.ceil(len(list)/2)
# print(size)
# list2 = []
# for i in range(size):
#     list2.append(list[i]*list[-i - 1])
# print(list2)

# # Задайте список из вещественных чисел. Напишите программу, 
# # которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# # Пример:
# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# x = [1.1, 1.2, 3.1, 5, 10.01]
# x1 = []
# for i in range(len(x)):
#     if x[i] % 1 != 0:
#         x1.append(x[i])
# x2 = [round(x1[i] % 1, 2) for i in range(len(x1))]
# print(f"{x2} => {max(x2) - min(x2)}")

# # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# # Пример:
# # - 45 -> 101101
# # - 3 -> 11
# # - 2 -> 10

# x = int(input("Введите число:  "))
# print(bin(x)[2:])





# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 , 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#F−n = (−1)n+1 * Fn

# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1).

x = int(input("Введите число:  "))
y = []
y.insert(-1, 1)
y.insert(-2, -1)
# y[-1] = 1
# y[-2] = -1

for n in range(x-2, 1):
    n = -3
    y[n] = y[n+2] - y[n+1]   
    y.insert(n, y[n])
    n = n - 1
print(y)