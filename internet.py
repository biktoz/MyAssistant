#Telegram Modules
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler

import webbrowser

def browser(update: Update, context: CallbackContext):
    update.message.reply_text("Boss, I've opened your browser")
    webbrowser.open_new_tab("https://google.com")

#PASSING ARGUMENTS = @context.args
def url(update: Update, context: CallbackContext):
    if context.args:
        #update.message.reply_text(context.args)
        if "www" in context.args[0]:
            update.message.reply_text("Boss, I've searched what you want")
            webbrowser.open(context.args[0])
        else:
            update.message.reply_text("Boss, I'm sorry, you have to write a valid link")
    else:
        update.message.reply_text("Boss, I'm sorry, after the command you have to write a valid link")




def search(update: Update, context: CallbackContext):
    if context.args:
        #update.message.reply_text(context.args)
        if context.args[0]:
            update.message.reply_text("Boss, I've completed the research")

            cosaCercare = ""
            for i in context.args:
                cosaCercare = cosaCercare + " " + i

            webbrowser.open("https://www.google.it/search?q=" + cosaCercare)

        else:
            message.reply_text("Boss, I'm sorry, you have to write what you want to search")
