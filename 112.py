import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

API_TOKEN = "7959603468:AAFXYwQhOLGNFXCKTaa5v-wskupio8A-Jbk"

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Рассчитать", "Информация", "Купить"]
    keyboard.add(*buttons)
    return keyboard

def create_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_calories = types.InlineKeyboardButton(text='Рассчитать калории', callback_data='calories')
    button_formulas = types.InlineKeyboardButton(text='Формулы', callback_data='formulas')
    keyboard.add(button_calories, button_formulas)
    return keyboard

def create_product_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_product1 = types.InlineKeyboardButton(text='Product1', callback_data='product1')
    button_product2 = types.InlineKeyboardButton(text='Product2', callback_data='product2')
    button_product3 = types.InlineKeyboardButton(text='Product3', callback_data='product3')
    button_product4 = types.InlineKeyboardButton(text='Product4', callback_data='product4')

    keyboard.add(button_product1, button_product2, button_product3, button_product4)
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = create_keyboard()
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=create_inline_keyboard())

@dp.message_handler(lambda message: message.text.lower() == 'информация')
async def send_info(message: types.Message):
    await message.answer("Я ваш калькулятор калорий! Я помогу вам рассчитать вашу норму калорий для поддержания здоровья и достижения ваших целей.")

@dp.message_handler(lambda message: message.text.lower() == 'купить')
async def get_buying_list(message: types.Message):
    products_info = [
        ("Product1", "описание 1", 100),
        ("Product2", "описание 2", 200),
        ("Product3", "описание 3", 300),
        ("Product4", "описание 4", 400),
    ]

    for product_name, description, price in products_info:
        await message.answer(f'Название: {product_name} | Описание: {description} | Цена: {price}₽')

    await message.answer("Выберите продукт для покупки:", reply_markup=create_product_keyboard())

@dp.callback_query_handler(lambda call: call.data.startswith('product'))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = call.data
    await call.message.answer(f"Вы успешно приобрели {product_id}!")
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        "Формула Миффлина-Сан Жеора:"
        "Для мужчин:"
        "BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5."
        "Для женщин:"
        "BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) - 161."
        "Эти формулы помогают рассчитать базальный уровень метаболизма (BMR), "
        "который показывает количество калорий, необходимых вашему организму для "
        "поддержания жизнедеятельности в состоянии покоя. Используйте эти данные для "
        "оптимизации своего питания и тренировок."
    )
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
