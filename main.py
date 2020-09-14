import pyautogui
import os
import time


# import subprocess
# import sys


ET_path = r'C:\Program Files (x86)\Caterpillar\Electronic Technician\Etech.exe'  # type:  str
Active_codes = r'Active_code.png'                                                # type: str
Active_events = r'Active_event.png'                                              # type: str
connect = r''                                                                    # type: str
ok = r''

def open_application(app_path):
    os.startfile(app_path)
    pyautogui.hotkey('winleft')


def click_on_button(image_path):
    position = pyautogui.locateCenterOnScreen(image_path)
    pyautogui.moveTo(position)
    pyautogui.click()
    return position


def take_screenshot(position):
    img = pyautogui.screenshot(region=(0, 0, 300, 400))


if __name__ == "__main__":
    open_application(ET_path)
    time.sleep(5)
    connect_position = click_on_button(connect)
    time.sleep(10)
    ok_position = click_on_button(ok)
    time.sleep(10)

