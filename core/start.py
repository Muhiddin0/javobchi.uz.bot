from loader import dp
from aiogram import types
from .users import create_user

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
        /start Commandasi uchun functsiya
    """
    user = message.from_user
    create_user(user_id=user.id, first_name=user.first_name, user_name=user.username)
    await message.answer(f"👋 Assalomu Alekum {user.first_name} aka\n @javobchiuzb_bot Sizga muntazir \n\nChat uchun menga yozing\nRasim uchun '/' Belgisdan so'ng kerakli commanda nomini yozing va undan so'ng xizmat uchun kerakli matini yozing")
    await message.answer(f"Misol uchun\n\n `/image creative pandas vilage`", parse_mode='MarkdownV2')