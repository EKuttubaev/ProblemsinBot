from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup


def add_product_name(update, context):
    update.message.reply_text("Введите название товара")
    pass


def product_unit(update, context):
    update.message.reply_text("Укажите единицу измерения")
    main_buttons = [
        ["Кг", "Литры" "Штук"]
    ]
    buttons = ReplyKeyboardMarkup(main_buttons)
    pass

def add_expense(update, context):
    update.message.reply_text("Enter sum of expense")
    pass


