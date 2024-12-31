# pip install aiogram==2.25.1

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text = ['/start'])
async def urban_message(message):
    print("Start_message")
    await message.answer("Рады вас видеть в нашем боте!")


class UserState(StatesGroup):
    age = State() # возраст
    growth = State() # рост
    weight = State() # вес

@dp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    #result = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5

    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age'])
    await message.answer(f"Ваша норма калорий {result}:")
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


