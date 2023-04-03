import string
import os


def get_fleshdisk(CODE_DIR):
    disk_list = []
    for c in string.ascii_uppercase:
        disk = c + f':\\{CODE_DIR}'
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list[-1].split('\\')[0]
