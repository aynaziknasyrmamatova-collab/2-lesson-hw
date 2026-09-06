# #open (путь,режим) синтаксис
# file=open("data.txt")
# print(file) # чтобы потом вышел результат с этим файлом нужно написать сам файл data.txt
# file.close()
# # r-чтение
# # w-запись
# # a- дозапись
# # x- создать новый
# # b- бинарный
# # t- текстовый
# with open("data.txt") as file: #этот код мы написали чтобы вывести данные из файла
#     text=file.read()
# print(text)
# #file.close() вызывается автоматически
# with open("data.txt","r", encoding="utf-8") as file:
#     text=file.read()
# print(text)

# with open("data.txt","w", encoding="utf-8") as file:
#     file.write("Python \n")
#     file.write("Javascript \n")
#     file.write("C++ \n")

# with open("data.txt", "a", encoding="utf-8") as file:
#     file.write("HTML \n")
#     file.write("Design \n")
#     file.write("SMM \n")
       


# fraza="Каждый охотник желает знать где сидит фазан"
# with open("data.txt","w", encoding="utf-8")as file:
#     for i in fraza:
#         file.write(f"{i}\n")
# # таким образом мы написали данную фрвзу в файл

# #logs- директория в котором фиксируется или пишутся все события происходящие в той или иной системе

# with open("logs.txtt","a", encoding="utf-8")as file:
#     file.write("Пользователь вошел в систему")
#     #таким образом создается файл с информацией то что пользователь вошел в систему

from datetime import datetime

def log_event(message):
    current_time= datetime.now().strftime("%%-%m-%d %H:%M:%S")
    with open("logs.txt","a", encoding="utf-8") as file:
        file.write(f"[{current_time}]{message}\n")

while True:
    print("\n MENU")
    print("1. Войти")
    print("2. Зарегистрироваться")
    print("3. Создать заказ")
    print('4. Выйти из аккаунта')
    print("5. Завершить программу")

    choice= input("\n Выберите действие: ")

    if choice =="1":
        print("Пользователь успешно вошел в аккаунт")
        log_event("Пользователь вошел в систему")

    elif choice=="2":
        print("Новый пользователь зарегистрировался")
        log_event("Создан новый пользователь")

    elif choice=="3":
        print("Заказ успешно создан")
        log_event("Создан новый заказ")

    elif choice=="4":
        print("Вышел из аккаунта")
        log_event("Пользователь вышел из аккаунта")
        

    elif choice=="5":
        print('Выйти из системы')
        log_event("Сервер остановлен")
        break
    else:
        print("Неизвестная команда")
        log_event(f"Неизветсная команда{choice}")

        