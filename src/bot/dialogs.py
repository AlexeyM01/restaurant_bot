"""
src/bot/dialogs.py
"""
from datetime import datetime, timedelta
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram_calendar import SimpleCalendarCallback, SimpleCalendar, get_user_locale
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from dateutil.relativedelta import relativedelta
from sqlalchemy import select

from src.database.database import get_db
from src.database.models import Booking


class BookingForm(StatesGroup):
    name = State()
    date = State()
    time = State()
    guests = State()


time_buttons = [
    [KeyboardButton(text="09:00"), KeyboardButton(text="10:00"), KeyboardButton(text="11:00")],
    [KeyboardButton(text="12:00"), KeyboardButton(text="13:00"), KeyboardButton(text="14:00")],
    [KeyboardButton(text="15:00"), KeyboardButton(text="16:00"), KeyboardButton(text="17:00")],
    [KeyboardButton(text="18:00"), KeyboardButton(text="19:00"), KeyboardButton(text="20:00")]
]
time_keyboard = ReplyKeyboardMarkup(
    keyboard=time_buttons,
    resize_keyboard=True
)


async def cmd_get(message: Message):
    telegram_user_id = message.from_user.id
    async for db in get_db():
        booking_query = select(Booking).where(Booking.telegram_user_id == telegram_user_id)
        result = await db.execute(booking_query)
        bookings = result.scalars().all()
        if bookings:
            booking_messages = "\n".join(
                [f"Бронирование: на имя: {booking.name}, дата: {booking.date}, "
                 f"гостей = {booking.guests}" for booking in bookings])
            await message.reply(booking_messages)
        else:
            await message.reply("У вас нет активных бронирований.")


async def cmd_start(message: Message, state: FSMContext):
    await message.reply("Привет! Пожалуйста, введи свое имя:")
    await state.set_state(BookingForm.name.state)


async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    calendar = SimpleCalendar(
        locale=await get_user_locale(message.from_user), show_alerts=True
    )
    calendar.set_dates_range(datetime.today()-timedelta(days=1), datetime.today()+relativedelta(months=3))

    await message.reply(
        "Отлично! Теперь выбери дату:",
        reply_markup=await calendar.start_calendar(year=datetime.now().year, month=datetime.now().month)
    )
    await state.set_state(BookingForm.date.state)


async def process_date(callback_query: CallbackQuery, callback_data: SimpleCalendarCallback, state: FSMContext):
    calendar = SimpleCalendar(
        locale=await get_user_locale(callback_query.from_user), show_alerts=True
    )
    calendar.set_dates_range(datetime.today()-timedelta(days=1), datetime.today()+relativedelta(months=3))
    selected, date = await calendar.process_selection(callback_query, callback_data)
    if selected:
        selected_date = f"{callback_data.day:02}.{callback_data.month:02}.{callback_data.year:4}"
        await callback_query.message.reply(
            f"Вы выбрали дату: {selected_date}. Пожалуйста, выбери время:", reply_markup=time_keyboard)
        await state.update_data(date=string_to_datetime(selected_date, "%d.%m.%Y"))
        await state.set_state(BookingForm.time.state)


async def process_time(message: Message, state: FSMContext):
    time = message.text
    data = await state.get_data()

    strdatetime = str(data["date"].strftime("%d.%m.%Y")) + " " + time
    datetime = string_to_datetime(strdatetime, "%d.%m.%Y %H:%M")
    await state.update_data(date=datetime)

    await message.reply("Отлично! Пожалуйста, введи количество гостей:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(BookingForm.guests.state)


async def process_guests(message: Message, state: FSMContext):
    guests_count = int(message.text)
    await state.update_data(guests=guests_count)
    data = await state.get_data()
    name, date = data['name'], data['date']
    telegram_user_id = message.from_user.id

    await message.reply(
        f"Спасибо! Вы забронировали на имя {name} на {date}, {date.strftime('%A')} на {guests_count} человек")
    await state.clear()

    await db_add_booking(data['name'], data['date'], guests_count, telegram_user_id)


def string_to_datetime(date_string, date_format):
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError as e:
        print(f"Ошибка преобразования: {e}")
        return None


async def db_add_booking(name: str, date: datetime, guests: int, telegram_user_id: int):
    new_booking = Booking(name=name, date=date, guests=guests, telegram_user_id = telegram_user_id)
    async for db in get_db():
        db.add(new_booking)
        await db.commit()
        await db.refresh(new_booking)


