from datetime import datetime
def log_event(message):

print("1. Ввести текст")
print("2. Просмотр файлов")
print("3. Выход")
while True:
    
    choice=input("\n Выберите действие: ")
    if choice== "1":
        print("Вы ввели текст")
        log_event("Пользователь ввел текст")

    elif choice=='2':
        print("Вы просмотрели содержимое файлов")
        log_event("Пользователь вывел содержимое данных")

    elif choice=="3":
        print('Выйти')
        log_event("Пользователь завершил программу")
        break
    else:
        print(f"Неизвестная команда {choice}")
