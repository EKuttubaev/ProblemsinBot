from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from datetime import datetime
from database.user import Product, Sale

product_data = {}
sale_data = {}


def add_product_name(update, context):
    user_id = update.effective_user.id
    product_data[user_id] = {}
    update.message.reply_text("Введите название товара")
    return 1


def save_name(update, context):
    product_name = update.message.text
    user_id = update.effective_user.id
    product_data[user_id]["name"] = product_name

    main_buttons = [
        ["Кг", "Литры", "Штук"]
    ]
    buttons = ReplyKeyboardMarkup(main_buttons)
    update.message.reply_text("Укажите единицу измерения", reply_markup=buttons)
    return 2


def save_unit(update, context):
    product_unit = update.message.text
    user_id = update.effective_user.id
    product_data[user_id]["unit"] = product_unit

    update.message.reply_text("Введите количество")
    return 3


def save_count(update, context):
    product_count = update.message.text
    user_id = update.effective_user.id
    product_data[user_id]["count"] = product_count

    update.message.reply_text("Введите цену")
    return 4


def save_price(update, context):
    product_price = update.message.text
    user_id = update.effective_user.id
    product_data[user_id]["price"] = product_price

    Product.create(name=product_data[user_id]["name"],
                   unit=product_data[user_id]["unit"],
                   count=product_data[user_id]["count"],
                   price=product_data[user_id]["price"])

    del product_data[user_id]

    update.message.reply_text("Товар добавлен")
    return 1


def clean(clean, context):
    pass


#def add_category(update, context):
    #update.message.reply_text("Введите категорию")


#def delete_category(update, context):
    #update.message.reply_text("Введите категорию для удаления")


#Функция добавления товара в базу.

#def add_product(update, context):
    #update.message.reply_text("")
def add_sale_product(update, context):
    user_id = update.effective_user.id
    sale_data[user_id] = {}
    update.message.reply_text("Введите наименование товара:")
    return 1


def save_sale_name(update, context):
    sale_name = update.message.text
    user_id = update.effective_user.id
    sale_data[user_id]["name"] = sale_name

    update.message.reply_text("Введите кол-во")
    return 2


def save_sale_count(update, context):
    sale_count = int(update.message.text)
    user_id = update.effective_user.id
    product_name = sale_data[user_id]["name"]
    product = Product.select().where(Product.name == product_name).get()
    Sale.create(product=product, count=sale_count, unit=product.unit, price=product.price,
                date_and_time=datetime.now(), total=sale_count * product.price)
    update.message.reply_text("Товар продан")
    return ConversationHandler.END

