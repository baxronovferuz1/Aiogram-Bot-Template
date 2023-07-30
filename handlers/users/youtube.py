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




from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from io import BytesIO

@dp.message_handler(Text(startswith="http"))
async def get_audio(message: types.Message):
    link = message.text

    try:
        # Validate the YouTube URL
        youtube = YouTube(link)

        # Check if an audio stream is available
        audio_stream = youtube.streams.filter(only_audio=True).first()

        if audio_stream:
            buffer = BytesIO()
            audio_stream.stream_to_buffer(buffer=buffer)
            buffer.seek(0)

            # Extract the title of the video as the caption
            filename = youtube.title

            await message.answer_audio(audio=buffer, caption=filename)
        else:
            await message.answer("Sorry, the provided URL does not contain any audio.")
    except Exception as e:
        # Handle any exceptions that might occur
        await message.answer(f"An error occurred: {str(e)}")
