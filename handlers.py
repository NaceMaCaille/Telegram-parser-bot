from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import keyboards as kb

from config import CHANNELS
from parser import get_air_warning_message

router = Router()


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(
                 'Цей бот використовується для повідомлення о '
                 'повітряних тривогах.\nЯкщо потрібно дізнатися '
                 'інформацію про повітряну тривогу /info або кнопка на клавіатурі.', 
                 reply_markup= kb.main)


@router.message(Command('info'))
async def info_air(message: Message):
    res = []
    for channel in CHANNELS:
        texts = await get_air_warning_message(channel)
        for text in texts:
            res.append(f'Канал {channel} повідомляє:\n{text}')
    if res:
        await message.answer("\n\n".join(res), reply_markup= kb.button1)
    else:
        await message.answer("Зараз тихо", reply_markup= kb.button)
        
        
@router.callback_query(F.data == 'info')
async def info(callback: CallbackQuery):
    await callback.answer()
    await info_air(callback.message)
    
@router.message(F.text == 'Інфо Чернігів/область')
async def button_info(message: Message):
    await info_air(message)