#str для пользователя
#repr для разработчиков
#lten для длины
#eq сравнивает, эти магические методы вызывают сами себя
#staticmethod это декоратор, который улучшает код
#в статичном методе можено обращаться к объекту напрямую, не принимают селф
#классовые методы прнимают атрибут клс вместо селф, работает с самим классом а не объектом
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.music=[]
    def __str__(self):
        return f"User(name={self.name},afe={self.age})"
    def add(self,song):
        self.music.append(song)
    def __len__ (self):
        return len(self.music)
    def __add__(self,other):
        if isinstance (other,User):
            return self.name +"&"+ other.name , self.age +other.age
        return NotImplemented
    def __eq__(self,other):
        if isinstance (other,User):
            return self.name==other.name and self.age ==other.age
user=User("Bob",30)
print(user)
user1=User("Alice",20)
user.add("Song 1")
user.add("Song 2")
print(len(user))


class Math:
    @staticmethod
    def add (a,b):
        return a+b 
n=Math 
print(Math.add(5,5))
def age(func):
    def a (*args,**kwargs):
        print("До вызова функции")
        func(*args,**kwargs)
        print("После вызова функции")
    return a
@age
def user(user="Bob"):
    print(user)
print(user("Alice"))
result=user('Alice')      
print(result)


class User:
    users=0
    def __init__(self,name):
        self.name=name
        User.users+=1
    @classmethod
    def total_user(cls):
        return cls.users
user1=User("Bob")
user2=User("Alice")
print(User.total_user())
#множественные классы, когда один класс принадлежить главным нескольким
class Fly:
    def fly(self):
        print("Летает")
class Swim:
    def swim(self):
        print("Плавает")
class Duck(Fly,Swim):
    pass
duck=Duck()
duck.fly()
duck.swim()
class A:
    def hello(self):
        print("A")
class B(A):
    def hello(self):
        print("B")
class C(A):
    def hello(self):
        print("C")
class D(B,C):
    pass
class E(A):
    pass
e=E()
e.hello()
d=D()
d.hello()
#каждый класс наследуется самым главным классом, который создал  сам питон -object, и чтобы посмотреть последовательность главных классов  необходимо написать:print(D.mro)
class Camera:
    def take_photo(self):
        print("photo")
class Phone:
    def call(self, number=None):
        self.number = number
        print("call")
class Smartphone(Camera,Phone):
    pass
camera=Camera()
camera.take_photo()
phone=Phone()
phone.call()
smartphone=Smartphone()