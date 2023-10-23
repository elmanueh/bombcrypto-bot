# LIBRERIAS NECESARIAS

import telebot  # Importamos las librería
import pyautogui
from datetime import datetime, date, time, timedelta
import yaml

# CARGAR CONFIGURACION
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# BOT TELEGRAM

bot = telebot.TeleBot(config["telegram_bot"])
chat_id = config["telegram_id"]

#bot.send_message(chat_id, "🔰 Comenzando a ejecutar el codigo\n👷 Colocando los Bheroes a trabajar\n🥷 Evitando ser expulsado por inactividad 🥷\n🛌 Colocando los Bheroes a dormir\n❌ Error detectado, refrescando el juego ❌")



'''while True:
    if pyautogui.locateOnScreen("image/game/error.png",confidence=.8) or pyautogui.locateOnScreen("image/game/ok.png",confidence=.8):
        print("hola")
    else:
        print("adios")'''


#bot.send_photo(chat_id, pyautogui.screenshot())

def hola(working):
   if(not working):
       print("hola")


working = True

hola(working)

