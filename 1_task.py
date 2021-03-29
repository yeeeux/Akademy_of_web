from random import randint

from math import *
def funcSort(x):
    if x>90:
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
    # if (dictionary_values[i][0])>0:
spisok=[]
for i in dictionary_rad.values():
    spisok.append(i)

print(dictionary_values)
print(dictionary_length)

print(dictionary_rad)
print(sorted(spisok, key=funcSort))


