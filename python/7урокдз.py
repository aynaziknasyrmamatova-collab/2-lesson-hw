#1 задание функция принимает список и возвращает сумму всех четных чисел
def sum_even(numbers):
    return numbers**2
print(sum_even(21344))
#2 задание принимает строку и возвращает кол=во гласных
def count_vowels(text):
    vowels=set ("аеоиуыяюёэaeoiuAEIOUАОЭЮЯИЁЕЫУ")
    return sum(1 for char in text if char in vowels)
print(count_vowels("Привет, Мир"))
#3 задание  чтобы получить новый список содержащие только числа кратные 5
numbers=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda i:i%5==0, numbers))
print(result)
#4 задание чтобы получить слова которые будут находится в верхнем регистре
spisok=["молоко", "хлеб", "печенье", "вода", "мука"]
spisok_lambda=list(map(lambda spisok:spisok.upper(),spisok))
print(spisok_lambda)
