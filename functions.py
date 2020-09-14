from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from user import *
from datetime import datetime, time, timedelta
from datetime import datetime
from datetime import datetime
from database.user import Product, User
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


def on_reg(update, context):
    update.message.reply_text("Введите Ваше имя")
    return 1


def reg_user(update, context):
    try:
        new_name = update.message.text
        User.create(name=new_name, created_at=datetime.now(), tel_id=update.effective_user.id)
        update.message.reply_text("Вы успешно зарегистрированы! нажмите команду:  /start")
        return ConversationHandler.END

    except:
        update.message.reply_text("Введите имя заново:")
        return 1


def on_reg(update, context):
    update.message.reply_text("Введите Ваше имя")
    return 1


def reg_user(update, context):
    try:
        new_name = update.message.text
        User.create(name=new_name, created_at=datetime.now(), tel_id=update.effective_user.id)
        update.message.reply_text("Вы успешно зарегистрированы! нажмите команду:  /start")
        return ConversationHandler.END

    except:
        update.message.reply_text("Введите имя заново:")
        return 1


def on_reports(update, context):
    report_buttons = [
        ["За сегодня", "За определенную дату"],
        ["За период/выберите период"], ["Главное меню"],

    ]
    buttons = ReplyKeyboardMarkup(report_buttons)
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Выберите отчеты по датам .",
                             reply_markup=buttons)


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




def main_menu(update, context):
    pass


def show_daily_report(update, context):
    update.message.reply_text("Общая сумма продаж: ")
    today = datetime.today()
    day_start = datetime.combine(today, time(0, 0, 0))
    day_end = day_start + timedelta(1)
    total_sum = Product.select(fn.Sum(Product.total).alias("sale_sum")).where(
        (Product.date_and_time > day_start) & (Product.date_and_time < day_end)).execute()

    for x in total_sum:
        if x.sale_sum == None:
            update.message.reply_text("Данных за сегодня нет")
        else:
            update.message.reply_text(f"Общая сумма продаж: {x.sale_sum}")
    good_info = Product.select(Product).where(
        (Product.date_and_time > day_start) & (Product.date_and_time < day_end)).execute()
    for sale in good_info:
        update.message.reply_text(f"{sale.name},количество: {sale.count},на сумму: {sale.total}")


def on_day(update, context):
    update.message.reply_text("Выберите дату в формате YYYY/MM/ DD")
    return 1


def one_day_date(update, context):
    try:
        input_datetime = update.message.text
        date1 = datetime.strptime(input_datetime, "%Y/%m/%d")
        day_start = datetime.combine(date1, time(0, 0, 0))
        day_end = day_start + timedelta(1)
        total_sum = Product.select(fn.Sum(Product.total).alias("sale_sum")).where(
            (Product.date_and_time > day_start) & (Product.date_and_time < day_end)).execute()

        for x in total_sum:
            if x.sale_sum == None:
                update.message.reply_text("Данных за запрощенную дату нет")
            else:
                update.message.reply_text(f"Общая сумма продаж {x.sale_sum}")
        good_info = Product.select(Product).where(
            (Product.date_and_time > day_start) & (Product.date_and_time < day_end)).execute()
        for sale in good_info:
            update.message.reply_text(f"{sale.name},количество: {sale.count},на сумму: {sale.total}")
        return ConversationHandler.END
    except:
        update.message.reply_text("Не правильно введена дата, введите в формате YYYY/MM/DD")
        return


data = {
    "f_date": "",
    "s_date": "",
}


def delta_date(update, context):
    update.message.reply_text("Выберите первую дату в формате YYYY/MM/ DD")
    return 1


def first_date(update, context):
    data["f_date"] = update.message.text
    update.message.reply_text("Выберите вторую дату в формате YYYY/MM/ DD")
    return 2


def second_date(update, context):
    try:
        data["s_date"] = update.message.text
        date1 = datetime.strptime(data["f_date"], "%Y/%m/%d")
        date2 = datetime.strptime(data["s_date"], "%Y/%m/%d")
        day_start = datetime.combine(date1, time(0, 0, 0))
        day_end = datetime.combine(date2, time(23, 59, 59))
        total_sum = Product.select(fn.Sum(Product.total).alias("sale_sum")).where(
            (Product.date_and_time > day_start) & (Product.date_and_time < day_end)).execute()

        for x in total_sum:
            if x.sale_sum == None:
                update.message.reply_text("Данных за запрощенную дату нет или неправильно введена дата")
            else:
                update.message.reply_text(f"Общая сумма продаж {x.sale_sum}")
        good_info = Product.select(Product).where(
            (Product.date_and_time > day_start) & (Product.date_and_time < day_end)).execute()
        for sale in good_info:
            update.message.reply_text(f"{sale.name},количество: {sale.count},на сумму: {sale.total}")
    except:
        update.message.reply_text("Неправильно введена дата, введите период заново")
        return ConversationHandler.END

    return ConversationHandler.END
