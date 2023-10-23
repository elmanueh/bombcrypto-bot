# L I B R E R I A S    N E C E S A R I A S 

from datetime import datetime, date, time, timedelta
import pyautogui
import time
import telebot
import yaml



# C A R G A R    C O N F I G U R A C I O N

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)



# B O T    T E L E G R A M

bot = telebot.TeleBot(config["telegram_bot"])
chat_id = config["telegram_id"]



# F U N C I O N E S    D E L    C O D I G O       


def Trabajar_Personajes(next):

    print("[+] Colocando los Bheroes a trabajar")
    bot.send_message(chat_id, "👷 Colocando los Bheroes a trabajar\nPróxima acción: " + next)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/atras.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/heroes.png",confidence=0.8), clicks=2, interval=0.25)
    
    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/trabajar.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/atrasx.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/minar.png",confidence=0.8), clicks=2, interval=0.25)


def Siendo_Activo(working):
    
    print("Evitando ser expulsado por inactividad")
    bot.send_message(chat_id, "🥷 Evitando ser expulsado por inactividad")

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/atras.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/minar.png",confidence=0.8), clicks=2, interval=0.25)

    if(not working):
        time.sleep(config["time_actions"])
        pyautogui.hotkey("win","d")



def Descansar_Personajes(next):

    print("[+] Colocando los Bheroes a dormir")
    bot.send_message(chat_id, "🛌 Colocando los Bheroes a dormir\nPróxima acción: " + next)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/atras.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/heroes.png",confidence=0.8), clicks=2, interval=0.25)
    
    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/dormir.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/atrasx.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/minar.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(config["time_actions"])
    pyautogui.hotkey("win","d")


def Errores():
    
    print("[-] Error detectado, refrescando el juego")
    bot.send_message(chat_id, "❌ Error detectado, refrescando el juego")

    bot.send_photo(chat_id, pyautogui.screenshot())

    time.sleep(config["time_actions"])
    pyautogui.hotkey("ctrl","r")

    time.sleep(10)
    pyautogui.click(pyautogui.locateCenterOnScreen("image/metamask/conectar.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(10)
    pyautogui.click(pyautogui.locateCenterOnScreen("image/metamask/firmar.png",confidence=0.8), clicks=2, interval=0.25)

    time.sleep(20)
    pyautogui.click(pyautogui.locateCenterOnScreen("image/game/minar.png",confidence=0.8), clicks=2, interval=0.25)
    



# C O M I E N Z A    E L    C O D I G O  


time_activated = 5      #minutos  
nerrores = 0
working = True
last_time_working = datetime.today() - timedelta(minutes=300)
last_time_activated = datetime.today()


print("\n\n### Comenzando a ejecutar el codigo ###")
bot.send_message(chat_id, "🔰 Comenzando a ejecutar el codigo")
time.sleep(10)


while nerrores<7:

    if pyautogui.locateOnScreen("image/game/error.png") or pyautogui.locateOnScreen("image/game/ok.png") or pyautogui.locateOnScreen("image/metamask/conectar.png"):
        nerrores+=1
        Errores()

    if (datetime.today()-last_time_working >= timedelta(minutes=(config["time_working"]+config["time_sleeping"]))):
        pyautogui.hotkey("win","1")
        time.sleep(config["time_actions"])

        if pyautogui.locateOnScreen("image/game/atras.png"):
            working = True
            time_activated = 5
            last_time_working = datetime.today()
            last_time_activated = datetime.today()
            next=(datetime.now()+timedelta(minutes=config["time_working"])).strftime('%H:%M')
            Trabajar_Personajes(next)
        else:
            nerrores+=1
            Errores()


    if ((datetime.today()-last_time_working >= timedelta(minutes=config["time_working"])) and working):
        if pyautogui.locateOnScreen("image/game/atras.png"):
            working = False
            time_activated = 14
            last_time_activated = datetime.today()
            next=(datetime.now()+timedelta(minutes=config["time_sleeping"])).strftime('%H:%M')
            Descansar_Personajes(next)
        else:
            nerrores+=1
            Errores()


    if (datetime.today()-last_time_activated >= timedelta(minutes=time_activated)):
        if(not working):
            pyautogui.hotkey("win","1")
            time.sleep(config["time_actions"])

        if pyautogui.locateOnScreen("image/game/atras.png"):
            last_time_activated = datetime.today()
            Siendo_Activo(working)
        else:
            nerrores+=1
            Errores()

    time.sleep(10)


time.sleep(config["time_sleeping"])
print("[X] Error Máximo, REINICIAME!!!")
bot.send_message(chat_id, "❌ Error Máximo, REINICIAME!!! ❌")
pyautogui.hotkey("win","d")