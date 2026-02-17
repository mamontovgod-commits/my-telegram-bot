import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ========== ВАШИ НАСТРОЙКИ ==========
TOKEN = "8446266058:AAFqzp4C9X5FHFQydp_2w2f2k1CwsW3nEK4"  # Ваш токен
OWNER = "@vasabik335"  # Ваш Telegram

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========
def get_status_emoji(in_stock: bool) -> str:
    """Возвращает эмодзи статуса наличия"""
    return "✅" if in_stock else "❌"

# ========== КОМАНДА /start ==========
@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 КАТАЛОГ ТОВАРОВ", callback_data="catalog")],
        [InlineKeyboardButton(text="📞 КОНТАКТЫ", callback_data="contacts"),
         InlineKeyboardButton(text="❓ ПОМОЩЬ", callback_data="help")]
    ])
    
    text = (
        "👋 <b>Добро пожаловать в магазин!</b>\n\n"
        "Здесь ты можешь выбрать:\n"
        "• 💧 Жидкости\n"
        "• 🔧 Подики\n"
        "• ⚙️ Расходники\n"
        "• 🚬 Одноразки\n\n"
        "<i>Статус товаров:</i>\n"
        "✅ - в наличии\n"
        "❌ - нет в наличии\n\n"
        "Приятных покупок!"
    )
    
    await message.answer(text, reply_markup=keyboard, parse_mode='HTML')

# ========== КАТАЛОГ ==========
@dp.callback_query(lambda c: c.data == "catalog")
async def catalog_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💧 ЖИДКОСТИ", callback_data="liquids"),
         InlineKeyboardButton(text="🔧 ПОДИКИ", callback_data="pods")],
        [InlineKeyboardButton(text="⚙️ РАСХОДНИКИ", callback_data="consumables"),
         InlineKeyboardButton(text="🚬 ОДНОРАЗКИ", callback_data="disposables")],
        [InlineKeyboardButton(text="🏠 ГЛАВНОЕ МЕНЮ", callback_data="back_main")]
    ])
    
    await call.message.edit_text(
        "📋 <b>КАТАЛОГ ТОВАРОВ</b>\n\nВыберите категорию:",
        reply_markup=keyboard,
        parse_mode='HTML'
    )

# ========== ЖИДКОСТИ ==========
@dp.callback_query(lambda c: c.data == "liquids")
async def liquids_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Грех/истерика 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Annima love 6% - 550 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Подонки critical 7% - 600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Дуал 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Рик и Морти кислые 5% - 500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Анархия 6% - 550 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Мэд/самоубица 7% - 600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Флэш 3% - 450 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД В КАТАЛОГ", callback_data="catalog")]
    ])
    
    text = (
        "💧 <b>ЖИДКОСТИ</b>\n\n"
        "✅ - в наличии\n"
        "❌ - нет в наличии\n\n"
        "<i>Нажмите на товар для связи с продавцом</i>"
    )
    
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode='HTML')

# ========== ПОДИКИ ==========
@dp.callback_query(lambda c: c.data == "pods")
async def pods_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Xros 5 - 3000 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Xros 5 мини - 2500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Pasito 2 - 3600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Aegis boost 3 - 5000 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Пасито 3 - 4600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(False)} Аегис Хиро 5 - 4500 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД В КАТАЛОГ", callback_data="catalog")]
    ])
    
    text = (
        "🔧 <b>ПОДИКИ</b>\n\n"
        "✅ - в наличии\n"
        "❌ - нет в наличии\n\n"
        "<i>Нажмите на товар для связи с продавцом</i>"
    )
    
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode='HTML')

# ========== РАСХОДНИКИ (ВСЕ В НАЛИЧИИ) ==========
@dp.callback_query(lambda c: c.data == "consumables")
async def consumables_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Картридж хрос 0,4 - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Картридж хрос 0,6 - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Картридж аегис нано - 350 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Испаритель пасито 50-65в - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Испаритель буст серии - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Испаритель манто - 300 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД В КАТАЛОГ", callback_data="catalog")]
    ])
    
    text = (
        "⚙️ <b>РАСХОДНИКИ</b>\n\n"
        "✅ ВСЕ ТОВАРЫ В НАЛИЧИИ!\n\n"
        "<i>Нажмите на товар для связи с продавцом</i>"
    )
    
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode='HTML')

# ========== ОДНОРАЗКИ ==========
@dp.callback_query(lambda c: c.data == "disposables")
async def disposables_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Подонки малазиан 12000тяг - 1600 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Рик и Морти зомби 23000тяг - 2000 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text=f"{get_status_emoji(True)} Рик и Морти на замерзоне кислые 20000тяг - 1800 руб", url=f"https://t.me/{OWNER[1:]}")],
        [InlineKeyboardButton(text="⬅️ НАЗАД В КАТАЛОГ", callback_data="catalog")]
    ])
    
    text = (
        "🚬 <b>ОДНОРАЗКИ</b>\n\n"
        "✅ Все товары в наличии\n\n"
        "<i>Нажмите на товар для связи с продавцом</i>"
    )
    
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode='HTML')

# ========== КОНТАКТЫ ==========
@dp.callback_query(lambda c: c.data == "contacts")
async def contacts_handler(call: types.CallbackQuery):
    text = (
        f"📞 <b>КОНТАКТЫ</b>\n\n"
        f"👤 <b>Продавец:</b> {OWNER}\n"
        f"📱 <b>Для заказа:</b> нажмите на товар в каталоге\n\n"
        f"🚚 <b>Доставка:</b> по договоренности\n\n"
        f"💬 <i>По всем вопросам пишите в личные сообщения</i>"
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="back_main")]
    ])
    
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode='HTML')

# ========== ПОМОЩЬ ==========
@dp.callback_query(lambda c: c.data == "help")
async def help_handler(call: types.CallbackQuery):
    text = (
        "❓ <b>ПОМОЩЬ</b>\n\n"
        "1️⃣ <b>Выберите категорию</b> в каталоге\n"
        "2️⃣ <b>Нажмите на нужный товар</b>\n"
        "3️⃣ <b>Вы перейдете к продавцу</b> в личные сообщения\n"
        "4️⃣ <b>Уточните наличие и оформите заказ</b>\n\n"
        "✅ <b>Статусы товаров:</b>\n"
        "• ✅ - есть в наличии\n"
        "• ❌ - нет в наличии\n\n"
        "💡 <i>Если кнопка не работает, напишите продавцу напрямую</i>"
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="back_main")]
    ])
    
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode='HTML')

# ========== НАЗАД В ГЛАВНОЕ ==========
@dp.callback_query(lambda c: c.data == "back_main")
async def back_main_handler(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 КАТАЛОГ ТОВАРОВ", callback_data="catalog")],
        [InlineKeyboardButton(text="📞 КОНТАКТЫ", callback_data="contacts"),
         InlineKeyboardButton(text="❓ ПОМОЩЬ", callback_data="help")]
    ])
    
    text = (
        "👋 <b>Главное меню</b>\n\n"
        "Выберите действие:"
    )
    
    await call.message.edit_text(text, reply_markup=keyboard, parse_mode='HTML')

# ========== ЗАПУСК БОТА ==========
if __name__ == "__main__":
    logging.info("🚀 Бот запущен!")
    executor.start_polling(dp, skip_updates=True)
