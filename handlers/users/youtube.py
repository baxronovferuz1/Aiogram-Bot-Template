# from aiogram import types

# from loader import dp
# from aiogram.dispatcher.filters import Text
# from pytube import YouTube

# @dp.message_handler(Text(startswith="http"))
# async def get_audio(message:types.Message):
#     link=message.text
#     from io import BytesIO
#     buffer=BytesIO()
#     url=YouTube(link)
#     if url.check_availability() is None:
#         audio=url.streams.get_audio_only()
#         audio.stream_to_buffer(buffer=buffer)
#         buffer.seek(0)
#         filename=url.title
#         await message.answer_audio(audio=buffer, caption=filename)
#     else:
#         await message.answer("Error")

import os
import logging
# import telegram
from pytube import YouTube

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# # Telegram Bot token
# TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# # Initialize the Telegram bot
# bot = telegram.Bot(token=TOKEN)


def download_audio(url):
    try:
        # Download YouTube video
        youtube = YouTube(url)
        video = youtube.streams.first()
        video.download('temp')
        
        # Extract audio from the downloaded video
        file_path = os.path.join('temp', video.default_filename)
        audio_path = os.path.splitext(file_path)[0] + '.mp3'
        os.system(f'ffmpeg -i "{file_path}" -vn -acodec libmp3lame "{audio_path}"')
        
        return audio_path
    except Exception as e:
        logger.error(f'Error downloading audio: {str(e)}')
        return None


# def handle_message(update, context):
#     message = update.message
#     chat_id = message.chat_id

    # Check if the message contains a YouTube video
