from aiogram import Bot, Dispatcher, executor, types
from rich.logging import RichHandler
import logging
import requests
import config

FORMAT = "%(message)s"
logging.basicConfig(
	level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
	)

# https://api.telegram.org/bot<token>/METHOD_NAME

user1 = requests.post(f'https://api.telegram.org/bot{config.TOKEN}/getChat?chat_id={config.USER_ID_1}').json()
user2 = requests.post(f'https://api.telegram.org/bot{config.TOKEN}/getChat?chat_id={config.USER_ID_1}').json()

log = logging.getLogger("rich")
log.info(f"USER_1: {user1['result']['first_name']} @{user1['result']['username']} {config.USER_ID_1}")
log.info(f"USER_2: {user2['result']['first_name']} @{user2['result']['username']} {config.USER_ID_2}")

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	if message.from_user.id == config.USER_ID_1 or config.USER_ID_2:
		user_FirstName = message.from_user.first_name
		me_FirstName = await bot.get_me()
		me_FirstName = me_FirstName.first_name

		await message.answer(f"Здраствуйте {user_FirstName}, это <b>{me_FirstName}</b> бот")
		log.info(f"Start {user_FirstName}")
	else:
		log.error(f'satrting user: ID: {message.from_user.id}')
		await message.answer('Простите но этот бот вам не доступень!')



@dp.message_handler(content_types='text')
async def text(message: types.Message):
	msg = message.text

	if message.from_user.id == config.USER_ID_1:
		await bot.send_message(config.USER_ID_2, message.text)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_message(config.USER_ID_1, message.text)
	else:
		log.error(f'User: {message.from_user.first_name}\t{message.from_user.id}')



@dp.message_handler(content_types='sticker')
async def sticker(message: types.Message):
	sti = message.sticker.file_id

	if message.from_user.id == config.USER_ID_1:
		await bot.send_sticker(config.USER_ID_2, sti)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_sticker(config.USER_ID_1, sti)
	else:
		pass



@dp.message_handler(content_types='voice')
async def voi(message: types.Message):
	voi = message.voice.file_id

	if message.from_user.id == config.USER_ID_1:
		await bot.send_voice(config.USER_ID_2, voi)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_voice(config.USER_ID_1, voi)
	else:
		pass



@dp.message_handler(content_types='audio')
async def aud(message: types.Message):
	aud = message.audio.file_id

	if message.from_user.id == config.USER_ID_1:
		await bot.send_audio(config.USER_ID_2, audio)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_audio(config.USER_ID_1, audio)
	else:
		pass



@dp.message_handler(content_types='photo')
async def photo(message: types.Message):
	pho = message.photo[0].file_id

	if message.from_user.id == config.USER_ID_1:
		await bot.send_photo(config.USER_ID_2, pho)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_photo(config.USER_ID_1, pho)
	else:
		pass



@dp.message_handler(content_types='video')
async def video(message: types.Message):
	vid = message.video.file_id

	if message.from_user.id == config.USER_ID_1:
		await bot.send_video(config.USER_ID_2, vid)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_video(config.USER_ID_1, vid)
	else:
		pass



@dp.message_handler(content_types='video_note')
async def video_note(message: types.Message):
	vin = message.video_note.file_id

	if message.from_user.id == config.USER_ID_1:
		await bot.send_video_note(config.USER_ID_2, vin)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_video_note(config.USER_ID_1, vin)
	else:
		pass



@dp.message_handler(content_types='location')
async def location(message: types.Message):
	loc = [message.location.latitude, message.location.longitude]

	if message.from_user.id == config.USER_ID_1:
		await bot.send_location(config.USER_ID_2, latitude=loc[0], longitude=loc[1])
		print(f'USER_1: https://maps.google.com/maps?q={loc[0]},{loc[1]}0&ll={loc[0]},{loc[1]}0&z=16')
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_location(config.USER_ID_1, latitude=loc[0], longitude=loc[1])
		print(f'USER_2: https://maps.google.com/maps?q={loc[0]},{loc[1]}0&ll={loc[0]},{loc[1]}0&z=16')
	else:
		pass


@dp.message_handler(content_types='document')
async def document(message: types.Message):
	doc = message.document.file_id

	if message.from_user.id == config.USER_ID_1:
		await bot.send_document(config.USER_ID_2, doc)
	elif message.from_user.id == config.USER_ID_2:
		await bot.send_document(config.USER_ID_1, doc)
	else:
		pass



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)