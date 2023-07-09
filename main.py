from gtts import gTTS
import aiogram as ag
from config import token

tts = gTTS("hello")
tts.save('hola.mp3')
tts.GOOGLE_TTS_HEADERS

bot = ag.Bot(token=token)
dp = ag.Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def process_help_command(message: ag.types.Message):
    await bot.send_voice(message.from_user.id, open('hola.mp3', 'rb'))


@dp.message_handler()
async def echo_message(msg: ag.types.Message):
    tts = gTTS(f"{msg.text}")
    tts.save('hola.mp3')
    await bot.send_voice(msg.from_user.id, open('hola.mp3', 'rb'))
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    ag.executor.start_polling(dp)
