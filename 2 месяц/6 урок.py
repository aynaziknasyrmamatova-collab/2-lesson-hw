#субд система управления базами данных  , программа которая позволяет вносить правки,создавать, читать базы данных
#sql хранят информацию в виде связанных таблиц со строгой схемой использвуя язык скл
import sqlite3
"""
создать таблицу
CREATE TABLE

добавить данные
INSERT              create-c

получить данные
SELECT              read-r

изменять 
UPDATE              update-u

удалить
DELETE              delete-d

типы данных
integer-целое число
real-число с остатками
blob-фото медиа
text-текст
null-пустое значение
boolean-true and false
"""
import sqlite3
conn=sqlite3.connect("shop.db")
cursor=conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key autoincrement,
            name text,
            age integer
    )
""")
#execute добавляет данные 1 раз
cursor.execute(
    """
        insert into users(name,age)
        values(?,?)
    """,("Bob",20)
)
#здесь мы начинаем добавлять других пользователей
users=[
    ("Alice",20),
    ("Lack",32),
    ("Mila",21)
]
cursor.executemany(
    "insert into users(name,age)values (?,?)",
    users
)
cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("select * from users where id=1")
user=cursor.fetchone()
print(user)
#здесь мы наичнаем изменять возраст боба
cursor.execute(
    """
        update users
        set age=?
        where id=?

    """,
    (30,1)
)
#чтобы удалить какого либо пользователя необходимо:
cursor.execute(
    """
        delete from users
        where id=?
    """,
    (1,)
)
conn.commit()
conn.close()
