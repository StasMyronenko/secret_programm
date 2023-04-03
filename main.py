from server import bot, win
import os
from settings import PROGRAM_FOLDER, CHROME_DRIVER_PATH_FROM, CHROME_DRIVER_PATH, DEBUG, PROGRAM_NAME
import time

if str(os.getcwd()) + f'\\{PROGRAM_NAME}' != PROGRAM_FOLDER:
    try:
        win.copy(os.getcwd() + f'\\{PROGRAM_NAME}', PROGRAM_FOLDER)
        win.add_autoload()

    except Exception as e:
        if DEBUG:
            print(e)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        if DEBUG:
            print(e)
    time.sleep(60)
