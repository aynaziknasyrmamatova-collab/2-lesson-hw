from datetime import datetime
def log_event(message):
    current_time= datetime.now().strftime("%%-%m-%d %H:%M:%S")
    with open("money.txt","a", encoding="utf-8") as file:
        file.write(f"[{current_time}]{message}\n")
while True:
    print("\n MENU")
    print("1. Добавить операцию")
    print("2. Посмотреть историю операций")
    print("3. Посчитать баланс")
    print("0. Выход")
    choice= input("\n Выберите действие: ")
    if choice=="1":
    
        print("\n Выберите тип операции")
        print("1. Приход")
        print("2. Расход")
        type= input("Ваш выбор (1 или 2): ")
    if type =="1":
        print("Приход")
        log_event("Пользователь выбрал приход")
    elif type=="2":
        print("Расход")
        log_event("Пользователь выбрал расход")
    else:
        print("Неверный выбор")
        log_event("Введена неверная комбинация")
        
    category=input("Введите категорию: ")
    try:
            amount=float(input("Введите сумму: "))
            if amount < 0:
                print("Сумма должна быть положительной")
                continue
    except ValueError:
          print("Пожалуйста введите правильное число")
    with open("money.txt", "a", encoding="utf-8") as file:
        file.write(f"{type}|{category}|{amount}\n")
        pass
    if choice=="2":
        print("Вот ваша история операций: ")
        log_event("Пользователь просмотрел историю операций")
    elif choice=="3":
        print("Ваша сумма расходов, а также доходов и текущий остаток денег: ")
        log_event("Пользователь посчитал баланс")
    else:
        print("Выход")
        log_event("Выход пользователя")
      