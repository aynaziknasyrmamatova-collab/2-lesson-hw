
#for name in range (10):
 #   print("hello")

#students=["Petya","Jeremy","Elena"]
#for name in students:
   # print(f"Добро пожаловать, {students}")
#чтобы найти числа от 1 до 10
for i in range (1,11):
    print(i)

#чтобы найти чисел в обратную сторону
for i in range (10,0,-1):
    print(i)

#чтобы найти четные числа
for i in range(1,21):
    if i%2==0:
        print(i)


#чтобы посчитать сумму всех чисел:
n=0
for i in range(1,101):
    n+=i
    print(n)



number=int(input("Введите любое число: "))
n=0
for i in range(1,number):
    n+=i
    print(n)



b=int(input("Введите любое число: "))
n=0
for i in range (1,b):
    n**=i
    print(n)


