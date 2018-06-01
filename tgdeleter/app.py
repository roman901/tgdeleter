import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from .config import Config

config_obj = Config()


def start(config_file):
    config_obj.apply(config_file)

    updater = Updater(token=config_obj['TOKEN'])
    dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.text, message_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()


def message_handler(bot, update):
    if update.message.from_user.id in config_obj['BAD_USERS']:
        chance = random.randint(0, 100)
        print(update.message.from_user.username, chance, chance < config_obj['CHANCE'])
        if chance < config_obj['CHANCE']:
            bot.delete_message(chat_id=update.message.chat.id, message_id=update.message.message_id)
