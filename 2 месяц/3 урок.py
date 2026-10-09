class BankAccount:
    def __init__(self):
        self.__balance = 1000 
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(500)
print(account.get_balance()) 
class User:
    def __init__(self):
        self.__age=18
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value >=0:
            self.__age=value
user=User()
user.age=25
print(user.age)

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod 
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Гав")
class Cat(Animal):
    def sound(self):
        print("Мяу")
dog=Dog()
dog.sound()
cat=Cat()
cat.sound()

from abc import ABC, abstractmethod
class Employer(ABC):
    @abstractmethod
    def work(self):
        pass
class Name(Employer):
    def work(self):
        print("Рабочий-Миша")
class Salary(Employer):
    def work(self):
        print('зарплату получает')
name=Name()
name.work()
salary=Salary()
salary.work()

class Salary(Employer):
    def __init__(self):
        self.__salary=40000
        @property
        def salary(self):
            return self.__salary
        @salary.setter
        def salary(self,value):
            if value<0:
                self.__salary=value
user=User()
user.salary= 90000
print(user.salary)

class Property():
    def __init__(self):
        pass
class Programmer(Property):
    def work(self):
        print("программируют,создают сайты и приложения")
class Designer (Property):
    def work(self):
        print("создают дизайны")
class Manager(Property):
    def work(self):
        print("следят за качеством работы")
manager=Manager()
manager.work()
designer=Designer()
designer.work()
manager=Manager()
manager.work()
workers=["Lisa","Mark","Bethany","Mark"]
salary=60000
print("Lisa- ", salary)

