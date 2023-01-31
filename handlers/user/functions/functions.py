import handlers.user.makups.makups as nav

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from asyncio import sleep

from loader import dp, bot
from utils.sql_commands import register_user

from handlers.admin.makups.makups import mainMenu as adminMainMenu
from data.config.config import ADMINS_ID
from states.user import RegUser


# from utils.sql_commands import add_coin_user, get_user, send_result_ques, rank_counter
# from utils.Helper import Helper
# from csv import reader


@dp.message_handler(CommandStart(), state='*')
async def start_bot(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS_ID:
        await message.answer(
            'Привет, Владелец!', reply_markup=adminMainMenu
        )
        return

    await message.answer(
        'Привет!\nВведите свое имя и фамилию для регистрации'
    )

    await RegUser.reg_user.set()


@dp.message_handler(state=RegUser.reg_user, content_types=types.ContentType.TEXT)
async def reg_user(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)

    if (user := message.text.split(' ')).__len__() == 2:
        register_user(tg_id=message.from_user.id, first_name=user[0], second_name=user[1])
        await message.answer("Регистрация прошла успешно!", reply_markup=nav.mainMenu)

    else:
        await message.answer("Упс... Что-то пошло не так, попробуйте еще.")
