#number=0

#while True:
    #number+=1
    #print(number)

# while true фраза будет делать цикл бесконечным чтобы его остановить необходимо ctrl c

#dictionary-словарь  данные хранятся в ключом и значении, {}скобки
students={"name":"Elya", "agge":"19"}
print(students["name"])
print(students["agge"])
students["hobby"]="football"
print(students)

students['name']= "Mary" 
print(students)

del students['age']

students.pop("hobby")
print(students.keys f)
#выводит только ключи


print(students.values{})
#выводит только значение


print(students.items{})
#выводит оба объекта

#set={} внутри объекта толлько 1 значение, изменяемый, не имеет индексов и определенного порядка, не имеет дубликата

students={"Nelya", "Goga", 'Bert'}
print(students)
#чтобы добавить:
students.add("Gensi")


#чтобы убрать,если в списке точно есть это значение:
students.remove("Goga")
print(students)


#если нету:
students.discard("Eka")


#frozenset неизменяемый, нельзя вносить правки , любые скобки главное написать frozenset
n=frozenset("frcf","ced")

#функции
#1- встроенные функции: print,min,max,len, встроены самими разработчиками
#2- искусственные функции (обычные функции) функции которые мы делаем сами
#3- анонимные функции
#чтобы создать функции надо сделать следующее:
def hec():
    print("Hello, babe")
hec()
#
#
#





