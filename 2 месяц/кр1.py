from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,id,brand,model,year,mileage,fuel):
        self.id=id
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage=mileage
        self.fuel=fuel
    def start_engine():
        pass
    def stop_engine():
        pass
    def drive(km):
        pass
    def info():
        pass
    def service():
        pass

class Car(Vehicle):
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def info(self):
        return (f"Легковой автомобиль {self.brand} {self.model} {self.year} Пробег: {self.mileage}")

    def service(self):
        return ("Замена масла")

class Truck(Vehicle):
    def __init__(self, model, max_load):
        self.model = model
        self.max_load = max_load

    def info(self):
        return (f"Грузовик {self.model} Макс. груз: {self.max_load}")

    def service(self):
        return ("Замена масла и проверка гидравлики")

class Motorcycle(Vehicle):
    def __init__(self, model):
        self.model = model
        
    def info(self):
        return (f"Мотоцикл {self.model}")
        
    def service(self):
        return ("Замена цепи")

class Bus(Vehicle):
    def __init__(self, seats):
        self.seats = seats

    def info(self):
        return (f"Автобус {self.seats} мест")
    def service(self):
        return ("Проверка пассажирских сидений")

vehicles = [
    Car("BMW", "M5", 2022, 15000),
    Truck("MAN TGX", "18 тонн"),
    Motorcycle("BMW S1000RR"),
    Bus(45)
]

for v in vehicles:
    print(f"{v.info()}  Обслуживание: {v.service()}")
class Car:
    def __init__(self, fuel=50, mileage=0):
        self.__fuel = max(0.0, min(100.0, float(fuel)))
        self.__mileage = max(0.0, float(mileage))

    def get_fuel(self):
        return self.__fuel

    def refuel(self, amount):
        if amount > 0:
            self.__fuel = min(100.0, self.__fuel + amount)
            print(f"Топливо пополнено. Текущий уровень топлива: {self.__fuel}%")
        else:
            print("Количество топлива для заправки должно быть больше нуля ")

    def consume_fuel(self, amount):
        if amount > 0:
            self.__fuel = max(0.0, self.__fuel - amount)
            print(f"Топливо израсходовано. Текущий уровень топлива: {self.__fuel}%")
        else:
            print("Количество расходуемого топлива должно быть больше нуля.")

    def get_mileage(self):
        return self.__mileage

    def drive(self, distance):
        if distance > 0:
            self.__mileage += distance
            print(f"Пробег увеличен на {distance} км. Всего: {self.__mileage} км.")
        elif distance=="2":
            print("Дистанция поездки должна быть больше нулz")
        elif distance=="6":
            print("На таую дистанцию автомобиль не сможет поехать")
        elif distance =="70":
            print('Эта дистанция не свободна. выберите другую')
        elif distance=="7":
            print("Ваша дистанция была успешно записана в наш автопарк")
        else:
            print('Ошибка, данная вами дистанция была набрана некорректно')