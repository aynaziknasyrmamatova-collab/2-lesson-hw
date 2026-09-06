
def hec ():
    num1=int(input("Введите первое число: "))
    num2=int(input("Введите второе число: "))
    print(num1+num2)
#чтобы вызвать функцию необходимо написать название функции и скобки добавить типо hec()
def info():
    name="Kendal"
    age=21
    print(f"Имя: (name), возраст: (age)")
def info(name,age):
    print(f"Имя: {name}, возраст: {age}")
info("Geeks",9)
info('Osh',30)

numbers=[1,2,3,4,5,6,7,8,9]

def qwe(number):
    if number%2==0:
        print("True")
    else:
        print("False")
qwe(6456)

def result(numbers):
    for i in numbers:
        print(1*2)

#lambda= анонимная функция пишется в одну строку, в данной функции из списка обычный цифры умножились на два
result_lambda= list(map(lambda i:i*2, numbers))
print(result_lambda)

result= lambda num1,num2:num1+num2
print(result(4,2)) # вот здесь после result мы всегда пишем те числа над которвми хотим произвести какую либо операцию

result= list(filter(lambda i:i%2==0, numbers)) #здесь мы находим четные числа
#filter - замена условия для цикла
print(result)
#map - выполняет работу цикла, обращается к каждому объекту
num1=85
print((lambda x:x*2)(num1))
