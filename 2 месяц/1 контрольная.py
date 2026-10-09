from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, id, brand, model, year, mileage, fuel):
        self.id = id
        self.brand = brand
        self.model = model
    
        if year < 0:
            raise ValueError("Год не может быть отрицательным.")
        self.year = year
        self.__mileage = max(0, mileage)
        self.__fuel = max(0.0, min(100.0, float(fuel)))

    def start_engine(self):
        print(f"Двигатель {self.brand} {self.model} запущен.")

    def stop_engine(self):
        print(f"Двигатель {self.brand} {self.model} остановлен.")
    def get_fuel(self):
        return self.__fuel

    def get_mileage(self):
        return self.__mileage

    def refuel(self, amount):
        if amount < 0:
            raise ValueError("Нельзя заправить отрицательное количество топлива.")
        new_fuel = self.__fuel + amount
        self.__fuel = min(100.0, new_fuel)
        print(f"Топливо пополнено. Текущий уровень топлива: {self.__fuel}%")

    def consume_fuel(self, amount):
        if amount < 0:
            raise ValueError("Расход не может быть отрицательным.")
        if self.__fuel < amount:
            raise ValueError("Недостаточно топлива для поездки")
        self.__fuel -= amount

    def drive(self, km):
        if km < 0:
            raise ValueError("Километраж не может быть отрицательным.")
        if self.__fuel <= 0:
            raise ValueError("Машина не может ехать, бак пуст. Необходимо полуить топливо")
        fuel_needed = km * 0.1
        self.consume_fuel(fuel_needed)
        self.__mileage += km
        print(f"Проехали {km} км. Текущий пробег: {self.__mileage} км.")

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
        print(f"Легковой автомобиль {self.brand} {self.model} ({self.body_type}, {self.doors} двери) — {self.year} г. Пробег: {self.get_mileage()} км. Топливо: {self.get_fuel()}%")

    def service(self):
        print(f"Обслуживание {self.brand} {self.model}: Замена масла.")


class Truck(Vehicle):
    def __init__(self, id, brand, model, year, mileage, fuel, max_load):
        super().__init__(id, brand, model, year, mileage, fuel)
        self.max_load = max_load

    def info(self):
        print(f"Грузовик {self.brand} {self.model} Макс. груз: {self.max_load} тонн — {self.year} г. Пробег: {self.get_mileage()} км. Топливо: {self.get_fuel()}%")

    def service(self):
        print(f"Обслуживание {self.brand} {self.model}: Замена масла и проверка гидравлики.")


class Motorcycle(Vehicle):
    def __init__(self, id, brand, model, year, mileage, fuel, engine_volume):
        super().__init__(id, brand, model, year, mileage, fuel)
        self.engine_volume = engine_volume

    def info(self):
        print(f"Мотоцикл {self.brand} {self.model} Объем двигателя: {self.engine_volume} куб.см — {self.year} г. Пробег: {self.get_mileage()} км. Топливо: {self.get_fuel()}%")

    def service(self):
        print(f"Обслуживание {self.brand} {self.model}: Замена цепи.")


class Bus(Vehicle):
    def __init__(self, id, brand, model, year, mileage, fuel, seats):
        super().__init__(id, brand, model, year, mileage, fuel)
        self.seats = seats

    def info(self):
        print(f"Автобус {self.brand} {self.model} {self.seats} мест — {self.year} г. Пробег: {self.get_mileage()} км. Топливо: {self.get_fuel()}%")

    def service(self):
        print(f"Обслуживание {self.brand} {self.model}: Проверка пассажирских сидений.")

class Driver:
    def __init__(self, name, age, experience, license_category):
        self.name = name
        self.age = age
        self.experience = experience
        self.license_category = license_category
        self.assigned_vehicle = None  # У одного водителя только 1 машина

    def assign_vehicle(self, vehicle):
        if self.assigned_vehicle:
            print(f"У водителя {self.name} уже есть машина: {self.assigned_vehicle.brand} {self.assigned_vehicle.model}")
        else:
            self.assigned_vehicle = vehicle
            print(f"Водитель {self.name} назначен на {vehicle.brand} {self.model}.")

    def remove_vehicle(self):
        if self.assigned_vehicle:
            print(f"Водитель {self.name} снят с машины {self.assigned_vehicle.brand} {self.assigned_vehicle.model}.")
            self.assigned_vehicle = None
        else:
            print(f"У водителя {self.name} нет назначенной машины.")

    def show_vehicle(self):
        if self.assigned_vehicle:
            print(f"Водитель {self.name} управляет:")
            self.assigned_vehicle.info()
        else:
            print(f"Водитель {self.name} в данный момент без машины.")

class Fleet:
    def __init__(self):
        self.vehicles = []
        self.drivers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Транспорт {vehicle.brand} {vehicle.model} добавлен в автопарк.")

    def remove_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.id == vehicle_id:
                self.vehicles.remove(v)
                print(f"Транспорт с ID {vehicle_id} удален.")
                return
        print("Транспорт с таким ID не найден.")

    def find_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.id == vehicle_id:
                return v
        return None

    def show_all(self):
        if not self.vehicles:
            print("Автопарк пуст.")
        for v in self.vehicles:
            v.info()

    def service_all(self):
        for v in self.vehicles:
            v.service()

    def drive_vehicle(self, vehicle_id, km):
        v = self.find_vehicle(vehicle_id)
        if v:
            try:
                v.drive(km)
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            print("Транспорт не найден.")

    def sort_by_year(self):
        self.vehicles.sort(key=lambda x: x.year)
        print("Транспорт отсортирован по году выпуска.")
        self.show_all()

    def sort_by_mileage(self):
        self.vehicles.sort(key=lambda x: x.get_mileage())
        print("Транспорт отсортирован по пробегу.")
        self.show_all()

    def add_driver(self, driver):
        self.drivers.append(driver)
        print(f"Водитель {driver.name} добавлен в базу.")

    def show_drivers(self):
        if not self.drivers:
            print("База водителей пуста.")
        for d in self.drivers:
            print(f"ФИО: {d.name}, Возраст: {d.age}, Стаж: {d.experience}г., Категория: {d.license_category}")
            d.show_vehicle()
def main():
    fleet = Fleet()
    fleet.add_driver(Driver("Иванов И.И.", 35, 12, "B, C"))

    while True:
        print("\n Меню управления автопарком:")
        print("1. Добавить транспорт")
        print("2. Удалить транспорт")
        print("3. Показать весь транспорт")
        print("4. Найти транспорт")
        print("5. Отправить транспорт на обслуживание")
        print("6. Заправить машину")
        print("7. Проехать расстояние")
        print("8. Назначить водителя на транспорт")
        print("9. Показать водителей")
        print("10. Сортировка транспорта")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            print('Вы добавили транспорт')
        elif choice =="2":
            print("Вы удалили транспорт.")
        elif choice =="3":
            print("Вам показали транспорт")
        elif choice== "4":
            print("Вы нашли транспорт.")
        elif choice =="5":
            print("Вы отправили машину на обслуживание.")
        elif choice=="6":
            print("Вы выбрали заправить машину")
        elif choice=="7":
            print("Вы проезжаете расстояние.")
        elif choice=="8":
            print("Вы назначили водителя")
        elif choice=="9":
            print("Вы просмотрели водителей")
        elif choice=="10":
            print("Вы применили сортировку")
        elif choice=="0":
            print('Вы вышли с приложения. До свидания.')
        else :
            print("Ошибка.")
if __name__ == "__main__":
    main()
