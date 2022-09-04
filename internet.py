#Telegram Modules
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler

import webbrowser

def chrome(update: Update, context: CallbackContext):
    update.message.reply_text("Boss, ho appena aperto Chrome sul suo PC")
    webbrowser.open_new_tab("https://google.com")

#Per passare gli argomenti uso @context.args
def url(update: Update, context: CallbackContext):
    if context.args:
        #update.message.reply_text(context.args)
        if "www" in context.args[0]:
            update.message.reply_text("Boss, ho appena eseguito la ricerca")
            webbrowser.open(context.args[0])
        else:
            update.message.reply_text("Boss, mi scusi, deve inserire un link valido")
    else:
        update.message.reply_text("Boss, mi scusi, dopo il comando deve inserire un link valido")




def cerca(update: Update, context: CallbackContext):
    if context.args:
        #update.message.reply_text(context.args)
        if context.args[0]:
            update.message.reply_text("Boss, ho appena eseguito la ricerca")

            cosaCercare = ""
            for i in context.args:
                cosaCercare = cosaCercare + " " + i

            webbrowser.open("https://www.google.it/search?q=" + cosaCercare)

        else:
            update.message.reply_text("Boss, mi scusi, deve inserire cosa vuole cercare")
    else:
        update.message.reply_text("Boss, mi scusi, dopo il comando deve inserire cosa vuole cercare")