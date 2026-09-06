import os

FILE_NAME = 'money.txt' #создаем название файла, в который будут сохраняться все действия и данные пользователя

def add_operation(): #здесь мы добавляем операцию
    print("\n Выберите тип операции: ")
    print("1. Приход")
    print("2. Расход")
    
    choice = input("Ваш выбор (1 или 2): ")
    if choice == "1":
        type = "Приход"
    elif choice == "2":
        type = "Расход"
    else:
        print("Неверный выбор")
        return

    category = input("Введите категорию: ")
    try:
        amount = float(input("Введите сумму: "))
        if amount < 0:
            print("Сумма должна быть положительной")
            return
    except ValueError:
        print("Введена некорректная сумма")
        return

    # Сохраняем в файл
    with open(FILE_NAME, 'a', encoding='utf-8') as f:
        f.write(f"{type};{category};{amount}\n")
    print("Операция успешно сохранена")

def history(): #здесь смотрим историю операций
    if not os.path.exists(FILE_NAME):
        print("\n История пока пуста.")
        return

    print("\n История операций: ")
    with open(FILE_NAME, 'r', encoding='utf-8') as f: #тоже сохраняем данные
        for i, line in enumerate(f, 1):
            parts = line.strip().split(';')
            if len(parts) == 3:
                print(f"{i}. [{parts[0]}] Категория: {parts[1]} | Сумма: {parts[2]}")

def balance(): #проверяем баланс
    if not os.path.exists(FILE_NAME):
        print("\n Баланс: 0")
        return

    income = 0
    expense = 0

    with open(FILE_NAME, 'r', encoding='utf-8') as f: # здесь мы сохраняем все действия в файл
        for line in f:
            parts = line.strip().split(';')
            if len(parts) == 3:
                type, balance, amount = parts
                amount = float(amount)
                if type == 'Приход':
                    income += amount
                elif type == 'Расход':
                    expense += amount

    balance = income - expense
    
    print("\n Финансовый баланс: ")
    print(f"Общий доход: {income}")
    print(f"Общий расход: {expense}")
    print(f"Текущий остаток: {balance}")

def main(): #создаем кнопку меню
    while True:
        print("\n  MENU ")
        print("1. Добавить операцию")
        print("2. Посмотреть историю операций")
        print("3. Посчитать баланс")
        print("0. Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1': #создаем условия если пользователь выберет определнные действия
            add_operation()
        elif choice == '2':
            history()
        elif choice == '3':
            balance()
        elif choice == '0':
            print("До свидания ")
            break
        else:
            print("Неверный пункт меню. Попробуйте снова ")

if __name__ == "__main__":
    main()
