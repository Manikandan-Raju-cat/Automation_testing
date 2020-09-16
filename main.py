import pyautogui
import os
import time


ET_path = r'C:\Program Files (x86)\Caterpillar\Electronic Technician\Etech.exe'  # type:  str
Active_codes = r'act_code.png'                                                # type: str
Active_events = r'Active_event.png'                                              # type: str
connect = r'connect.png'                                                                    # type: str
ok = r'ok.png'
check = r'check_box.png'
ECM_select = r'HVAC_ECM.png'
delay = 5


def open_application(app_path):
    os.startfile(app_path)
    print("app_opened")
    #time.sleep(2*delay)
    #pyautogui.hotkey('winleft')


def click_on_button(image_path):
    position = pyautogui.locateCenterOnScreen(image_path)
    print(position)
    pyautogui.moveTo(position)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

    return position


def take_screenshot(position):
    img = pyautogui.screenshot(region=(0, 0, 300, 400))


'''
if __name__ == "__main__":
'''
open_application(ET_path)
time.sleep(2.5*delay)
connect_position = click_on_button(connect)
print("connect_clicked")
time.sleep(8*delay)
connect_position = click_on_button(ECM_select)
print("ECM_Selected")
time.sleep(1*delay)
connect_position = click_on_button(ok)
print("ok_clicked")
time.sleep(2*delay)
code_pos = click_on_button(Active_codes)
print("code_clicked")
time.sleep(2*delay)
code_pos = click_on_button(check)
print(type(code_pos))
print("check_clicked")
time.sleep(5*delay)

