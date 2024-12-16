from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "5300888482:AAG48qrnvpQI-QWLyiJ_N6hlIiOC6E57d8A"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button3 = KeyboardButton(text="Купить")
rkm = ReplyKeyboardMarkup(resize_keyboard=True).row(button, button2)
rkm2 = ReplyKeyboardMarkup(resize_keyboard=True)
rkm.add(button3)

in_button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
in_button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
in_button3 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
in_button4 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
in_button5 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
in_button6 = InlineKeyboardButton(text="Product4", callback_data="product_buying")
inrkm = InlineKeyboardMarkup(resize_keyboard=True).row(in_button, in_button2)
inrkm2 = InlineKeyboardMarkup(resize_keyboard=True).row(in_button3, in_button4, in_button5, in_button6)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст: ")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост в (см): ")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес в (кг): ")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    await message.answer(f"Ваша норма калорий {result} ккал")
    await state.finish()

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию: ", reply_markup=inrkm)

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    with open("files/1.jpg", "rb") as img1:
        await message.answer_photo(img1, "Название: Смартфон | Описание: Раскладной смартфон | Цена: 100")
    with open("files/2.jpg", "rb") as img2:
        await message.answer_photo(img2, "Название: Брелок | Описание: Брелок детский | Цена: 200")
    with open("files/3.jpg", "rb") as img3:
        await message.answer_photo(img3, "Название: Инструменты | Описание: Набор инструменты | Цена: 300")
    with open("files/4.jpg", "rb") as img4:
        await message.answer_photo(img4, "Название: Канцелярия | Описание: Набор канцелярии | Цена: 400")
    await message.answer("Выберите продукт для покупки: ", reply_markup=inrkm2)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=rkm)

@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

