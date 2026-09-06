import sqlite3
conn=sqlite3.connect("admission.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    name TEXT,
    age INTEGER,
    city TEXT,
    major TEXT,
    countries TEXT

)
""")
conn.commit()
print("Database is ready!")
cursor.execute("""
CREATE TABLE IF NOT EXISTS universities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT,
    major TEXT,
    website TEXT
)
""")
conn.commit()
universities=[
    (
        "Stanford University",
        "USA",
        "Stanford",
        "Computer Science",
        "https://www.stanford.edu"
    ),
    (
        "University of Bologna",
        "Italy",
        "Bologna",
        "Computer Science",
        "https://www.unibo.it"

    ),
    (
        "Politecnio di Milano",
        "Italy",
        "Milan",
        "Engineering",
        "https://www.polimi.it"
    )
]

universities = [
    (
        "Stanford University",
        "USA",
        "Stanford",
        "Computer Science",
        "https://www.stanford.edu"
    ),
    (
        "University of Bologna",
        "Italy",
        "Bologna",
        "Computer Science",
        "https://www.unibo.it"
    ),
    (
        "Politecnico di Milano",
        "Italy",
        "Milan",
        "Engineering",
        "https://www.polimi.it"
    )
]
cursor.executemany("""
INSERT OR IGNORE INTO universities
(name, country, city, major, website)
VALUES (?,?,?,?,?)
""", universities)
conn.commit()
def save_user(telegram_id, name, age,city, major,countries):
    countries=",".join(countries)
    cursor.execute("""
        INSERT OR REPLACE INTO users
        (telegram_id, name, age,city, major, countries)
        VALUES (?,?,?,?,?,?)
    """, (telegram_id, name, age, city, major, countries))
    conn.commit()
def get_user(telegram_id):
    cursor.execute("""
        SELECT name,age,city,major,countries
        FROM users
        WHERE telegram_id=?
    """,(telegram_id,))
    return cursor.fetchone()
def search_university(name):
    cursor.execute("""
        SELECT name,country,city,major,website
        FROM universities
        WHERE name LIKE ?
    """,(f"%{name}%",))
    return cursor.fetchall()
def get_universities_by_country(country):
    cursor.execute("""
        SELECT name,country,city,major,website
        FROM universities
        WHERE country=?
    """,(country,))
    return cursor.fetchall()