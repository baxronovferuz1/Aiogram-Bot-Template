from aiogram import types
from loader import dp,bot
from aiogram.dispatcher.filters import Text
from instagram import instadownLoader
@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def send_media(message:types.Message):
    link=message.text
    data=instadownLoader(link=link)
    if data=="Bad request":
        await message.answer("Bu url orqali hech narsa topilmadi!")
    else:
        if data["type"]=="image":
            await message.answer_photo(photo=data["media"])
        elif data["type"]=="video":
            await message.answer_video(video=data["media"])
        elif data["type"]=="carousel":
            for i in data["media"]:
                await message.answer_document(document=i)
        else:
            await message.answer("Bu url orqali hech narsa topilmadi!")


