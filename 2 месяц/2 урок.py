class Animal:
    def __init__ (self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} ест")
class Cat(Animal):
    def __init__(self,name,color):
        super().__init__ (name)
        self.color=color
    def meow(self):
        print(f"{self.name} мяукает")
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age_years = age

    def age(self):
        print(f"{self.age_years} года")

    def bark(self):
        print(f"{self.name} лает")

cat = Cat("Барсик", "серый")
dog = Dog("Шарик", 3)
print(cat.name)
print(cat.color)
cat.eat()
cat.meow()
dog.eat()
dog.bark()
dog.age()

class Animal:
    def sound (self):
        pass
class Cat(Animal):
    def sound(self):
        print("Мяу")
class Dog(Animal):
    def sound(self):
        print('Гав')
cat=Cat()
cat.sound()
dog=Dog()
dog.sound()
class Payment:
    def __init__(self, amount):
        self.amount = amount

class Card(Payment):
    def pay(self):
        print(f"Оплата картой {self.amount}")
class Cash(Payment):
    def pay(self):
        print(f"Оплата наличными {self.amount}")
class Paypal(Payment):
    def pay(self):
        print(f"Оплата Paypal {self.amount}")
methods=[Paypal(100),Card(3000),Cash(200)]
for method in methods:
    method.pay()
    