#задание 1

a=int(input("Введите первое любое число: "))
b=int(input("Введите второе любое число: "))
if a>b:
    print("Первое число больше")
elif b>a:
    print("Второе число больше")
elif a==b:
    print("Числа равны")
elif ab>0:
    print("Оба числа положительные")



#задание 2

number=int(input("Введите любое число: "))
min=1
max=10
if min <= number <= max:
    print("Число в диапазоне 1-10")
min=11
max=100
if min <= number <= max:
    print("Число в диапазоне 11-100")
else:
    print("Число вне диапазона")


#3 задание

name=(input("Введите свое имя: "))
min=5
max=8

# print(len(name))
if len(name) <5:
    print("Короткое имя")
elif min<= len(name) <= max:
    print("Среднее имя")
else:
    print("Длинное имя")

#4 задание

numbers=[7,3,15,2]
print(numbers[1])
print(numbers[3])
numbers=[2,3,15,7]
print(numbers)


#5 задание

number=int(input("Введите сумму покупки: "))
if number>5000:
    skidka=(10/100)*number
    print(skidka , '-ваш размер скидки')
    summa=number-skidka
    print(summa , '-ваша итоговая сумма')
elif number>2000:
    skidka2=(5/100)*number
    print (skidka2, "-ваша скидка" )
    summa2=number-skidka2
    print(summa2, "-ваша итоговая сумма" )
else:
    print("Скидки нет")



