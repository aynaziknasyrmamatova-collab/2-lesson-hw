from abc import ABC, abstractmethod
class Vehicle(ABC):

    def __init__(self, vehicle_id, brand, model, year, mileage, fuel):
        if year < 0:
            raise ValueError("Год не может быть отрицательным")

        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")

        if fuel < 0 or fuel > 100:
            raise ValueError("Топливо должно быть от 0 до 100%")

        self.id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year

        # Инкапсуляция
        self.__mileage = mileage
        self.__fuel = fuel

        self.engine_running = False

    def refuel(self, amount):
        if amount <= 0:
            raise ValueError("Количество топлива должно быть положительным")

        if self.__fuel + amount > 100:
            raise ValueError("Нельзя заправить больше 100%")

        self.__fuel += amount
        print(f"Транспорт заправлен. Топливо: {self.__fuel}%")

    def get_fuel(self):
        return self.__fuel

    def consume_fuel(self, amount):
        if amount < 0:
            raise ValueError("Расход топлива не может быть отрицательным")

        if self.__fuel - amount < 0:
            raise ValueError("Недостаточно топлива")

        self.__fuel -= amount
    def get_mileage(self):
        return self.__mileage

    def drive(self, km):
        if km <= 0:
            raise ValueError("Расстояние должно быть положительным")

        if self.__fuel <= 0:
            raise ValueError("Нельзя ехать без топлива")
        fuel_consumption = km / 10

        if fuel_consumption > self.__fuel:
            raise ValueError("Недостаточно топлива для поездки")

        self.__mileage += km
        self.consume_fuel(fuel_consumption)

        print(f"Транспорт проехал {km} км")
        print(f"Текущий пробег: {self.__mileage} км")
        print(f"Остаток топлива: {self.__fuel:.1f}%")

    def start_engine(self):
        if self.__fuel <= 0:
            print("Нельзя запустить двигатель: нет топлива")
            return

        self.engine_running = True
        print(f"{self.brand} {self.model}: двигатель запущен")

    def stop_engine(self):
        self.engine_running = False
        print(f"{self.brand} {self.model}: двигатель остановлен")
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def service(self):
        pass

    def __str__(self):
        return f"{self.brand} {self.model}"
class Car(Vehicle):

    def __init__(
            self,
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            doors,
            body_type
    ):
        super().__init__(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel
        )

        self.doors = doors
        self.body_type = body_type

    def info(self):
        print("\n--- Легковой автомобиль ---")
        print(f"ID: {self.id}")
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Пробег: {self.get_mileage()} км")
        print(f"Топливо: {self.get_fuel():.1f}%")
        print(f"Количество дверей: {self.doors}")
        print(f"Тип кузова: {self.body_type}")

    def service(self):
        print(f"{self}: замена масла и диагностика двигателя")
class Truck(Vehicle):

    def __init__(
            self,
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            max_load
    ):
        super().__init__(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel
        )

        self.max_load = max_load

    def info(self):
        print("\n--- Грузовик ---")
        print(f"ID: {self.id}")
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Пробег: {self.get_mileage()} км")
        print(f"Топливо: {self.get_fuel():.1f}%")
        print(f"Максимальная грузоподъёмность: {self.max_load} тонн")

    def service(self):
        print(f"{self}: замена масла и проверка гидравлики")
class Motorcycle(Vehicle):

    def __init__(
            self,
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            engine_volume
    ):
        super().__init__(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel
        )

        self.engine_volume = engine_volume

    def info(self):
        print("\n--- Мотоцикл ---")
        print(f"ID: {self.id}")
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Пробег: {self.get_mileage()} км")
        print(f"Топливо: {self.get_fuel():.1f}%")
        print(f"Объём двигателя: {self.engine_volume} см³")

    def service(self):
        print(f"{self}: замена цепи и проверка тормозов")
class Bus(Vehicle):

    def __init__(
            self,
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            seats
    ):
        super().__init__(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel
        )

        self.seats = seats

    def info(self):
        print("\n--- Автобус ---")
        print(f"ID: {self.id}")
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год: {self.year}")
        print(f"Пробег: {self.get_mileage()} км")
        print(f"Топливо: {self.get_fuel():.1f}%")
        print(f"Количество мест: {self.seats}")

    def service(self):
        print(f"{self}: проверка пассажирских сидений и тормозной системы")

class Fleet:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Можно добавить только транспорт")

        if self.find_vehicle(vehicle.id):
            raise ValueError("Транспорт с таким ID уже существует")

        self.vehicles.append(vehicle)
        print("Транспорт успешно добавлен")

    def remove_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Транспорт не найден")
            return

        self.vehicles.remove(vehicle)
        print("Транспорт удалён")

    def find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                return vehicle

        return None

    def show_all(self):
        if not self.vehicles:
            print("Автопарк пуст")
            return

        for vehicle in self.vehicles:
            vehicle.info()

    def service_all(self):
        if not self.vehicles:
            print("Автопарк пуст")
            return

        for vehicle in self.vehicles:
            vehicle.service()

    def drive_vehicle(self, vehicle_id, km):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Транспорт не найден")
            return

        vehicle.drive(km)

    def sort_by_year(self):
        self.vehicles.sort(key=lambda vehicle: vehicle.year)
        print("Транспорт отсортирован по году выпуска")

    def sort_by_mileage(self):
        self.vehicles.sort(key=lambda vehicle: vehicle.get_mileage())
        print("Транспорт отсортирован по пробегу")
class Driver:

    def __init__(self, full_name, age, experience, license_category):
        self.full_name = full_name
        self.age = age
        self.experience = experience
        self.license_category = license_category

        self.vehicle = None

    def assign_vehicle(self, vehicle):
        if self.vehicle is not None:
            print("У водителя уже есть назначенный транспорт")
            return

        self.vehicle = vehicle
        print(
            f"Водителю {self.full_name} назначен "
            f"{vehicle.brand} {vehicle.model}"
        )

    def remove_vehicle(self):
        if self.vehicle is None:
            print("У водителя нет назначенного транспорта")
            return

        print(f"Транспорт снят с водителя {self.full_name}")
        self.vehicle = None

    def show_vehicle(self):
        if self.vehicle is None:
            print(f"{self.full_name}: транспорт не назначен")
        else:
            print(
                f"{self.full_name} управляет "
                f"{self.vehicle.brand} {self.vehicle.model}"
            )

    def __str__(self):
        return (
            f"{self.full_name}, "
            f"возраст: {self.age}, "
            f"стаж: {self.experience} лет, "
            f"категория: {self.license_category}"
        )

def create_vehicle():
    print("\nВыберите тип транспорта:")
    print("1. Легковой автомобиль")
    print("2. Грузовик")
    print("3. Мотоцикл")
    print("4. Автобус")

    vehicle_type = input("Ваш выбор: ")

    vehicle_id = int(input("ID: "))
    brand = input("Марка: ")
    model = input("Модель: ")
    year = int(input("Год выпуска: "))
    mileage = float(input("Пробег: "))
    fuel = float(input("Топливо (%): "))

    if vehicle_type == "1":
        doors = int(input("Количество дверей: "))
        body_type = input("Тип кузова: ")

        return Car(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            doors,
            body_type
        )

    elif vehicle_type == "2":
        max_load = float(input("Максимальная грузоподъёмность (тонн): "))

        return Truck(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            max_load
        )

    elif vehicle_type == "3":
        engine_volume = int(input("Объём двигателя (см³): "))

        return Motorcycle(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            engine_volume
        )

    elif vehicle_type == "4":
        seats = int(input("Количество мест: "))

        return Bus(
            vehicle_id,
            brand,
            model,
            year,
            mileage,
            fuel,
            seats
        )

    else:
        print("Неверный тип транспорта")
        return None
def main():

    fleet = Fleet()
    drivers = []

    while True:

        print("\n========== АВТОПАРК ==========")
        print("1. Добавить транспорт")
        print("2. Удалить транспорт")
        print("3. Показать транспорт")
        print("4. Найти транспорт")
        print("5. Отправить на обслуживание")
        print("6. Заправить машину")
        print("7. Проехать расстояние")
        print("8. Назначить водителя")
        print("9. Показать водителей")
        print("10. Сортировка")
        print("0. Выход")

        choice = input("Выберите действие: ")

        try:

            if choice == "1":

                vehicle = create_vehicle()

                if vehicle is not None:
                    fleet.add_vehicle(vehicle)

            elif choice == "2":

                vehicle_id = int(input("Введите ID транспорта: "))
                fleet.remove_vehicle(vehicle_id)

            elif choice == "3":

                fleet.show_all()

            elif choice == "4":

                vehicle_id = int(input("Введите ID транспорта: "))
                vehicle = fleet.find_vehicle(vehicle_id)

                if vehicle is None:
                    print("Транспорт не найден")
                else:
                    vehicle.info()

            elif choice == "5":

                vehicle_id = int(input("Введите ID транспорта: "))
                vehicle = fleet.find_vehicle(vehicle_id)

                if vehicle is None:
                    print("Транспорт не найден")
                else:
                    vehicle.service()

            elif choice == "6":

                vehicle_id = int(input("Введите ID транспорта: "))
                amount = float(input("Сколько процентов заправить: "))

                vehicle = fleet.find_vehicle(vehicle_id)

                if vehicle is None:
                    print("Транспорт не найден")
                else:
                    vehicle.refuel(amount)

            elif choice == "7":

                vehicle_id = int(input("Введите ID транспорта: "))
                km = float(input("Сколько километров проехать: "))

                fleet.drive_vehicle(vehicle_id, km)

            elif choice == "8":

                full_name = input("ФИО водителя: ")
                age = int(input("Возраст: "))
                experience = int(input("Стаж: "))
                category = input("Категория прав: ")

                driver = Driver(
                    full_name,
                    age,
                    experience,
                    category
                )

                vehicle_id = int(
                    input("Введите ID транспорта для назначения: ")
                )

                vehicle = fleet.find_vehicle(vehicle_id)

                if vehicle is None:
                    print("Транспорт не найден")
                else:
                    driver.assign_vehicle(vehicle)
                    drivers.append(driver)

            elif choice == "9":

                if not drivers:
                    print("Водителей нет")
                else:
                    for driver in drivers:
                        print(driver)
                        driver.show_vehicle()

            elif choice == "10":

                print("\n1. Сортировать по году")
                print("2. Сортировать по пробегу")

                sort_choice = input("Ваш выбор: ")

                if sort_choice == "1":
                    fleet.sort_by_year()
                    fleet.show_all()

                elif sort_choice == "2":
                    fleet.sort_by_mileage()
                    fleet.show_all()

                else:
                    print("Неверный выбор")

            elif choice == "0":

                print("Программа завершена")
                break

            else:
                print("Неверный пункт меню")
if __name__ == "__main__":
    main()