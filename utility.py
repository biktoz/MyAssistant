from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
import os
import psutil


def shutdown(update: Update, context: CallbackContext):
    update.message.reply_text("Boss, I've turned off your PC")
    os.system("shutdown /s /t 1")


def restart(update: Update, context: CallbackContext):
    update.message.reply_text("Boss, I've restarted your PC")
    os.system("shutdown /r /t 1")



def cmd(update: Update, context: CallbackContext):
    if context.args:
        if context.args[0]:
            update.message.reply_text("Boss, I've executed the command")

            cmd = ""
            for i in context.args:
                cmd = cmd + " " + i

            a = os.popen(cmd).read()

            if context.args[0] == "cd":
                os.chdir(context.args[1])

            if a == "":
                update.message.reply_text("Yeah!")
            else:
                update.message.reply_text(a)
        else:
            update.message.reply_text("Boss, I'm sorry, syntax error")
    else:
        update.message.reply_text("Boss, I'm sorry, you have to write something to execute in the shell")




def kill(update: Update, context: CallbackContext):
    if context.args:

        if context.args[0]:
            update.message.reply_text("Boss, I've killed the app")


            process_to_kill = context.args[0]

            my_pid = os.getpid()

            for p in psutil.process_iter():
                if p.name() == process_to_kill:
                    if not p.pid == my_pid:
                        p.terminate()
        else:
            update.message.reply_text("Boss, I'm sorry, you have to write a valid name")
    else:
        update.message.reply_text("Boss, I'm sorry, after the command you need to write a valid app name")
