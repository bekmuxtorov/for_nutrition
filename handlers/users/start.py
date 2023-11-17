from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, BASE_DIR, bot
from utils import define, get_nutrients, create_text, send_message_to_admin
from data.config import ADMINS
import os


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alekum, {message.from_user.full_name}!\n\nBotga xush kelibsiz!")
    await message.answer(f"📸 Mahsulotni suratini yuboring!")
    await send_message_to_admin(message.from_user, "start")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def resive_photo(message: types.Message):
    file_path = str(os.path.join(BASE_DIR, "uploads",
                                 f"{message.from_user.id}_{message.message_id}.png"))
    await message.photo[-1].download(
        destination_file=file_path,
    )
    await send_message_to_admin(message.from_user, "send image")

    name, score = await define(file_path)
    datas = await get_nutrients(name)
    text = await create_text(name, datas)

    if text:
        await message.answer(text=text)
    else:
        await message.answer(text="❌ Ma'lumot topilmadi!")

    os.remove(file_path)
