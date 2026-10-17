import pyautogui
from datetime import datetime
import os

def take_screenshot():
    folder = "screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = "screenshot_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

    path = os.path.join(folder, filename)

    image = pyautogui.screenshot()
    image.save(path)

    return path