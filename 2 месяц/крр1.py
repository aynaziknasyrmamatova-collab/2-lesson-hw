from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, id_num, brand, model, year, mileage, fuel):
        self.id = id_num
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage  
        self.__fuel = max(
            0, min(100, fuel)
        )  

    def start_engine(self):
        print(f"Двигатель {self.brand} {self.model} запущен.")

    def stop_engine(self):
        print(f"Двигатель {self.brand} {self.model} остановлен.")

    def drive(self, km):
        if self.__fuel <= 0:
            print("Топливо закончилось! Заправьте транспорт перед поездкой.")
            return
        needed_fuel = km * 0.1
        if self.consume_fuel(needed_fuel):
            self.__mileage += km
            print(f"Проехали {km} км. Новый пробег: {self.__mileage} км.")
        else:
            print("Недостаточно топлива для полной поездки.")
    def get_fuel(self):
        return self.__fuel

    def refuel(self, amount):
        new_fuel = self.__fuel + amount
        self.__fuel = max(
            0, min(100, new_fuel)
        ) 
        print(f"Топливо пополнено. Уровень: {self.get_fuel()}%")

    def consume_fuel(self, amount):
        if self.__fuel - amount >= 0:
            self.__fuel -= amount
            return True
        return False
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def service(self):
        pass

class Car(Vehicle):
    def __init__(self, id_num, brand, model, year, mileage, fuel, doors, body_type):
        super().__init__(id_num, brand, model, year, mileage, fuel)
        self.doors = doors
        self.body_type = body_type

    def info(self):
        print(
            f"Легковой автомобиль {self.brand} {self.model} ({self.year}) — {self.doors} двери, тип кузова: {self.body_type}. Пробег: {self._Vehicle__mileage} км."
        )

    def service(self):
        print(f"Обслуживание {self.brand} {self.model}: Замена масла.")

class Truck(Vehicle):
    def __init__(self, id_num, brand, model, year, mileage, fuel, max_load):
        super().__init__(id_num, brand, model, year, mileage, fuel)
        self.max_load = max_load

    def info(self):
        print(
            f"Грузовик {self.brand} {self.model} ({self.year}) Макс. груз: {self.max_load} тонн. Пробег: {self._Vehicle__mileage} км."
        )

    def service(self):
        print(
            f"Обслуживание {self.brand} {self.model}: Замена масла и проверка гидравлики."
        )

class Motorcycle(Vehicle):
    def __init__(self, id_num, brand, model, year, mileage, fuel, engine_volume):
        super().__init__(id_num, brand, model, year, mileage, fuel)
        self.engine_volume = engine_volume

    def info(self):
        print(
            f"Мотоцикл {self.brand} {self.model} ({self.year}) Объем двигателя: {self.engine_volume} куб.см. Пробег: {self._Vehicle__mileage} км."
        )

    def service(self):
        print(f"Обслуживание {self.brand} {self.model}: Замена цепи.")
class Bus(Vehicle):
    def __init__(self, id_num, brand, model, year, mileage, fuel, seats):
        super().__init__(id_num, brand, model, year, mileage, fuel)
        self.seats = seats

    def info(self):
        print(
            f"Автобус {self.brand} {self.model} ({self.year}) — {self.seats} мест. Пробег: {self._Vehicle__mileage} км."
        )

    def service(self):
        print(
            f"Обслуживание {self.brand} {self.model}: Проверка пассажирских сидений."
        )
if __name__ == "__main__":
    my_car = Car(1, "BMW", "M5", 2022, 15000, 50, 4, "седан")
    my_truck = Truck(2, "MAN", "TGX", 2021, 120000, 80, 18)
    my_motorcycle=Motorcycle("BMW", 30000,2023,13000,34,8)
    my_bus=Bus("Mercedes Benz",130, 2003,1400,70,8)
my_car.drive(100)  
print("\n Информация")
my_car.info()
my_truck.info()
my_motorcycle.info
my_bus.info()
print("\n Сервис")
my_car.service()
my_truck.service()
my_bus.service()
my_motorcycle.service()

