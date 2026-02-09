import logging
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# ========== ВАШИ НАСТРОЙКИ ==========
TOKEN = os.getenv("BOT_TOKEN", "8446266058:AAFqzp4C9X5FHFQydp_2w2f2k1CwsW3nEK4")
OWNER = os.getenv("OWNER_USERNAME", "@vasabik335")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ========== КОМАНДА /start ==========
@dp.message(Command("start"))
async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Каталог товаров", callback_data="catalog")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")]
    ])
    
    text = "👋 Приветствую!\nТут ты можешь выбрать интересующие тебя товары,\nудачных покупок!"
    await message.answer(text, reply_markup=keyboard)

# ========== КАТАЛОГ ==========
@dp.callback_query(lambda c: c.data == "catalog")
async def catalog_handler(call: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💧 Жидкости", callback_data="liquids")],
        [InlineKeyboardButton(text="🔧 Подики", callback_data="pods")],
        [InlineKeyboardButton(text="⚙️ Расходники", callback_data="consumables")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
    ])
    await call.message.edit_text("📋 Выберите категорию:", reply_markup=keyboard)

# ========== ЖИДКОСТИ ==========
@dp.callback_query(lambda c: c.data == "liquids")
async def liquids_handler(call: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Дуал 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Рик и Морти кислые 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Анархия 6% - 550 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Мэд/самоубица 7% - 600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Флэш 3% - 450 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Подонки критикал 7% - 550 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Истерика/грех 5% - 550 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ Назад в каталог", callback_data="catalog")]
    ])
    await call.message.edit_text("💧 Выберите жидкость:", reply_markup=keyboard)

# ========== ПОДИКИ ==========
@dp.callback_query(lambda c: c.data == "pods")
async def pods_handler(call: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Хрос 5 - 3000 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Хрос 5 мини - 2500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Пасито 3 - 4600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Аегис буст 3 - 5600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Аегис Хиро 5 - 4500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ Назад в каталог", callback_data="catalog")]
    ])
    await call.message.edit_text("🔧 Выберите подик:", reply_markup=keyboard)

# ========== РАСХОДНИКИ ==========
@dp.callback_query(lambda c: c.data == "consumables")
async def consumables_handler(call: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Картридж хрос 0,4 - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Картридж хрос 0,6 - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Картридж аегис нано - 350 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Испаритель пасито 50-65в - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Испаритель буст серии - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="Испаритель манто - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ Назад в каталог", callback_data="catalog")]
    ])
    await call.message.edit_text("⚙️ Выберите расходник:", reply_markup=keyboard)

# ========== КОНТАКТЫ ==========
@dp.callback_query(lambda c: c.data == "contacts")
async def contacts_handler(call: CallbackQuery):
    text = f"📞 Контакты\n\nВладелец магазина: {OWNER}\n\nДля заказа нажмите на товар в каталоге"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
    ])
    await call.message.edit_text(text, reply_markup=keyboard)

# ========== ПОМОЩЬ ==========
@dp.callback_query(lambda c: c.data == "help")
async def help_handler(call: CallbackQuery):
    text = """❓ Помощь

1. Выберите категорию товара
2. Нажмите на нужный товар
3. Вы перейдете к продавцу
4. Уточните детали покупки

Если кнопка не работает, напишите продавцу напрямую"""
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
    ])
    await call.message.edit_text(text, reply_markup=keyboard)

# ========== НАЗАД В ГЛАВНОЕ ==========
@dp.callback_query(lambda c: c.data == "back_main")
async def back_main_handler(call: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Каталог товаров", callback_data="catalog")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")]
    ])
    await call.message.edit_text("👋 Главное меню:", reply_markup=keyboard)

# ========== ЗАПУСК БОТА ==========
async def main():
    logging.info("🚀 Бот запущен на BotHost 24/7!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
