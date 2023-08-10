from aiogram import Bot, Dispatcher, executor, types
import os

from aiogram.types import CallbackQuery
from dotenv import load_dotenv
from keyboard import kb
from anekdots import jokas_pars
from days import hollyd_pars


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)
anekdot_lst = jokas_pars()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, привет! Повысыть настроение помоооооожет одна из кнопок.',
                         reply_markup=kb)


@dp.message_handler()
async def reply(message: types.Message):
    await message.reply('Я не искусственный интеллект. Жми на экранные кнопки.', reply_markup=kb)


@dp.callback_query_handler(text_contains='anekdot')
async def joka(call: CallbackQuery):
    await call.message.answer(f'{anekdot_lst[0]}', reply_markup=kb)
    del anekdot_lst[0]


@dp.callback_query_handler(text_contains='day')
async def hollyday(call: CallbackQuery):
    await call.message.answer(f'Сегодня {hollyd_pars()}', reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp)
