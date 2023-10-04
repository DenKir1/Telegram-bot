import asyncio
import requests
from aiogram import Bot, types, Dispatcher
from config import Rapidtoken, tokenTele


dp = Dispatcher()


@dp.message()
async def send(message: types.Message):
	url = "https://open-ai21.p.rapidapi.com/conversationgpt35"
	payload = {
		"messages": [
			{
				"role": "user",
				"content": message
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

	await message.answer(response.json()['BOT'])


async def main():
	bot = Bot(tokenTele)
	await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())

