import pyautogui
import os
import time


ET_path = r'C:\Program Files (x86)\Caterpillar\Electronic Technician\Etech.exe'
Active_codes = r'act_code.png'
Active_events = r'Active_event.png'
connect = r'connect.png'
ok = r'ok.png'
check = r'check_box.png'
ECM_select = r'HVAC_ECM.png'
log = r'log_code.png'


def open_application(app_path):
    os.startfile(app_path)
    print("app_opened")


def click_on_button(image_path):
    position = pyautogui.locateCenterOnScreen(image_path)
    for i in range(0, 5):
        if position is None:
            position = pyautogui.locateCenterOnScreen(image_path)
    print(position)
    pyautogui.moveTo(position)
    for i in range(0, 2):
        pyautogui.click()
        print("button_clicked")
    return position


def take_screenshot(position):
    img = pyautogui.screenshot(region=(0, 0, 800, 600))


open_application(ET_path)
time.sleep(10)

connect_position = click_on_button(connect)
time.sleep(100)

select_position = click_on_button(ECM_select)
time.sleep(5)

ok_position = click_on_button(ok)
time.sleep(10)

code_position = click_on_button(Active_codes)
time.sleep(5)
