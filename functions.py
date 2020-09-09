from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup


def add_product_name(update, context):
    update.message.reply_text("Введите название товара")
    return 1


def product_unit(update, context):
    main_buttons = [
        ["Кг", "Литры", "Штук"]
    ]
    buttons = ReplyKeyboardMarkup(main_buttons)
    update.message.reply_text("Укажите единицу измерения", reply_markup=buttons)
    return 2


def add_expense(update, context):
    update.message.reply_text("Введите сумму продажи")

    update.message.reply_text("Товар добавлен")

    return ConversationHandler.END()


def clean(clean, context):
    pass