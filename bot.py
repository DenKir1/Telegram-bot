
import requests
from aiogram import Bot, types, Dispatcher, executor
from config import Rapidtoken, tokenTele

bot = Bot(tokenTele)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
	await message.answer(f'Добро пожаловать в чат семьи Кирдянкиных {message.from_user.first_name}')


@dp.message_handler()
async def send(message: types.Message):
	url = "https://open-ai21.p.rapidapi.com/conversationgpt35"
	payload = {
		"messages": [
			{
				"role": "user",
				"content": message.text
			}
		],
		"web_access": False,
		"stream": False
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": Rapidtoken,
		"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
	}

	response = requests.post(url, json=payload, headers=headers)
	res = response.json()['BOT']
	await message.answer(res)

executor.start_polling(dp)


