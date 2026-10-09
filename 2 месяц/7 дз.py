import sqlite3
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        price INTEGER
    )
''')
cursor.execute('DELETE FROM orders')
initial_data = [
    (1, 'iPhone', 1000),
    (1, 'AirPods', 200),
    (2, 'Laptop', 1500),
    (2, 'Mouse', 50),
    (3, 'Keyboard', 120)
]
cursor.executemany('INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?)', initial_data)
conn.commit()

cursor.execute('DROP VIEW IF EXISTS expensive_orders')
cursor.execute('''
    CREATE VIEW expensive_orders AS  
    SELECT * FROM orders WHERE price > 500
''')
conn.commit()
#тут мы создаем view

print("Исходные данные в VIEW ")
cursor.execute('SELECT * FROM expensive_orders')
for row in cursor.fetchall():
    print(row)


cursor.execute('INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?)', (3, 'MacBook', 2500))
conn.commit()

print("\nVIEW после добавления MacBook")
cursor.execute('SELECT * FROM expensive_orders')
for row in cursor.fetchall():
    print(row)

cursor.execute('DROP VIEW expensive_orders')
conn.commit()
print("\nПроверка удаления VIEW")
try:
    cursor.execute('SELECT * FROM expensive_orders')
except Exception as e:
    print(f"Ошибка: Представление (VIEW) больше не существует. ({e})")
conn.close()
