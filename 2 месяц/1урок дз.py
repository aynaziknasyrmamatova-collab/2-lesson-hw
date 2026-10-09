#1 задание
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Страницы: {self.pages}")
    def read(self):
        print(f"Читаем книгу {self.title}")
book = Book("Гарри Поттер", "Джоан Роулинг", 500)
book.info()
book.read()
#2 задание
class Player:
    def __init__(self, name, health=100, level=1):
        self.name = name
        self.health = health
        self.level = level
    def show_info(self):
        print(f"Игрок: {self.name}, Уровень: {self.level}, Здоровье: {self.health}")
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print("Игрок погиб!")
    def heal(self, amount):
        self.health += amount
    def level_up(self):
        self.level += 1
player = Player("Knight")
player.show_info()
player.take_damage(30)
player.heal(20)
player.level_up()
player.show_info()
#3 задание
class OnlineStore:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print("Такого товара нет!")
    def show_products(self):
        print(f"Товары в магазине '{self.name}': {', '.join(self.products)}")
    def count_products(self):
        print(f"Всего товаров: {len(self.products)}")
store = OnlineStore("Tech Store")
store.add_product("Ноутбук")
store.add_product("Мышка")
store.add_product("Клавиатура")
store.show_products()
store.count_products()
store.remove_product("Мышка")
store.show_products()

