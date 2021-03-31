from random import randint

letters=["А","В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У" , "Х"]
digits=["1","2","3", "4", "5", "6", "7", "8", "9", "0"]

def check_number(num):
    summ=0
    if len(num) <8 or len(num)>9:
        summ=0
    letters_keys=[0,4,5]
    for i in range(len(num)):
        if i in letters_keys:
            if num[i] in letters:
                summ+=1
        else:
            if num[i] in digits:
                summ+=100
    if summ == 503 or summ == 603:
        return num




list_autos_numbers=["А123АА11","А222АА123","А12А123","А123СС1234","АА123А12","АА1А23А1А2"]


count=int(input("Сколько сгенерировать случайных номеров?"))


def gen_alphabet():
    x=randint(0,11)
    return letters[x]
def gen_digit():
    x=randint(0,9)
    return str(x)
robot_list=[]

letters_keys=[0,4,5]
# генерация верных номеров
for j in range(count):
    number=""
    tumbler=randint(0,1)
    if tumbler==0:
        length=randint(8,9)
        for i in range(length):
            if i in letters_keys:
                number+=gen_alphabet()
            else:
                number+=gen_digit()
    else:
        length=randint(5,15)
        for i in range(length):
            tumbler_2=randint(0,1)
            if tumbler_2 ==0:
                number+=gen_alphabet()
            else:
                number+=gen_digit()

    robot_list.append(number)
print("Были сгенерированы следующие номера:\n", robot_list,
      '\n они были добавлены к существуещему списку:\n',
      list_autos_numbers)

list_autos_numbers+=robot_list
print("Следующие номера являются правильными")
for i in list_autos_numbers:
    if check_number(i)!=None:
        print(check_number(i))
