class BankAccount:
    def __init__(self,balance=0.0):
        self.balance=float(balance)
    def deposit(self,amount):
        if self.valid(amount):
            self.balance+=amount
            print(f"Счет поплнен на {amount}. Текущий баланс: {self.balance}")
    def withdraw(self,amount):
        if not BankAccount.valid(amount):
            return
        if amount>self.balance:
            print("Ошибка")
        else:
            self.balance-=amount
            print(f"Со счета снято {amount}. Текущий баланс: {self.balance}")
    def __str__(self):
        return (f"BankaAcount: Баланс= {self.balance}")
    def __add__(self,other):
        if isinstance(other,BankAccount):
            return BankAccount(self.balance+other.balance)
        return NotImplemented
    @staticmethod
    def valid(amount):
        if isinstance(amount,(int, float)) and amount>0:
            return True
        print("Ошибка")
        return False
    @classmethod
    def create(cls):
        return cls(1000)
account1= BankAccount.create()
print(account1)
account2=BankAccount(500)
account2.deposit(200)
total=account1+account2
print(total)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age} лет"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
    @staticmethod
    def is_adult(age):
        return age >= 18
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"{super().__str__()}, Студент (ID: {self.student_id})"
class Teacher(Person):
    """Класс преподавателя, наследуется от Person."""
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()}, Преподаватель (Предмет: {self.subject})"
class Researcher:
    """Класс исследователя."""
    def research(self):
        return "Проводит научное исследование"


class Assistant(Student, Researcher):
    @classmethod
    def create_junior_assistant(cls, name, age):
        return cls(name, age, "0000")

    def __str__(self):
        return f"Ассистент: {self.name}, Возраст: {self.age}, ID: {self.student_id}"

print(" Создание объектов")
p1 = Person("Маша", 25)
p2 = Person("Маша", 25)
student = Student("Иван", 20, "9889800")
teacher = Teacher("Алексей Петрович", 45, "Физика")
assistant = Assistant.create_junior_assistant("Мария", 22)

print(p1)
print(student)
print(teacher)
print(assistant)

print("\nПроверка равенства и статического метода")
print(f"Равны ли p1 и p2? {p1 == p2}")  
print(f"Студенту Ивану есть 18 лет? {Person.is_adult(student.age)}") 
print("\n Работа методов и множественного наследования")
print(f"Ассистент Мария: {assistant.research()}")  
print("\n Порядок разрешения методов (MRO) для Assistant")
print("MRO показывает, в каком порядке Python ищет методы:")
print("-> ".join([cls.__name__ for cls in Assistant.mro()]))
