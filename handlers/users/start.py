from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"🔥Assalomu alaykum, {message.from_user.full_name}, @save_insta_utube_bot botga xush kelipsiz.Bot orqali quyidagilarni yuklab olishingiz mumkin: \n \n •Instagram funksiyasi: video,photo,carousel postlar \n \n •YouTube funksiyasi:videoni audio formatda qaytaradi \n \n 🚀 Media yuklashni boshlash uchun uning havolasini yuboring. \n 😎 Bot guruhlarda ham ishlay oladi! \n \n Aloqa uchun:@Baxronov_Feruz")
# from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
# from pyrogram import Client,filters,StopPropagation
# from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

# @Client.on_message(filters.command(["start"]), group=-2)
# async def start(client, message):
#     # return
#     joinButton = InlineKeyboardMarkup([
#         [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
#         [InlineKeyboardButton(
#             "Report Bugs 😊", url="https://t.me/aryanvikash")]
#     ])
#     welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
#     await message.reply_text(welcomed, reply_markup=joinButton)
#     raise StopPropagation