import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# ========== ВАШИ НАСТРОЙКИ ==========
TOKEN = "8446266058:AAFqzp4C9X5FHFQydp_2w2f2k1CwsW3nEK4"
OWNER = "@vasabik335"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_status_emoji(in_stock: bool) -> str:
    return "✅" if in_stock else "❌"

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=" КАТАЛОГ", callback_data="catalog")],
        [InlineKeyboardButton(text=" КОНТАКТЫ", callback_data="contacts"),
         InlineKeyboardButton(text=" ПОМОЩЬ", callback_data="help")]
    ])
    
    text = "👋 Добро пожаловать в бот магазина SmokyRooom,приятных покупок!"
    await message.answer(text, reply_markup=keyboard)

@dp.callback_query(lambda c: c.data == "catalog")
async def catalog_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=" ЖИДКОСТИ", callback_data="liquids"),
         InlineKeyboardButton(text=" ПОДИКИ", callback_data="pods")],
        [InlineKeyboardButton(text=" РАСХОДНИКИ", callback_data="consumables"),
         InlineKeyboardButton(text=" ОДНОРАЗКИ", callback_data="disposables")],
        [InlineKeyboardButton(text=" ГЛАВНОЕ", callback_data="back_main")]
    ])
    await call.message.edit_text("📋 Каталог:", reply_markup=keyboard)

# ========== ЖИДКОСТИ ==========
@dp.callback_query(lambda c: c.data == "liquids")
async def liquids_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Joker 7% - 600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Грех/истерика 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Annima love 6% - 550 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Подонки critical 7% - 600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Дуал 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Рик и Морти кислые 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Анархия 6% - 550 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Мэд/самоубица 7% - 600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Флэш 3% - 450 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="catalog")]
    ])
    await call.message.edit_text("💧 Жидкости:", reply_markup=keyboard)

# ========== ПОДИКИ (НОВЫЕ ЦЕНЫ) ==========
@dp.callback_query(lambda c: c.data == "pods")
async def pods_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Xros 5 - 2850 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Xros 5 мини - 2500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Pasito 2 - 3600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Aegis boost 3 - 4600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Пасито 3 - 4600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Аегис Хиро 5 - 4500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="catalog")]
    ])
    await call.message.edit_text("🔧 Подики:", reply_markup=keyboard)

# ========== РАСХОДНИКИ ==========
@dp.callback_query(lambda c: c.data == "consumables")
async def consumables_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Картридж хрос 0,4 - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Картридж хрос 0,6 - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Картридж аегис нано - 350 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Испаритель пасито 50-65в - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Испаритель буст серии - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Испаритель манто - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="catalog")]
    ])
    await call.message.edit_text("⚙️ Расходники:", reply_markup=keyboard)

# ========== ОДНОРАЗКИ ==========
@dp.callback_query(lambda c: c.data == "disposables")
async def disposables_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Подонки малазиан 12000тяг - 1600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Рик и Морти зомби 23000тяг - 2000 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Рик и Морти на замерзоне кислые 20000тяг - 1800 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="catalog")]
    ])
    await call.message.edit_text("🚬 Одноразки:", reply_markup=keyboard)

# ========== КОНТАКТЫ ==========
@dp.callback_query(lambda c: c.data == "contacts")
async def contacts_handler(call: types.CallbackQuery):
    text = f"📞 Контакты\n\nПродавец: {OWNER}"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="back_main")]
    ])
    await call.message.edit_text(text, reply_markup=keyboard)

# ========== ПОМОЩЬ ==========
@dp.callback_query(lambda c: c.data == "help")
async def help_handler(call: types.CallbackQuery):
    text = "❓ Помощь\n\n1. Выберите товар\n2. Нажмите на кнопку\n3. Свяжитесь с продавцом"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="back_main")]
    ])
    await call.message.edit_text(text, reply_markup=keyboard)

# ========== НАЗАД В ГЛАВНОЕ ==========
@dp.callback_query(lambda c: c.data == "back_main")
async def back_main_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 КАТАЛОГ", callback_data="catalog")],
        [InlineKeyboardButton(text="📞 КОНТАКТЫ", callback_data="contacts"),
         InlineKeyboardButton(text="❓ ПОМОЩЬ", callback_data="help")]
    ])
    await call.message.edit_text("👋 Главное меню:", reply_markup=keyboard)

# ========== ЗАПУСК ==========
async def main():
    logging.info("🚀 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
