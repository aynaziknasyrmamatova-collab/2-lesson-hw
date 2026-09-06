#задание 1
n1
if number>100:
    print("Большое число")
elif number<100:
    print("Маленькое число")
elif number==100:
    print("Ровно 100")
#задание 2
age=int(input("Введите свой возраст: "))
if age<18:
    print("Несовершеннолетний")
else:
    print("Совершеннолетний")

#задание 3
number=int(input("Введите любое число: "))
if number%3==0:
    print("Делится на 3 ")
else: 
    print("Не делится на 3")


#задание 4
result=["Хатико", "Человек-паук", "Мстители", "Гадкий я", "Дневник памяти"]
print(result)
print(result[0])
print(result[4])


#задание 5

result=["Москва", "Бишкек", "Ош"]
result.insert (1,"Париж")
print(result)


#задание 6

numbers=[10,20,30,40,50]
numbers.remove (30)
numbers.pop(3)
print(result)

#задание 7

names= ["Nurbolot", "Islam", "Adina", "Beksultan"]
names.sort()
names.reverse()
print(names)


#задание 8



color_tuple=("red","blue","green","yellow","white")
len(color_tuple)
print( color_tuple [2])
print(len(color_tuple))


#задание 9

a=int(input("Введите первое любое число: "))
b=int(input("Введите любое второе число: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)


#задание 10


number=int(input("Введите число от 1 до 7: "))
if number==1:
    print("Понедельник")
elif number==2:
    print("Вторник")
elif number==3:
    print("Среда")
elif number==4:
    print("Четверг")
elif number==5:
    print("Пятница")
elif number==6:
    print("Суббота")
elif number==7:
    print("Воскресенье")
else:
    print("Ошибка")


