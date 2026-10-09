#1 задание
class Delivery:
    def __init__ (self,sender,receiver,distance):
        self.sender=sender
        self.receiver=receiver
        self.distance=distance #создаем родительский класс с атрибутами
    def price(self):
        pass #создаем метод прайс который пока ничего не делает
    def deliver(self):
        print(f"Доставка от: {self.sender}")
        print(f"Получатель: {self.receiver}")
        print(f"Дистанция: {self.distance} км" ) #тут метод деливер выводит информацию о доставке
delivery=Delivery("Иван", "Маша", "43") #здесь мы просто пишем данные
delivery.deliver()
#2 задание
class CarDelivery (Delivery):
    def __init__(self,distance):
        super().__init__("","",distance) #тут создаем доченрий класс с супер инит
    def calculate_price(self):
        return self.distance * 15 #здесь делают цену с учетом дистанции *15
    def estimated_time(self):
        return round(self.distance/60,2)
    def deliver(self):
        print(f"Способ доставки: машина")
        print(f"Стоимость доставки: {self.calculate_price()} сом\n")
class AirDelivery(Delivery):
    def __init__(self,distance):
        super().__init__("","",distance) #также создаем доченрий класс с супер инит
    def calculate_price(self):
        return self.distance *50+500 #находим цену за доставку
    def estimated_time(self):
        return round(self.distance/700,2)
    def deliver(self):
        print(f"Способ доставки: воздушное судно")
        print(f"Стоимость доставки: {self.calculate_price()} сом\n")
class DroneDelivery(Delivery):
    def __init__(self,distance):
        super().__init__("","",distance) #тоже самое создаем дочерний класс
    def calculate_price(self):
        return self.distance *30 #находим цену за доставку
    def estimated_time(self):
        return round(self.distance/4,2)
    def deliver(self):
        if self.distance>30:
            print(f"Дрон не может доставить на такое расстояние") #делаем условие что на расстояние больше 30 км дрон не может доставить
        else:
            print(f"Способ доставки: дрон")
            print(f"Стоимость доставки {self.calculate_price()} сом\n")

car=CarDelivery (45)
car.deliver()
air=AirDelivery(100)
air.deliver()
drone1=DroneDelivery (20)
drone1.deliver()
drone2=DroneDelivery (70)
drone2.deliver()
#тут мы все пишем, чтобы потом в терминале у нас все вывелось, а также в скобках пишем дистанцию
#3 задание
deliver=[CarDelivery(45),AirDelivery(100),DroneDelivery(10),CarDelivery(15)] #создаем список доставок
print("Запуск цикла")
for delivery in deliver:
    delivery.deliver()
    print(f"Результат calculate_price():{delivery.calculate_price()}")
    print("-"*40+"\n")
#циклом проходимся, вызывая для каждого объекта delivery.deliver
#4 задание
print("Запус проверки метода estimated_time()") #добавляем метод estimated time
for delivery in deliver:
    if isinstance(delivery, DroneDelivery)and delivery.distance>30:
        continue
    print(f"Транспорт с дистанцией {delivery.distance} км")
    print(f"Время в пути: {delivery.estimated_time()} ч")
    print("-"*40+"\n")

#5 задание
class DeliveryManager:
    def __init__(self):
        self.deliveries = []
    def add_delivery(self, delivery):
        self.deliveries.append(delivery)
    def show_all(self):
        print("ВСЕ ДОСТАВКИ")
        for delivery in self.deliveries:
            delivery.deliver()
            print("-" * 30)
    def total_income(self):
        total = 0
        for delivery in self.deliveries:
            total = total + delivery.calculate_price()
        return total
    def most_expensive_delivery(self):
        if len(self.deliveries) == 0:
            return None
        expensive = self.deliveries[0]
        
        for delivery in self.deliveries:
            if delivery.calculate_price() > expensive.calculate_price():
                expensive = delivery 
        return expensive
#6 задание
manager = DeliveryManager()
manager.add_delivery(CarDelivery(45))
manager.add_delivery(AirDelivery(100))
manager.add_delivery(DroneDelivery(20))
manager.add_delivery(CarDelivery(15))
manager.show_all()
income = manager.total_income()
print(f"Общий доход: {income} сом")
print("-" * 30)
best_delivery = manager.most_expensive_delivery()
print("Самая дорогая доставка:")
best_delivery.deliver()

        
            