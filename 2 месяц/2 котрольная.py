class Book:
    def info(self,id,title,author,year,genre,pages,available):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.genre=genre
        self.pages=pages
        self.available=available
    def borrow(self,id,title,author,year,genre,pages,available):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.genre=genre
        self.pages=pages
        self.available=available
    def return_book(self,id,title,author,year,genre,pages,available):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.genre=genre
        self.pages=pages
        self.available=available
class User:
    def borrow_book(self,id,name,age:str,phone:str,borrowed_books:str):
        self.id=id
        self.__name=name
        self.age=age
        self.phone=phone
        self.borrowed_books=borrowed_books
    def return_book (self,id,name,age:str,phone:str,borrowed_books:str):
        self.id=id
        self.name=name
        self.age=age
        self.phone=phone
        self.borrowed_books=borrowed_books
    def info(self,id,name,age:str,phone:str,borrowed_books:str):
        self.id=id
        self.name=name
        self.age=age
        self.phone=phone
        self.borrowed_books=borrowed_books
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,new_phone:str):
        if isinstance (new_phone,str) and new_phone.startswith("+996"):
            self.__phone=new_phone
        else:
            print('Ошибка, ваш номер телефона должен начинаться с +996')
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age:str):
        if isinstance(new_age,str) and len (new_age)<10:
            self.__age=new_age
        else:
            print("Ошибка, возраст должен быть больше 10 лет")
    @property
    def borrowed_books(self):
        return self.__borrowed_books
    @borrowed_books.setter
    def borrowed_books (self,new_borrowed_books:str):
        if isinstance(new_borrowed_books, str) and new_borrowed_books>0:
            self.__borrowed_books=new_borrowed_books
        else:
            print("Ошибка, название книги не может быть пустой")


class Library:
    def add_book(self,books,users):
        self.books=books
        self.users=users
    def remove_book(self,books,users):
        self.books=books
        self.users=users
    def find_book(self,books,users):
        self.books=books
        self.users=users
    def register_book(self,books,users):
        self.books=books
        self.users=users
    def show_books(self,books,users):
        self.books=books
        self.users=users
    def show_users(self,books,users):
        self.books=books
        self.users=users
    def borrow_book(self,books,users):
        self.books=books
        self.users=users
    def return_book(self,books,users):
        self.books=books
        self.users=users
class Person:
    def info(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
class User(Person):
    def info(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
class Librarian(Person):
    def info(self,id,name,age,salary,position):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
        self.position=position
    def show_information(self,person):
        super().__init__(person)
        self.person=person
from abc import ABC,abstractmethod
class LibraryItem:
    @abstractmethod
    def take():
        return
    @abstractmethod
    def give_back():
        return
class Downloadable:
    def download():
        print("Вы успешно загрузили книгу")
class DigitalBook(Book,Downloadable):
    def downloaded_books():
        print("Вы просмотрели все загруженные книги")
    def __len__(self):
        return len(Library)
    def __eq__(self,other):
        if isinstance (other,Book):
            return self.book==other.book
class Validator():
    @staticmethod
    def validate_phone():
        return
    @staticmethod
    def validate_year():
        return
    @staticmethod
    def validate_pages():
        return

import sqlite3
conn=sqlite3.connect("books.db")
cursor=conn.cursor()
cursor.execute("""
    create table if not exists books(
        id integer primary key autoincrement,
        user_id integer,
        title text,
        author text,
        genre text,
        yeat integer,
        pages integer,
        available boolean,
        

    )
""")
cursor=conn.cursor()
cursor.execute("""
    create table if not exists users(
    id INTEGER PRIMARY KEY AUTOINCREMENT
    name text,
    age integer,
    phone text,
    
    )
""")
cursor=conn.cursor()
cursor.execute("""
    create table if not exists borrow_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT
    Auser_id integer
    book_id integer
    borrow_date text
    return_date text
    foreign key(user_id) references users(id)
    foreign key(book_id)references books(id)
    )
""")
while True:
    print("\n Для пользователей")
    print("1.")