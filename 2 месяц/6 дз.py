import sqlite3
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    address TEXT,
    phone TEXT,
    date TEXT
)
""")
conn.commit()
def add_patient():
  print("\nРегистрация нового пациента")
  name = input("Введите ФИО: ")
  age = int(input("Введите возраст: "))
  address = input("Введите адрес: ")
  phone = input("Введите телефон: ")
  date = input("Введите дату: ")

  cursor.execute(
      """
        INSERT INTO patients (name, age, address, phone, date) 
        VALUES (?, ?, ?, ?, ?)
    """,
      (name, age, address, phone, date),
  )
  conn.commit()
  print(f" Пациент {name} успешно добавлен в базу данных")

def show_table():
  cursor.execute("SELECT * FROM patients")
  rows = cursor.fetchall() 

  if not rows:
    print("\n Таблица пуста")
    return

  print("\n" + "=" * 90)
  print(
      f"{'ID':<4} | {'ФИО':<25} | {'Возраст':<7} | {'Адрес':<20} |"
      f" {'Телефон':<13} | {'Дата':<10}"
  )
  print("=" * 90)

  for row in rows:
    print(
        f"{row[0]:<4} | {row[1]:<25} | {row[2]:<7} | {row[3]:<20} |"
        f" {row[4]:<13} | {row[5]:<10}"
    )
  print("=" * 90)


def update_patient():
  show_table()
  patient_id = input(
      "\nВведите ID пациента, данные которого нужно изменить: "
  )

  cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
  if not cursor.fetchone():
    print(" Пациент с таким ID не найден!")
    return

  print("Введите данные:")
  name = input("Новое ФИО: ")
  age = int(input("Новый возраст: "))
  address = input("Новый адрес: ")
  phone = input("Новый телефон: ")
  date = input("Новая дата: ")

  cursor.execute(
      """
        UPDATE patients 
        SET name = ?, age = ?, address = ?, phone = ?, date = ? 
        WHERE id = ?
    """,
      (name, age, address, phone, date, patient_id),
  )
  conn.commit()
  print(" Данные успешно обновлены")

def delete_patient():
  show_table()
  patient_id = input("\nВведите ID пациента для УДАЛЕНИЯ: ")

  cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
  conn.commit()
  print(" Пациент успешно удален из базы данных")

while True:
  print("\n  БОЛЬНИЦA:")
  print("1. Добавить пациента ")
  print("2. Показать таблицу пациентов ")
  print("3. Изменить данные пациента ")
  print("4. Удалить пациента")
  print("5. Выйти")

  choice = input("Выберите действие (1-5): ")

  if choice == "1":
    add_patient()
  elif choice == "2":
    show_table()
  elif choice == "3":
    update_patient()
  elif choice == "4":
    delete_patient()
  elif choice == "5":
    conn.close()  
    print("До свидания ")
    break
  else:
    print("Ошибка")
