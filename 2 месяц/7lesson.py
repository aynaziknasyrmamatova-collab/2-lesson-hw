#for in key позволяет связать две таблицы в одну
#cursor нужен для того чтобы управлять базу данных
# есть 3 вида связывния таблиц 1-1 к 1, 1 к многим- когда несколько товаров привязываются к одному юзеру, многие к многим- один студент может прлходить много курсов, один курс проходят много студентов
# агреационная функция- вспомогательная функция,
# count function - считает количество
# sum function-пределяет всю сумму, суммирует
import sqlite3
conn=sqlite3.connect("shohp.db")
cursor=conn.cursor()
cursor.execute("""
    create table if not exists users(
        id integer primary key autoincrement,
        name,text,
        age integer
    )
""")
cursor.execute("""
    create table if not exists orders(
        id integer primary key autoincrement,
        user_id integer,
        product text,
        price integer,
        foreign key(user_id) references users(Id)

    )
""")
users=[
    ('Bob',20),
    ("Alice",18),
    ("Lauren",34)
]
cursor.executemany(
    "INSERT INTO users (name,age) VALUES (?,?)",
    users
)
orders=[
    (1,"hamburger",300),
    (1,"Cheesecake",200),
    (2,'coke',80),
    (2,"Sandwich",150),
    (3,"fried wings",400)
]
cursor.executemany(
    "INSERT INTO orders (user_id,product,price) VALUES (?,?,?)",
    orders
)
cursor.execute("SELECT  * FROM users")
print(cursor.fetchall())
#inner join показывает пользователей с заказами
#left join показывает пользователей без заказов
cursor.execute("""
    SELECT users.name,
            orders.product,
            orders.price
    FROM users
    INNER JOIN orders
    ON users.id = orders.user_id
""")
for row in cursor.fetchall():
    print(row)
cursor.execute("""
    insert into users(name,age)
    values("Jimmy",25)
""")
cursor.execute("""
    select users.name,
            orders.product
    from users
    left join orders
    on users.id=orders.user_id
""")
for row in cursor:
    print(row)

#находим сумму
cursor.execute("""
    select sum(price) from orders
""")
print(cursor.fetchall()[0])

#находим среднюю стоимость
cursor.execute("""
    select avg(price) from orders
""")
print(cursor.fetchall()[0])


#находим значение max
cursor.execute("""
    select max(price) from orders
""")
print("Max: ",cursor.fetchall()[0])

#находим значение min
cursor.execute("""
    select min(price) from orders
""")
print("Min: ",cursor.fetchall()[0])

#здесь мы искали общую сумму  заказа для юзера
cursor.execute("""
    select
        users.name,
        sum(orders.price)
    from users
    join orders
    on users.id = orders.user_id
    group by users.name
""")
for row in cursor.fetchall():
    print(row)


#тут мы ищем самый дорогой продукт, а также у нас тут вложенные функции,то есть функции внутри функции
cursor.execute("""
    select name
    from users
    where id=(
        select user_id from orders
        where price =(
            select max(price)
            from orders
        )
    )
""")
print(cursor.fetchone())


conn.commit()
conn.close()

#create view предоставляет виртуальную таблицу которая представлет собой сохраненный под именем select запрос
#позволяет спрятать огромные запросы под одним именем
#