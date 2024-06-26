import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config

#Запуск логирования
logging.basicConfig(level=logging.INFO)
#Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
#Диспетчер
dp = Dispatcher()

#Хэндлер на start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
	await message.answer("Hello!")


#Хэндлер на test1
@dp.message(Command("answer"))
async def cmd_test1(massage: types.Message):
	await massage.answer("Простой ответ")

#Хэндлер на test1
@dp.message(Command("reply"))
async def cmd_test2(massage:types.Message):
	await massage.reply("Ответ с ответом")


#Запуск процесса пулинга
async def main():
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())

