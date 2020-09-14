from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import config
import functions
from database.user import *


print("Бот запущен!")


def on_start(update, context):
    current_id = update.effective_user.id
    if User.select().where(User.tel_id == current_id).count() > 0:
        main_buttons = [
            ["Продажа", "Категории"],
            ["Отчеты", "История"],
            ["Добавить товар"]
        ]
        buttons = ReplyKeyboardMarkup(main_buttons)
        chat = update.effective_chat
        context.bot.send_message(chat_id=chat.id, text="Привет! Я бот помощник.\n Выберите команду.",
                                 reply_markup=buttons)
    else:
        chat = update.effective_chat
        context.bot.send_message(chat_id=chat.id, text="Вам необходимо зарегистрироваться:\n "
                                                       "Для регистрации напишите /reg")


updater = Updater(config.token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", on_start))

product_function_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex("Добавить товар"), functions.add_product_name)],
    states={
        1: [MessageHandler(Filters.text, functions.save_name)],
        2: [MessageHandler(Filters.text, functions.save_unit)],
        3: [MessageHandler(Filters.text, functions.save_count)],
        4: [MessageHandler(Filters.text, functions.save_price)],
    },
    fallbacks=[]
)


function_add_product = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex("Продажа"), functions.add_sale_product)],
    states={
        1: [MessageHandler(Filters.text, functions.save_sale_name)],
        2: [MessageHandler(Filters.text, functions.save_sale_count)],
    },

    fallbacks=[CommandHandler("clean", functions.clean)]
)

conversation_handler = ConversationHandler(
    entry_points=[(CommandHandler("reg", functions.on_reg))],
    states={
        1: [MessageHandler(Filters.text, functions.reg_user)]
    },
    fallbacks=[CommandHandler("clean", functions.clean)]
)

dispatcher.add_handler(conversation_handler)
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(function_add_product)
dispatcher.add_handler(product_function_handler)
prep_database()
updater.start_polling()
updater.idle()
