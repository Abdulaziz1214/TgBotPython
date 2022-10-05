import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text

from config import *
from keyboards import *

loop = asyncio.new_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

help_message = text(
    "Это урок по клавиатурам.",
    "Доступные команды:\n",
    "/start - приветствие",
    "\nШаблоны клавиатур:",
    "/hi1 - авто размер",
    "/hi2 - скрыть после нажатия",
    "/hi3 - больше кнопок",
    "/hi4 - кнопки в ряд",
    "/hi5 - больше рядов",
    "/hi6 - запрос локации и номера телефона",
    "/hi7 - все методы"
    "/rm - убрать шаблоны",
    "\nИнлайн клавиатуры:",
    "/1 - первая кнопка",
    "/2 - сразу много кнопок",
    sep="\n"
)


if __name__ == "__main__":
   from handlers import *
   executor.start_polling(dp, skip_updates=True)