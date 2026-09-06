#1 задание
student={"name": "Masha","age":"14", "group":"2", "ball": "4.34"}
print(student)
print(student["name"])
print(student["ball"])
#2 задание
tovar={"молоко":90, "хлеб": 50, "помидор": 120, "огурец": 80, "яблоко":60}
expensive=max(tovar,key=lambda x: tovar[x])
print("Самый дорогой товар: " ,expensive)
cheap=min(tovar, key=lambda x:tovar[x])
print("Самый дешевый товар: ", cheap)
number = sum(tovar.values()) / len(tovar)
print("Средняя цена товаров:",(number))
#3 задание
unique_words = set()  

print("Введите 5 слов: ")
for i in range(5):
    word = input(f"Слово {i + 1}: ")
    unique_words.add(word)
print("Уникальные слова:", ", ".join(unique_words))
print("Количество уникальных слов: ", len(unique_words))
#4 задание
a={1,2,3,4,5}
b={4,5,6,7,8}
elements = a & b 
print("Общие элементы:",elements)
print("Элементы, которые есть только в а: ",a)
print("Элементы, которые есть только в b:", b)
result = a | b
print("Объединение множеств: ", result)
#5 задание  
students_grades = {"Masha": [4,5,2], "Pasha": [2,3,5], "Kay": [3,2,4]}
for name, grades in students_grades.items():
    average = sum(grades) / len(grades)
    print(f"Студент: {name}  Средняя оценка: {average:.2f}")
#6задание
stroka = input("Введите строку: ")
rezultat = {}
for bukva in stroka:
    rezultat[bukva] = rezultat.get(bukva, 0) + 1
print(rezultat)
#7 задание
numbers=[1,2,2,3,4,4,5,6,6,7]
unique_numbers = list(set(numbers))
print(unique_numbers)
#8 задание
student1_subjects = {"Математика", "Физика", "Информатика", "Химия"}
student2_subjects = {"Физика", "Информатика", "История", "Литература"}
common_subjects = student1_subjects & student2_subjects
print("Одинаковые предметы:",common_subjects)
print(" Предметы первого студента : ",student1_subjects)
print("\n Предметы второго студента: ", student2_subjects)
 #9 задание
numbers = [2, 4, 6, 8]
result = list(map(lambda x: x**2, numbers))
print(result)
#10 задание
number = int(input("Введите число: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


