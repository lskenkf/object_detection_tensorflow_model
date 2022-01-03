import pyautogui
import time

pyautogui.keyDown('alt')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.click(button='left')
time.sleep(1)
pyautogui.keyUp('alt')



screenshot = pyautogui.screenshot()
screenshot.save("screen.png")