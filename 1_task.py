from random import randint
from math import *


def funcsort(x):
    """
    Функция сортировки точек по величине угла
    :param x:
    :return:
    Начинает сортировку с точки, которая находится ближе к оси Y в 1 координатной четверти
    """
    if x >= ungle:
        return x
    else:
        return x + 1000


def gen_random(a, b):
    """
    Функция генерации рандомных чисел
    a и b параметр диапазона генерации чисел
    :return:
    x - рандомное число
    y - рандомное число
    """
    x = randint(a, b)
    y = randint(a, b)
    return x, y


# цикл ввода значения количества точек. Не прекращается пока не будет введено валидное число.
vvod = True
while vvod:
    try:
        n = abs(int(input("Введите размер списка точек:")))
        vvod = False
    except ValueError:
        print("Введите целое число!")
# словари, координат, расстояний от точки 0,0, углов в градусах
dictionary_values = {}
dictionary_length = {}
dictionary_rad = {}
# цикл генерации рандомных чисел, определения длины от точки 0:0 до точки,
# определения угла до точки.
for i in range(n):
    dictionary_values.update({i: gen_random(-100, 100)})
    sqrtt = round(hypot((dictionary_values[i][0]), (dictionary_values[i][1])), 5)
    degree = round(degrees(atan2((dictionary_values[i][1]), (dictionary_values[i][0]))), 5)
    dictionary_length.update({i: sqrtt})
    dictionary_rad.update({i: degree})

# цикл поиска точки в 1 четверти, ближайшей к оси Y
point_min=101
for i in range(n):
    if ((dictionary_values[i][0])>0 and (dictionary_values[i][1])>0):
        if (dictionary_values[i][0])<=point_min:
            point_min = (dictionary_values[i][0])
            key_point_min=i
# Назначение угла, с которого будет начинаться обход

try:
    ungle=dictionary_rad[key_point_min]
except NameError:
    ungle=90

# Вывод точек и их координат
print(dictionary_values)

# Сортировка значений словаря с углами, по функции funcsort
sort_values = (sorted(dictionary_rad.values(), key=funcsort))
# Определение координат точек по отсортированному списку.
sort_dictionary = {}
for i in range(len(sort_values)):
    for k in dictionary_rad.keys():
        if dictionary_rad[k] == sort_values[i]:
            sort_dictionary.update({k: sort_values[i]})
# Вывод отсортированных точек и координат
for i in sort_dictionary.keys():
    print(f"Точка №{i}, координаты:", dictionary_values[i])
# Определение номеров точек с максимальным и минимальными значениями отдаления от 0:0
key_max = max(dictionary_length, key=dictionary_length.get)
key_min = min(dictionary_length, key=dictionary_length.get)
# Определение среднего значения отдаления
average_length = sum(dictionary_length.values()) / len(dictionary_length.values())
# Вывод результатов
print(f"Максимальное расстояние точки # {key_max} от центра с координатами{dictionary_values[key_max]}, длина",
      dictionary_length[key_max])
print(f"Минимальное расстояние точки # {key_min} от центра с координатами{dictionary_values[key_min]}, длина",
      dictionary_length[key_min])
print(f"Среднее расстояние точек от центра", average_length)
