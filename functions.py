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


def product_amount(update, context):
    update.message.reply_text("Введите количество")
    return 3


def add_expense(update, context):
    update.message.reply_text("Введите сумму продажи")
    update.message.reply_text("Товар добавлен")
    return ConversationHandler.END




def clean(clean, context):
    pass


def add_category(update, context):
    update.message.reply_text("Введите категорию")


def delete_category(update, context):
    update.message.reply_text("Введите категорию для удаления")


#Функция добавления товара в базу.

def add_product(update, context):
    update.message.reply_text("Введите наименование товара:")
    return 1


def add_product_price(update, context):
    update.message.reply_text("Введите цену")
    return 2


def add_product_unit(update, context):
    update.message.reply_text("Введите ед.измерения")
    return 3


def add_product_count(update, context):
    update.message.reply_text("Введите кол-во")

    return 4


def add_product_end(update, context):
    update.message.reply_text("Товар добавлен")
    return ConversationHandler.END()


