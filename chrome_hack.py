import string
import os
import time

from settings import DEBUG, CHROME_DRIVER_PATH, CHROME_SAVE_FOLDER, CHROME_DATABASE_FOLDER

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# for copy in win buffer
import pyperclip

import keyboard

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeHack:
    def __init__(self):
        self.options = Options()
        self.options.add_argument(f"user-data-dir={CHROME_DATABASE_FOLDER}")
        #self.options.headless=True
        #user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        #self.options.add_argument(f'user-agent={user_agent}')

    def start(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=self.options)

    def connect(self, url):
        try:
            self.driver.get(url)
            if DEBUG:
                print('Connected')
        except Exception as e:
            print('Connection Error:', e)

    def quit(self):
        self.driver.quit()

    def expand_shadow_element(self, element):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def save_chrome_pass(self):
        try:
            # click 1
            element = self.driver.find_element("tag name", "settings-ui")
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'main')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('css selector', 'settings-basic-page')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('css selector', 'settings-autofill-page')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'passwordSection')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'exportImportMenuButton')
            sh = self.expand_shadow_element(element)

            b = sh.find_element('id', 'maskedImage')
            b.click()

            # click 2
            element = self.driver.find_element("tag name", "settings-ui")
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'main')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('css selector', 'settings-basic-page')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('css selector', 'settings-autofill-page')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'passwordSection')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'exportImportMenu')
            b = element.find_element('id', 'menuExportPassword')
            b.click()

            # click 3
            element = self.driver.find_element("tag name", "settings-ui")
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'main')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('css selector', 'settings-basic-page')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('css selector', 'settings-autofill-page')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'passwordSection')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('css selector', 'passwords-export-dialog')
            sh = self.expand_shadow_element(element)

            element = sh.find_element('id', 'dialog_start')

            b = element.find_element('id', 'exportPasswordsButton')
            b.click()
            # code after this comment hack dialog window. Also it hack your mind and all that have meaning
            WebDriverWait(self.driver, 3).until_not(EC.number_of_windows_to_be(1))
            pyperclip.copy(CHROME_SAVE_FOLDER + '\\Chrome_pass.csv')
            keyboard.press_and_release('ctrl+v')

            keyboard.press_and_release('enter')
            time.sleep(3)

            # print(self.driver.window_handles)
            # pyperclip.copy(CHROME_SAVE_FOLDER + '\\Chrome_passwords.csv')
            # window_before = self.driver.window_handles[0]
            # window_after = self.driver.window_handles[5]
            # for i in self.driver.window_handles:
            #     self.driver.switch_to.window(i)

        except Exception as e:
            print(f'Element Error. {e}')

    def save_chrome_pass_2(self):
        try:
            pyperclip.copy(CHROME_SAVE_FOLDER + '\\Chrome_passwords.csv')
            keyboard.press_and_release('tab')
            keyboard.press_and_release('tab')
            keyboard.press_and_release('tab')
            keyboard.press_and_release('tab')
            keyboard.press_and_release('tab')
            keyboard.press_and_release('tab')
            keyboard.press_and_release('tab')
            time.sleep(0.1)
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('ctrl+v')
            keyboard.press_and_release('enter')
        except Exception as e:
            print('Error', e)