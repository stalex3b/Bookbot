from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def send_any_msg(message: Message):
    await message.answer(f'сообщение: {message.text} не распознано как команда')