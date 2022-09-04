from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
import os
import psutil


def spegni(update: Update, context: CallbackContext):
    update.message.reply_text("Boss, ho appena spento il suo PC")
    os.system("shutdown /s /t 1")


def riavvia(update: Update, context: CallbackContext):
    update.message.reply_text("Boss, ho appena riavviato il suo PC")
    os.system("shutdown /r /t 1")


def chiudi(update: Update, context: CallbackContext):
    update.message.reply_text("Boss, ho appena chiuso l'app")


def cmd(update: Update, context: CallbackContext):
    if context.args:
        if context.args[0]:
            update.message.reply_text("Boss, ho appena eseguito il comando")

            cmd = ""
            for i in context.args:
                cmd = cmd + " " + i

            a = os.popen(cmd).read()

            if context.args[0] == "cd":
                os.chdir(context.args[1])

            if a == "":
                update.message.reply_text("Fatto!")
            else:
                update.message.reply_text(a)
        else:
            update.message.reply_text("Boss, mi scusi, deve inserire un comando")
    else:
        update.message.reply_text("Boss, mi scusi, dopo il comando deve inserire qualcosa da scrivere nella shell")




def kill(update: Update, context: CallbackContext):
    if context.args:

        if context.args[0]:
            update.message.reply_text("Boss, ho appena eseguito il comando")

            process_to_kill = context.args[0]

            my_pid = os.getpid()

            for p in psutil.process_iter():
                if p.name() == process_to_kill:
                    if not p.pid == my_pid:
                        p.terminate()
        else:
            update.message.reply_text("Boss, mi scusi, deve inserire un nome valido")
    else:
        update.message.reply_text("Boss, mi scusi, dopo il comando deve inserire il nome dell'app da chiudere")