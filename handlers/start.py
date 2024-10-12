import os

from aiogram import types, Dispatcher, Router
from aiogram.client.session import aiohttp
from aiogram.types import Message, ContentType
from aiogram.filters import CommandStart
from aiogram import F

from keyboards.location_kb import locationKB
from models.user import get_db, User
from models.users_locations import UserLocation
from utils.async_db_connection import async_session
from utils.db_requests import add_user_to_db
from utils.location import getLocationFromCoordinates
from dotenv import load_dotenv

load_dotenv()
BOT_KEY = os.getenv('BOT_KEY')

dp = Dispatcher()
router = Router()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id

    # Добавление пользователя в базу данных
    try:
        response = add_user_to_db(telegram_id=user_id, name=user_name)
    except Exception as e:
        print(e)
    finally:
        await message.reply(
            f"Привет, {user_name}! Отправь мне пожалуйста свою локацию чтобы я мог присылать тебе данные о погоде <3",
            reply_markup=locationKB()
        )


@router.message(F.content_type == ContentType.LOCATION)
async def location(message: types.Message):
    if message.location is not None:
        # , state: FSMContext
        # await state.set_state(StartWithUser.accepting)
        lon = message.location.longitude
        lat = message.location.latitude
        await message.answer(f'Подождите пожалуйста')
        userLocation = getLocationFromCoordinates(TOKEN=os.getenv('GEOCODING_API_KEY'), longitude=lon, latitude=lat)

        if userLocation:  # Проверяем, что локация успешно получена
            location_name = userLocation['addres']['city']

            # Используем get_db для получения сессии
            db = next(get_db())
            try:
                # Добавляем или обновляем пользователя в базе данных
                user = db.query(User).filter(User.telegram_id == message.from_user.id).first()
                if user:
                    # Если пользователь уже существует, обновляем его локацию
                    user.location = location_name
                else:
                    # Если пользователя нет, создаем новую запись
                    user = User(telegram_id=message.from_user.id, name=message.from_user.full_name,
                                location=location_name)
                    db.add(user)

                # Сохраняем изменения в базе данных
                db.commit()
                await message.answer(f'Ваша локация обновлена на: {location_name}')
            except Exception as e:
                await message.answer('Произошла ошибка при обновлении локации.')
                print(f'Ошибка: {e}')
            finally:
                db.close()
        else:
            await message.answer('Не удалось получить локацию из координат.')
    else:
        await message.answer('Локация не найдена.')

    await message.answer(f'Вы находитесь в: {location_name}! Спасибо за предоставленную информацию, теперь я могу предоставить тебе прогноз погоды!')