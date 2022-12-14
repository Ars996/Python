import logging
import pathlib
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from configparser import ConfigParser
from logic import get_list_elements, mass_operation, doing_simple


BOT_DIR = pathlib.Path(__file__).parent
config = ConfigParser()
config.read(BOT_DIR / 'bot.conf', encoding='utf-8')

TOKEN = config.get('bot', 'TOKEN')
MY_LINK = config.get('bot', 'LINK')

# Configure logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Этот handler будет вызыван когда пользователь отправит
    команду `/start` или `/help`
    """
    await message.reply(
        f"Привет!\nЯ EchoBot!\nОтправь ссылку на меня друзьям {MY_LINK}.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open(BOT_DIR / 'media/approval.png', 'rb') as picture:
        await message.reply_photo(picture, caption='Согласовано 😺')


@dp.message_handler()
async def main(message: types.Message):
    expression: str = message.text
    arr = get_list_elements(expression)
    arr = doing_simple(arr)
    result = mass_operation(arr)
    await message.answer(f'Результат выражения\n{expression}={result}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)