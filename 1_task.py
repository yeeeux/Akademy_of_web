from random import randint

from math import *
def funcSort(x):
    if x>89.9:
        return x
    else:
        return x+1000


def gen_random(a,b):
    """
    Функция генерации рандомных чисел
    a и b параметр диапазона генерации чисел
    :return:
    x - рандомное число
    y - рандомное число
    """
    x = randint(a,b)
    y = randint(a,b)
    return x,y

vvod=True
while vvod:
    try:
        n=int(input("Введите размер списка точек:"))
        vvod=False
    except:
        print("Введите целое число!")

dictionary_values={}
dictionary_length={}

dictionary_rad={}
for i in range(n):
    dictionary_values.update({i:gen_random(-100,100)})
    sqrtt=round(hypot((dictionary_values[i][0]),(dictionary_values[i][1])),5)
    degree=round(degrees(atan2((dictionary_values[i][1]),(dictionary_values[i][0]))),5)
    dictionary_length.update({i:sqrtt})

    dictionary_rad.update({i:degree})
print(dictionary_values)
sort_values=(sorted(dictionary_rad.values(), key=funcSort))

sort_dictionary={}
for i in range(len(sort_values)):

    for k in dictionary_rad.keys():

        if dictionary_rad[k]==sort_values[i]:
            sort_dictionary.update({k:sort_values[i]})
for i in sort_dictionary.keys():
    print(f"Точка №{i}, координаты:",dictionary_values[i])
max=0
min=dictionary_length[0]
average=0
for i in dictionary_length.keys():
    average+=dictionary_length[i]
    if dictionary_length[i]>max:
        max=dictionary_length[i]
        k=i
    if dictionary_length[i]<min:
        min=dictionary_length[i]
        j=i
average=average/n
print(f"Максимальное расстояние точки # {k} от центра с координатами{dictionary_values[k]}, длина",  max)
print(f"Минимальное расстояние точки # {j} от центра с координатами{dictionary_values[j]}, длина",  min)
print(f"Среднее расстояние точек от центра",  average)
