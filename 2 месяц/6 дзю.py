import sqlite3
conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key autoincrement,
            name text,
               age integer,
               adress TEXT,
               phone TEXT,
               date TEXT
    )
""")
conn.commit()



def create_patient(name,age,adress,phone,date):
    cursor.execute(
        "INSERT INTO patients(name,age,adress,phone,date) VALUES(?,?,?,"",?,?)",
        (name,age,phone,adress,date)
    )
conn.commit()
print("Пациент успешно добавлен")

def read():
    cursor.execute("SELECT *FROM patients")
    rows=cursor.fetchall()
    for row in rows:
        print(f"ID:{row[0]} Имя: {row[1]} Возраст:{row[2]} Адрес : {row[3]} Телефон: {row[4]} Дата : {row[5]}")

def update(patient_id,name,age,address,phone,date):
    cursor.execute("""
        UPDATE patients
        SET name=?,age=?,address=?,phone=?,date=?
        WHERE id=?
""",
    (name,age,address,phone,date,patient_id)
)
conn.commit()
print("Данные пациента обновлены")

def delete(patient_id):
    cursor.execute('DELETE FROM patients WHERE id=?',(patient_id))
    conn.commit()
    print("Пациент удален")
users=[
    ("Alice",20,"Main 2", 5467890,"24 июля"),
    ("Bob",50,"Namrin 3",33487340,"24 июля")
]
