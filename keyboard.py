from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = InlineKeyboardMarkup(row_width=2)
kb.add(
    InlineKeyboardButton(text='Анекдот', callback_data='anekdot'),
    InlineKeyboardButton(text='День чего?', callback_data='day')
)

