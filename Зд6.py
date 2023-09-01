# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.
# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# def func(first_num: int, step: int, num_elem: int) -> list:
#     list_1 = []
#     list_1.append(first_num)
#     count = first_num
#     for idx, elem in enumerate (list_1):
#         elem = count + step
#         count = elem
#         list_1.append(count)
#         if idx > (num_elem-3):
#             break
#     return list_1
# print(func(7, 2, 5))
# print(func(2, 3, 12))

# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# def func(lst1: list, min_range: int, max_range: int) -> list:
#     lst2 = []
#     lst3 = []
#     tuple1 = []
#     for idx, elem in enumerate(lst1):
#         if lst1[idx] >= min_range and lst1[idx] <= max_range:
#             lst2.append(idx)
#             lst3.append(elem)
#             tuple1 = list(zip(lst2, lst3))
#     return  tuple1  
# print(func(lst1, 2, 10))
# print(func(lst1, 2, 9))
# print(func(lst1, 0, 6))

#Усложнение *
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# def func(lst1: list, min_range: int, max_range: int) -> list:
#     lst2 = [idx for idx, elem in enumerate(lst1) if lst1[idx] >= min_range and lst1[idx] <= max_range]
#     return lst2
# print(func(lst1, 2, 10))
# print(func(lst1, 2, 9))
# print(func(lst1, 0, 6))


# (**) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# def func(lst1: list, min_range: int, max_range: int) -> list:
#     lst2 = []
#     lst3 = []
#     tuple1 = []
#     for idx, elem in enumerate(lst1):
#         if lst1[idx] >= min_range and lst1[idx] <= max_range:
#             lst2.append(idx)
#             lst3.append(elem)
#             tuple1 = list(zip(lst2, lst3))
#     return  tuple1  
# print(func(lst1, 2, 10))
