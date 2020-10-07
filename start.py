import pyautogui

actual_img = None
last_img = None

def get_screen():
    actual_img = pyautogui.screenshot('screens/screenshot.png')

def compare_screens(actual_img):
    return last_img == actual_img
        

get_screen()