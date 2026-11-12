import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# ========== НАСТРОЙКИ ==========
# Токен берём из переменной окружения (BOT_TOKEN), иначе — из константы
TOKEN = os.getenv("BOT_TOKEN", "8446266058:AAGDv4xvk_3xQWFDegWLFqUWz7j7hpdAz0k")
OWNER = "@vasabik335"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_status_emoji(in_stock: bool) -> str:
    return "✅" if in_stock else "❌"

# ========== СТАРТ ==========
@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 КАТАЛОГ", callback_data="catalog")],
        [InlineKeyboardButton(text="📞 КОНТАКТЫ", callback_data="contacts"),
         InlineKeyboardButton(text="❓ ПОМОЩЬ", callback_data="help")]
    ])
    text = (
        "👋 <b>Добро пожаловать в SmokyRooom!</b>\n\n"
        "🛒 Здесь вы найдёте:\n"
        "💧 Жидкости\n"
        "🔧 Подики\n"
        "⚙️ Расходники\n"
        "🚬 Одноразки\n\n"
        "Выберите раздел ниже 👇"
    )
    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")

# ========== КАТАЛОГ ==========
@dp.callback_query(lambda c: c.data == "catalog")
async def catalog_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💧 ЖИДКОСТИ", callback_data="liquids"),
         InlineKeyboardButton(text="🔧 ПОДИКИ", callback_data="pods")],
        [InlineKeyboardButton(text="⚙️ РАСХОДНИКИ", callback_data="consumables"),
         InlineKeyboardButton(text="🚬 ОДНОРАЗКИ", callback_data="disposables")],
        [InlineKeyboardButton(text="🏠 ГЛАВНОЕ", callback_data="back_main")]
    ])
    await call.message.edit_text(
        "📋 <b>Каталог</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "Выберите категорию:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# ========== УНИВЕРСАЛЬНЫЙ ОБРАБОТЧИК ТОВАРА ==========
@dp.callback_query(lambda c: c.data.startswith("item_"))
async def item_handler(call: types.CallbackQuery):
    # формат: item_<категория>_<название>_<цена>_<наличие 1/0>
    parts = call.data.split("_", 4)
    category = parts[1]
    name = parts[2]
    price = parts[3]
    in_stock = parts[4] == "1"

    status_text = "✅ В наличии" if in_stock else "❌ Нет в наличии"
    text = (
        f"🛒 <b>{name}</b>\n"
        f"━━━━━━━━━━━━━━━\n"
        f"💰 Цена: <b>{price} ₽</b>\n"
        f"📦 Статус: {status_text}\n\n"
        f"Нажмите кнопку ниже, чтобы связаться с продавцом:"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать продавцу", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data=category)]
    ])
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")

# ========== СПИСОК ЖИДКОСТЕЙ ==========
@dp.callback_query(lambda c: c.data == "liquids")
async def liquids_handler(call: types.CallbackQuery):
    items = [
        ("Joker 7%", 600, False),
        ("Подонки critical 7%", 600, False),
        ("Грех/истерика 5%", 500, False),
        ("Annima love 6%", 550, False),
        ("Дуал 5%", 500, False),
        ("Рик и Морти кислые 5%", 500, False),
        ("Анархия 6%", 550, False),
        ("Мэд/самоубица 7%", 600, False),
        ("Флэш 3%", 450, False),
    ]
    buttons = []
    for name, price, in_stock in items:
        cb = f"item_liquids_{name}_{price}_{1 if in_stock else 0}"
        buttons.append([
            InlineKeyboardButton(
                text=f"{get_status_emoji(in_stock)} {name} — {price} ₽",
                callback_data=cb[:64]  # лимит callback_data = 64 байта
            )
        ])
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="catalog")])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await call.message.edit_text(
        "💧 <b>Жидкости</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "Выберите товар:\n\n"
        "✅ — в наличии\n"
        "❌ — нет в наличии",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# ========== ПОДИКИ ==========
@dp.callback_query(lambda c: c.data == "pods")
async def pods_handler(call: types.CallbackQuery):
    items = [
        ("Xros 5", 2850, True),
        ("Xros 5 мини", 2500, False),
        ("Pasito 2", 3600, False),
        ("Aegis boost 3", 4600, True),
        ("Пасито 3", 4600, False),
        ("Аегис Хиро 5", 4500, False),
    ]
    buttons = []
    for name, price, in_stock in items:
        cb = f"item_pods_{name}_{price}_{1 if in_stock else 0}"
        buttons.append([
            InlineKeyboardButton(
                text=f"{get_status_emoji(in_stock)} {name} — {price} ₽",
                callback_data=cb[:64]
            )
        ])
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="catalog")])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await call.message.edit_text(
        "🔧 <b>Подики</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "Выберите товар:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# ========== РАСХОДНИКИ ==========
@dp.callback_query(lambda c: c.data == "consumables")
async def consumables_handler(call: types.CallbackQuery):
    items = [
        ("Картридж хрос 0,4", 300, True),
        ("Картридж хрос 0,6", 300, True),
        ("Картридж аегис нано", 350, True),
        ("Испаритель пасито 50-65в", 300, True),
        ("Испаритель буст серии", 300, True),
        ("Испаритель манто", 300, True),
    ]
    buttons = []
    for name, price, in_stock in items:
        cb = f"item_consumables_{name}_{price}_{1 if in_stock else 0}"
        buttons.append([
            InlineKeyboardButton(
                text=f"{get_status_emoji(in_stock)} {name} — {price} ₽",
                callback_data=cb[:64]
            )
        ])
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="catalog")])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await call.message.edit_text(
        "⚙️ <b>Расходники</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "Выберите товар:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# ========== ОДНОРАЗКИ ==========
@dp.callback_query(lambda c: c.data == "disposables")
async def disposables_handler(call: types.CallbackQuery):
    items = [
        ("Подонки малезиан 12000 тяг", 1600, False),
        ("Рик и Морти зомби 23000 тяг", 2000, False),
        ("Рик и Морти на замерзоне кислые 20000 тяг", 1800, False),
    ]
    buttons = []
    for name, price, in_stock in items:
        cb = f"item_disposables_{name}_{price}_{1 if in_stock else 0}"
        buttons.append([
            InlineKeyboardButton(
                text=f"{get_status_emoji(in_stock)} {name} — {price} ₽",
                callback_data=cb[:64]
            )
        ])
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="catalog")])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await call.message.edit_text(
        "🚬 <b>Одноразки</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "Выберите товар:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# ========== КОНТАКТЫ ==========
@dp.callback_query(lambda c: c.data == "contacts")
async def contacts_handler(call: types.CallbackQuery):
    text = (
        "📞 <b>Контакты</b>\n"
        "━━━━━━━━━━━━━━━\n\n"
        f"👤 Продавец: {OWNER}\n\n"
        "Напишите нам для заказа или консультации."
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
    ])
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")

# ========== ПОМОЩЬ ==========
@dp.callback_query(lambda c: c.data == "help")
async def help_handler(call: types.CallbackQuery):
    text = (
        "❓ <b>Помощь</b>\n"
        "━━━━━━━━━━━━━━━\n\n"
        "1️⃣ Откройте «Каталог»\n"
        "2️⃣ Выберите категорию\n"
        "3️⃣ Нажмите на товар\n"
        "4️⃣ Свяжитесь с продавцом\n\n"
        "✅ — товар в наличии\n"
        "❌ — товар отсутствует"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")]
    ])
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")

# ========== НАЗАД В ГЛАВНОЕ ==========
@dp.callback_query(lambda c: c.data == "back_main")
async def back_main_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 КАТАЛОГ", callback_data="catalog")],
        [InlineKeyboardButton(text="📞 КОНТАКТЫ", callback_data="contacts"),
         InlineKeyboardButton(text="❓ ПОМОЩЬ", callback_data="help")]
    ])
    await call.message.edit_text(
        "🏠 <b>Главное меню</b>\n\nВыберите действие:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# ========== ЗАПУСК ==========
async def main():
    logging.info("🚀 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
