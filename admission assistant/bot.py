import asyncio
import sqlite3
import os
from dotenv import load_dotenv
from database import (
    save_user,
    get_user,
    search_university,
    get_universities_by_country
)
from aiogram import Bot, Dispatcher, F
from aiogram import F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
load_dotenv()
TOKEN=os.getenv("BOT_TOKEN")
bot=Bot(token=TOKEN)
dp=Dispatcher()
main_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏫 Universities"),
            KeyboardButton(text="📃 My applications")
        ],
        [
            KeyboardButton(text="💼 Documents"),
            KeyboardButton(text="🗓️ Deadlines")
        ],
        [
            KeyboardButton(text="💵 Scholarship"),
            KeyboardButton(text="👤 Profile")
        ]
    ],
    resize_keyboard=True
)
class ProfileState(StatesGroup):
    waiting_for_name=State()
    waiting_for_age=State()
    waiting_for_city=State()
    waiting_for_major=State()
    waiting_for_countries=State()
class UniversityState(StatesGroup):
    waiting_for_university=State()
    waiting_for_country=State()
@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(
        "🎓 Welcome to Admission Assistant!\n\n"
        "Я помогу тебе в подготовке для поступления заграницу.\n\n "
        "Выбери нужный раздел 👇",
        reply_markup=main_menu
    )
@dp.message(F.text == "👤 Profile")
async def profile(message: Message):
   
    user = get_user(message.from_user.id)
    if user is None:
        await message.answer(
            "👤 Your Profile\n\n"
            "Профиль пока пустой.\n"
            "Let's create your profile! 👇",
            reply_markup=profile_menu
        )
        return
    name, age, city, major, countries = user

    await message.answer(
        "👤 Your Profile\n\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"City: {city}\n"
        f"Intended major: {major}\n"
        f"Target countries: {countries}"
    )
country_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇸 USA"),
            KeyboardButton(text="🇮🇹 Italy")
        ],
        [
            KeyboardButton(text="🇩🇪 Germany"),
            KeyboardButton(text="🇪🇸 Spain")
        ],
        [
            KeyboardButton(text="🔙 Back")
        ]
    ],
    resize_keyboard=True
)
universities_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎 Search university")
        ],
        [
            KeyboardButton(text="🌍 Browse by country"),
            KeyboardButton(text="🎓 Browse by major")
        ],
        [
            KeyboardButton(text="🔙 Back")
        ]
    ],
    resize_keyboard=True
)
@dp.message(F.text=="🔙 Back")
async def back_to_main(message:Message):
    await message.answer(
        "Главное меню 👇",
        reply=main_menu
    )
@dp.message(F.text=="🏫 Universities")
async def universities(message:Message):
    await message.answer(
        "🏫 Universities\n\n"
        "Здесь ты можешь найти университеты"
        " по стране или специальности.",
        reply_markup=universities_menu
    )
@dp.message(F.text=="🔎 Search university")
async def search_university_start(message:Message,state:FSMContext):
    await state.set_state(UniversityState.waiting_for_university)
    await message.answer(
        "🔎 Введите название университета на английском языке:"
    )
@dp.message(F.text == "🌍 Browse by country")
async def browse_by_country(message: Message, state: FSMContext):
    await state.set_state(UniversityState.waiting_for_country)

    await message.answer(
        "🌍 Choose a country:",
        reply_markup=country_menu
    )

@dp.message(UniversityState.waiting_for_university)
async def university_search(message:Message,state:FSMContext):
    results=search_university(message.text)
    if not results:
        await message.answer(
            "❌ University not found.\n\n"
            "Try another name."
        )
        return
    for university in results:
        name,country,city,major,website=university
        await message.answer(
            f"🏫 {name}\n\n"
            f"🌍 Country: {country}\n"
            f"📍 City: {city}\n"
            f"🎓 Major: {major}\n"
            f"🌐 Website: {website}"
        )
    await state.clear()
@dp.message(UniversityState.waiting_for_country)
async def get_country(message: Message, state: FSMContext):
    print("USER CHOSE:", repr(message.text))

    countries = {
        "🇺🇸 USA": "USA",
        "🇮🇹 Italy": "Italy",
        "🇩🇪 Germany": "Germany",
        "🇪🇸 Spain": "Spain"
    }

    country = countries.get(message.text)

    if country is None:
        await message.answer(
            "❌ I don't understand this country."
        )
        return

    universities = get_universities_by_country(country)

    print("FOUND:", universities)

    if not universities:
        await message.answer(
            f"❌ No universities found in {country}."
        )
        await state.clear()
        return

    for university in universities:
        name, country, city, major, website = university

        await message.answer(
            f"🏫 {name}\n\n"
            f"🌍 Country: {country}\n"
            f"📍 City: {city}\n"
            f"🎓 Major: {major}\n"
            f"🌐 Website: {website}"
        )

    await state.clear()
@dp.message(F.text=="➕ Create profile")
async def create_profile(message:Message,state:FSMContext):
    await state.set_state(ProfileState.waiting_for_name)
    await message.answer(
        "👋 Как тебя зовут?"
    )
@dp.message(ProfileState.waiting_for_name)
async def get_name(message:Message,state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ProfileState.waiting_for_age)
    await message.answer(
        f"Приятно познакомиться, {message.text}! 😊 \n\n"
        "Сколько тебе лет?"
    )
@dp.message(ProfileState.waiting_for_age)
async def get_age(message:Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            "Пожалуйста введите свой возраст."
        )
        return
    await state.update_data(age=int(message.text))
    await state.set_state(ProfileState.waiting_for_city)
    await message.answer(
        "📍 В каком городе ты живешь?"
    )
@dp.message(ProfileState.waiting_for_city)
async def get_city(message:Message, state:FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(ProfileState.waiting_for_major)
    await message.answer(
        "🎓 Какую специальность ты хочешь изучать?"
    )
@dp.message(ProfileState.waiting_for_major)
async def get_major(message:Message,state:FSMContext):
    await state.update_data(major=message.text)
    await state.set_state(ProfileState.waiting_for_countries)
    await message.answer(
        "В каких странах ты хотел/а бы учиться?\n\n"
        "Можно писать несколько стран запятой.\n"
        "Например: США, Италия, Германия."
    )
@dp.message(ProfileState.waiting_for_countries)
async def get_countries(message:Message,state:FSMContext):
    countries=[
        country.strip()
        for country in message.text.split(",")
    ]
    await state.update_data(countries=countries)
    data=await state.get_data()
    save_user(
        telegram_id=message.from_user.id,
        name=data["name"],
        age=data["age"],
        city=data["city"],
        major=data["major"],
        countries=data["countries"]
    )
    await message.answer(
        "🎉 Ваша анкета заполнена!\n\n"
        f"👤 Имя: {data['name']}\n"
        f"🎂 Возраст: {data['age']}\n"
        f"🌍 Город проживания: {data['city']}\n"
        f"🎓 Выбранная специальность: {data['major']}\n"
        f"✈️ Страны для поступления: {','.join(data['countries'])}"
    )
    await state.clear()
profile_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Create profile")

        ],
        [
            KeyboardButton(text="🔙 Back")
        ]
    ],
    resize_keyboard=True
)

async def main():
    await dp.start_polling(bot)
if __name__=="__main__":
    asyncio.run(main())
    