number=int(input("Введите число: "))
if number>0:
    print("Положительное")
elif number<0:
    print("Отрицательное")
else:
    print("Середина")


number=int(input("Введите число: "))
if number%2==0:
    print("Четное")
else:
    print("Нечетное")
result= '3'
print(type(result))
result= ["Aynazik",31,21,3,False]
print(result)
#списки нужны для того чтобы не писать кучу тем, а просто добавить в список
#вместо name=1, name=inder, мы пишем с квадратными скобками
result= ["Aynazik", "Dan", "Leila"]
print (result)
# но если мы хотим вывести определенный объект из списка нам нужно писать так:
result=["Aynazik","Nelya","Caroline"]
print(result)
print(result[0])

#отсчет начинается с 0, то есть Айназик-0, Неля-1, и так далее

result.append ("Ken")
print(result)
# append нужен для добавления информации в список, только в конец


# а если мы хотим добавить в определенную часть то не обходимо использовать  insert
result.insert(1,"Adina")
print(result)
# а если мы хотим удалить объект,называя имя необходимо:
result.remove("Ken")
print(result)
#а если мы хотим удалить по индексу/цифре, то можно использовать следующую операцию:
result.pop(2)
print(result)


#а если хочешь отсортировать список необходимо:
result.sort()
print(result)
# а для того чтобв список перевернулся надо:
result.reverse()
print(result)

#но если лень искать индекс у данной, то можно использовать следующее:
print(result.index ("Caroline"))

list_result=['BMW','mercedes','hyundai','toyota']
print(list_result)

#срез списка

my_list = ['один', 'два', 'три', 'четыре', 'пять']
print(my_list[1:3])



tuple_result=('BMW','mercedes','hyundai','toyota')
print(tuple_result)

#отличие tuple,списки в том что в тьюпл нельзя изменять данные, а в списках можно
#также если мы ходим измерить длину кортежа, необходимо написать следующее:

print(len(result_tuple))

#а если необходимо вывести определнный элемент из кортежа, необходимо написать это, без запятой пишем!!!:

print(result_tuple [2])


#если надо найти определенный элемент в кортеже надо написать следующее:
result[2]


#нарезка кортежа с определлный элементов до других

data= ("лето", "осень", "зима", "весна")
data[0:3]


#преобразование кортежа в список

data = ('Лето', 'Зима', 'Осень', 'Весна')
list(data)

