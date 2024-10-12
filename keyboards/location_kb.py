from aiogram.utils.keyboard import ReplyKeyboardBuilder

def locationKB():
    kb = ReplyKeyboardBuilder()
    kb.button(text=f"Отправить геолокацию", request_location=True)
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)