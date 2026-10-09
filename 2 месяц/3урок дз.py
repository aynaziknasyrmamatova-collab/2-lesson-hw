
#1 задание
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self): #метод make sound сделали абстрактным
        pass

class Dog(Animal):
    def make_sound(self): #пишем метод для каждого класса чтобы он производил свой звук
        print("Гав")

class Cat(Animal):
    def make_sound(self): #для класса cat производится звук мяу
        print("Мяу")

class Bird(Animal):
    def make_sound(self): #для класса bird создается звук чирик
        print("Чирик")

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.make_sound() #здесь мы вызываем звуки через цикл

#2 задание
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = float(initial_balance) #здесь мы создали поля owner и приватное поле balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Счет пополнен на {amount}. Баланс: {self.__balance}")
        else:
            print("Ошибка: сумма пополнения должна быть положительной.") # здесь мы создаем метод депозит,где есть правило что нельзя класть деньги на отрицательную сумму

    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть положительной.")
        elif amount > self.__balance:
            print("Ошибка: недостаточно средств на счету.")
        else:
            self.__balance -= amount
            print(f"Снято {amount}. Баланс: {self.__balance}") #тут мы создаем метод, добавляя как прежду условие что нельзя снять на отрицательную сумму, а также если средств недостаточно на счету
    def get_balance(self):
        return self.__balance # тут мы просто баланс пищем пополняем его
    def calculate_profit(self):
        pass #создаем просто метод calculate profit который ничего не будет делать
class CreditAccount(BankAccount):
    def __init__(self, owner, limit=1000):
        super().__init__(owner, initial_balance=0) #супер инит это дочерний класс
        self.limit = limit #создаем класс кредитаккаунт, который имеет кредитный лимит

    def calculate_profit(self):
        return self.get_balance() * 0.01  #здесь он считает прибыль

class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate=0.05):
        super().__init__(owner)
        self.interest_rate = interest_rate #тут мы реализовали полиморфизм , который будет считать прибыль

    def calculate_profit(self):
        return self.get_balance() * self.interest_rate #здесь считается прибыль уже точно
acc = SavingsAccount("Иван", interest_rate=0.05)
acc.deposit(1000) #тут добавляются данные о пользователе
print(f"Прибыль: {acc.calculate_profit()}")
#3 задание
from abc import ABC, abstractmethod #используем абстрактный метод
class Delivery(ABC):
    def __init__(self, address, price): #вот то что находится внутри скобочек и дальше пишется,это поля
        self.address = address
        self.price = price
    @abstractmethod
    def deliver(self): #делаем методы инит и деливери абстрактными
        pass
    @abstractmethod
    def calculate_price(self):
        pass
class CourierDelivery(Delivery):
    def __init__(self, address, courier_name, price=150):
        super().__init__(address, price) #добавляем методы с именем курьера
        self.courier_name = courier_name
    def calculate_price(self):
        return self.price
    def deliver(self):
        print(f"Курьер {self.courier_name} доставляет заказ по адресу: {self.address}. Стоимость: {self.calculate_price()} руб.")
class CarDelivery(Delivery):
    def __init__(self, address, distance, price_per_km=30):
        super().__init__(address, price=0)
        self.distance = distance
        self.price_per_km = price_per_km
    def calculate_price(self):
        return self.distance * self.price_per_km
    def deliver(self):
        print(f"Автомобиль доставляет заказ по адресу: {self.address} (расстояние {self.distance} км). Стоимость: {self.calculate_price()} руб.")
class DroneDelivery(Delivery):
    def __init__(self, address, weight, max_weight=5, price=200):
        super().__init__(address, price)
        self.weight = weight
        self.max_weight = max_weight

    def calculate_price(self):
        return self.price

    def deliver(self):
        if self.weight > self.max_weight:
            print(f"Ошибка: дрон не может доставить заказ (вес {self.weight} кг превышает лимит {self.max_weight} кг) по адресу: {self.address}.")
        else:
            print(f"Дрон доставляет заказ по адресу: {self.address}. Стоимость: {self.calculate_price()} руб.")
class Order:
    def __init__(self, address, delivery_method):
        self.address = address
        self.products = []
        self.__total_price = 0.0
        self.delivery_method = delivery_method

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})
        self.__total_price += price #добавляем инкапсуляцию, где цена остается приватной
        print(f"Товар '{name}' добавлен. Текущая стоимость корзины: {self.__total_price}")

    def remove_product(self, name, price):
        for item in self.products:
            if item["name"] == name and item["price"] == price:
                self.products.remove(item)
                self.__total_price -= price
                print(f"Товар '{name}' удален.")
                break
    def get_total_price(self):
        delivery_cost = self.delivery_method.calculate_price()
        return self.__total_price + delivery_cost
deliveries = [CourierDelivery("ул. Пушкина, 10", "Алексей"),CarDelivery("ул. Ленина, 15", 12),DroneDelivery("Парк Победы", 3.5)] #используем полиморфизм
for delivery in deliveries:
    delivery.deliver()
