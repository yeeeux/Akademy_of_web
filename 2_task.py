from random import randint

# Списки допустимых символов
letters = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

robot_list = []
letters_keys = [0, 4, 5]

# функция ввода значения количества точек. Не прекращается пока не будет введено валидное число.
def vvod_integer():
    vvod = True
    while vvod:
        try:
            return abs(int(input("Сколько сгенерировать случайных номеров?")))
        except ValueError:
            print("Введите целое число!")


def check_number(num):
    """
    Функция проверки номеров.
    :param num:
    На вход получает гос номер, который необходимо проверить на валидность
    :return:
    Возвращает номер, если с ним все ок. В противном случае выходит из функции
    """
    summ = 0
    if len(num) < 8 or len(num) > 9:
        return
    for i in range(len(num)):
        if i in letters_keys:
            if num[i] in letters:
                summ += 1
        else:
            if num[i] in digits:
                summ += 100
    if summ == 503 or summ == 603:
        return num


# В ручную забитые номера.
list_autos_numbers = ["А123АА11", "А222АА123", "А12А123", "А123СС1234", "АА123А12", "АА1А23А1А2", "ОС93МАХ1МУАА44"]

count = int(vvod_integer())


def gen_alphabet():
    """
    Функция генерации допустимых букв
    :return:
    Возвращает 1 букву
    """
    x = randint(0, 11)
    return letters[x]


def gen_digit():
    """
    Функция генерации цифр
    :return:
    Возвращает 1 цифру
    """
    x = randint(0, 9)
    return str(x)




for j in range(count):
    number = ""
    tumbler = randint(0, 1)
    # цикл генерации верных номеров
    if tumbler == 0:
        length = randint(8, 9)
        for i in range(length):
            if i in letters_keys:
                number += gen_alphabet()
            else:
                number += gen_digit()
    # цикл генерации неверных номеров
    else:
        length = randint(5, 15)
        for i in range(length):
            tumbler_2 = randint(0, 1)
            if tumbler_2 == 0:
                number += gen_alphabet()
            else:
                number += gen_digit()

    robot_list.append(number)
print("Были сгенерированы следующие номера:\n", robot_list,
      '\n они были добавлены к существуещему списку:\n',
      list_autos_numbers)

# Итоговый список номеров для проверки
list_autos_numbers += robot_list
print("Следующие номера являются правильными")
# Цикл проверки валидности номера:
for i in list_autos_numbers:
    if check_number(i) is not None:
        print(check_number(i))
