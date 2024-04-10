import random
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types
from services import get_random, get_pong, calculate_expression
import asyncio
# Токен вашего бота
TOKEN = '6851010287:AAGvSeH7KGz_kMrX7nXPgF6byg14wcUA7cw'

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /random - выдает рандомное число от 1 до 100
@dp.message(Command("random"))
async def random_number(message: types.Message):
    random_num = get_random(1 , 100)
    await message.reply(f"Ваше рандомное число: {random_num}")

# Команда /dice - выдает результат броска кубика
@dp.message(Command("dice"))
async def roll_dice(message: types.Message):
    dice_result = get_random()
    await message.reply(f"Вы бросили кубик и получили: {dice_result}")

# Команда /ping - выдает "pong"
@dp.message(Command("ping"))
async def ping(message: types.Message):
    await message.reply(f"{get_pong()}")

# Команда /ping - выдает "pong"
@dp.message(Command("math"))
async def math(message: types.Message):
    await message.reply(f"{calculate_expression(message.text.replace("/math" , ""))}")

async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())