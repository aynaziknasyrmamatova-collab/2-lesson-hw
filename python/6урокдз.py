# 1 задание,  для тго чтобы вывести количество введеных чисел
number=0
while True:
    a=int(input("Введите любое число: "))
    if a ==0:
        break
    number+=a
print("Итоговая сумма:", number)
#2 задание, пока пользователь не введет правильный ответ
c=0
while True:
    password=(input("Введите пароль: "))
    if password=="python123":
        break
print("Поздравляю с успешным входом")
#3 задание,  чтобы вывести ключи и значения из словаря
book={"name": "peppa", "author": "james", "year": "2012"}
print("Ключи: ")
print(list(book.keys()))
print("Значения словаря: ")
print(list(book.values()))
#4 задание чтобы изменить данные в словаря
student={"name": "Leila", "age": "15"}
student["group"]=10
student["age"]=16
student.pop("age")
print(student)
#5 задание для того чтобы вывести количество имен и пользователь вводит 10 имен
names=set()  
print("Введите 10 имен: ")
for i in range(10):
    name=input(f"Имя {i + 1}: ")
    names.add(name)
print("Количество уникальных имен: ", len(names))
#6 задание выводит количество студентов в обоих множествах
set1={"Маша", "Саша", "Миша", "Ваня"}
set2={"Саша", "Стеша", "Ваня", "Милана"}
students=set1&set2
print(students)
#7 задание проверять если есть какое либо данный
list=["Январь","Июнь", "Май", "Декабрь"]
months=frozenset(list)
june="Июнь" in months
print("Содержится ли июнь: ", june)
#8 задание добавляе м в оба множества данные
set={"dcdxsa", "32sdc", 'wxedxwd','3wedwxq'}
frozensett=frozenset(["dcdxsa", "32sdc", 'wxedxwd','3wedwxq'])
set.add(0)
print(set)
#frozenset.add(0)
#print(frozenset)
#но во frozenset невозможно делать изменения, и пайтон затем выдаст ошибку
# 9 задание создаем функцию где принимает число и возвращает в квадрат
def square(number):
    return number **2

#10 задание создаем функцию которая определяет если число четное
def is_even(number):
    if number%2==0:
        print("True")
    else:
        print("False")


