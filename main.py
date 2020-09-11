import pyautogui
import os
import subprocess
import sys


def open_application():
    os.startfile(r'C:\Program Files (x86)\Caterpillar\Electronic Technician\Etech.exe')


def click_on_button(image_path):
    connect_position = pyautogui.locateCenterOnScreen('start.png')
    pyautogui.moveTo(connect_position)
    pyautogui.click()