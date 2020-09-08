import config
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

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


updater = Updater(config.token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))

updater.start_polling()
updater.idle()
