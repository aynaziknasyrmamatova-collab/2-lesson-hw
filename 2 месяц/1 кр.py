from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, id, brand, model, year, mileage, fuel):
        if year < 0:
            raise ValueError("Год не может быть отрицательным.")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным.")
        if not (0 <= fuel <= 100):
            raise ValueError("Топливо должно быть от 0 до 100.")
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage
        self.__fuel = fuel

    def start_engine(self):
        print(f"{self.brand} {self.model}: двигатель запущен.")

    def stop_engine(self):
        print(f"{self.brand} {self.model}: двигатель остановлен.")

    def drive(self, km):
        if km < 0:
            print("Нельзя ехать отрицательное расстояние ")
            return

        if self.__fuel <= 0:
            print("Недостаточно топлива ")
            return

        fuel_need = km * 0.1

        if fuel_need > self.__fuel:
            print("Недостаточно топлива для поездки.")
            return

        self.__mileage += km
        self.consume_fuel(fuel_need)

        print(f"{self.brand} проехал {km} км ")

    def refuel(self, amount):
        if amount < 0:
            print("Нельзя заправить отрицательное количество")
            return

        if self.__fuel + amount > 100:
            self.__fuel = 100
        else:
            self.__fuel += amount
        print(f"Топливо: {self.__fuel:.1f}%")
    def consume_fuel(self, amount):
        self.__fuel -= amount
        if self.__fuel < 0:
            self.__fuel = 0
    def get_fuel(self):
        return round(self.__fuel, 1)
    def get_mileage(self):
        return self.__mileage

    @abstractmethod
    def info(self):
        pass
    @abstractmethod
    def service(self):
        pass
class Car(Vehicle):
    def __init__(self, id, brand, model, year, mileage, fuel, doors, body_type):
        super().__init__(id, brand, model, year, mileage, fuel)
        self.doors = doors
        self.body_type = body_type

    def info(self):
        print(f"""
Легковой автомобиль
{self.brand} {self.model}
Год: {self.year}
Пробег: {self.get_mileage()} км
Топливо: {self.get_fuel()}%
Дверей: {self.doors}
Кузов: {self.body_type}
""")

    def service(self):
        print(f"{self.brand}: Замена масла.")

class Truck(Vehicle):
    def __init__(self, id, brand, model, year, mileage, fuel, max_load):
        super().__init__(id, brand, model, year, mileage, fuel)
        self.max_load = max_load

    def info(self):
        print(f"""
Грузовик
{self.brand} {self.model}
Макс. груз: {self.max_load} тонн
Пробег: {self.get_mileage()} км
""")

    def service(self):
        print(f"{self.brand}: Замена масла и проверка гидравлики.")

class Motorcycle(Vehicle):
    def __init__(self, id, brand, model, year, mileage, fuel, engine_volume):
        super().__init__(id, brand, model, year, mileage, fuel)
        self.engine_volume = engine_volume

    def info(self):
        print(f"""
Мотоцикл
{self.brand} {self.model}
Объем двигателя: {self.engine_volume}
Пробег: {self.get_mileage()} км
""")

    def service(self):
        print(f"{self.brand}: Замена цепи")


class Bus(Vehicle):
    def __init__(self, id, brand, model, year, mileage, fuel, seats):
        super().__init__(id, brand, model, year, mileage, fuel)
        self.seats = seats

    def info(self):
        print(f"""
Автобус
{self.brand} {self.model}
Количество мест: {self.seats}
Пробег: {self.get_mileage()} км
""")

    def service(self):
        print(f"{self.brand}: Проверка пассажирских сидений.")
class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, id):
        self.vehicles = [v for v in self.vehicles if v.id != id]

    def find_vehicle(self, id):
        for v in self.vehicles:
            if v.id == id:
                return v
        return None

    def show_all(self):
        if not self.vehicles:
            print("Транспорт отсутствует.  ")
            return

        for v in self.vehicles:
            v.info()

    def service_all(self):
        for v in self.vehicles:
            v.service()

    def drive_vehicle(self, id, km):
        vehicle = self.find_vehicle(id)
        if vehicle:
            vehicle.drive(km)
        else:
            print("Не найден.")

    def sort_by_year(self):
        self.vehicles.sort(key=lambda x: x.year)

    def sort_by_mileage(self):
        self.vehicles.sort(key=lambda x: x.get_mileage())


class Driver:
    def __init__(self, fullname, age, experience, category):
        self.fullname = fullname
        self.age = age
        self.experience = experience
        self.category = category
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        if self.vehicle is not None:
            print("У водителя уже есть транспорт")
        else:
            self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = None

    def show_vehicle(self):
        print(f"\nВодитель: {self.fullname}")

        if self.vehicle:
            self.vehicle.info()
        else:
            print("Транспорт не назначен")

fleet = Fleet()
drivers = []

while True:
    print("""
СИСТЕМА УПРАВЛЕНИЯ АВТОПАРКОМ
1.Добавить транспорт
2 .Удалить транспорт
3. Показать транспорт
4. Найти транспорт
5 .Отправить на обслуживание
6. Заправить машину
7. Проехать расстояние
8. Назначить водителя
9. Показать водителей
10. Сортировка
0 .Выход
""")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print("1-car, 2-truck,3- motorcycle, 4-bus")
        t = input()

        id = int(input("ID: "))
        brand = input("Марка: ")
        model = input("Модель: ")
        year = int(input("Год:"))
        mileage = float(input("Пробег: "))
        fuel = float(input("Топливо:"))

        if t == "1":
            doors = int(input("Количество дверей:"))
            body = input("Тип кузова: ")
            fleet.add_vehicle(Car(id, brand, model, year, mileage, fuel, doors, body))

        elif t == "2":
            load = float(input("Макс. груз: "))
            fleet.add_vehicle(Truck(id, brand, model, year, mileage, fuel, load))

        elif t == "3":
            volume = input("Объем двигателя:")
            fleet.add_vehicle(Motorcycle(id, brand, model, year, mileage, fuel, volume))

        elif t == "4":
            seats = int(input("Количество мест: "))
            fleet.add_vehicle(Bus(id, brand, model, year, mileage, fuel, seats))

    elif choice == "2":
        fleet.remove_vehicle(int(input("ID:")))

    elif choice == "3":
        fleet.show_all()
    elif choice == "4":
        v = fleet.find_vehicle(int(input("ID:")))
        if v:
            v.info()
        else:
            print("Не найдено")

    elif choice == "5":
        v = fleet.find_vehicle(int(input("ID: ")))
        if v:
            v.service()

    elif choice == "6":
        v = fleet.find_vehicle(int(input("ID: ")))
        if v:
            amount = float(input("Сколько заправить : "))
            v.refuel(amount)

    elif choice == "7":
        fleet.drive_vehicle(
            int(input("ID: ")),
            float(input("Километры: "))
        )

    elif choice == "8":
        name = input("ФИО: ")
        age = int(input("Возраст: "))
        exp = int(input("Стаж:"))
        cat = input("Категория:")

        driver = Driver(name, age, exp, cat)
        vehicle = fleet.find_vehicle(int(input("ID транспорта: ")))
        if vehicle:
            driver.assign_vehicle(vehicle)
        drivers.append(driver)
    elif choice == "9":
        for i in drivers:
            i.show_vehicle()

    elif choice == "10":
        print("1 - По году")
        print("2 - По пробегу")
        s = input()
        if s == "1":
            fleet.sort_by_year()
        else:
            fleet.sort_by_mileage()
        fleet.show_all()
    elif choice == "0":
        print("Вы вышли с приложения. До савидания.")
        break
    else:
        print("Неверный выбор, попробуйте снова")