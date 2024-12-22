import logging
from aiogram import Bot,Dispatcher,types
from aiogram.filters import CommandStart,Command
from dotenv import load_dotenv
import os
import sys
import asyncio
# connecting with the telegram bot
load_dotenv()
API_TOKEN = os.getenv("TOKEN")
#print(API_TOKEN)

logging.basicConfig(level=logging.INFO)

# initialize bot and dispatcher
dp = Dispatcher()

@dp.message(Command(commands=['help','start']))
async def command_start_handler(message: types.Message):
    """
    This handler recieves messages with '/start' or '/help' command
    """
    await message.answer("Hi\nI am Echo Bot!\nPowered by aiogram")

@dp.message()
async def generic_greetings_handler(message: types.Message):
    if message.text.lower() in ['hi','hello']:
        await message.answer("Hi\nI am Echo Bot!\nPowered by aiogram")

async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    asyncio.run(main())
