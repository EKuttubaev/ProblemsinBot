from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import configuration
import functions

updater = Updater(configuration.TOKEN, use_context=True)
dispatcher = updater.dispatcher
print("Бот запущен!")


def on_start(update, context):
    main_buttons = [
        ["Продажа", "Категории"],
        ["Отчеты", "История"],
        ["Добавить товар"]
    ]
    buttons = ReplyKeyboardMarkup(main_buttons)
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет! Я бот помощник.\n Выберите команду.",
                             reply_markup=buttons)


product_function_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex("Продажа"), functions.add_product_name)],
    states={
        1: [MessageHandler(Filters.text, functions.product_unit)],
        2: [MessageHandler(Filters.text, functions.product_amount)],
        3: [MessageHandler(Filters.text, functions.add_expense)],
    },

    fallbacks=[CommandHandler("clean", functions.clean)]
)


function_add_product = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex("Добавить товар"), functions.add_product)],
    states={
        1: [MessageHandler(Filters.text, functions.add_product_price)],
        2: [MessageHandler(Filters.text, functions.add_product_unit)],
        3: [MessageHandler(Filters.text, functions.add_product_count)],
        4: [MessageHandler(Filters.text, functions.add_product_end)]
    },

    fallbacks=[CommandHandler("clean", functions.clean)]
)

category_function_handler = ConversationHandler()

dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(function_add_product)
dispatcher.add_handler(product_function_handler)
updater.start_polling()
updater.idle()
