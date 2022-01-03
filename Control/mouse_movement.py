# alt-tab

import pyautogui,time

pyautogui.keyDown('alt')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)


pyautogui.press('enter')
time.sleep(1)
pyautogui.keyUp('alt')

pyautogui.click(button='left')

pyautogui.keyDown('w')
time.sleep(5)
pyautogui.keyUp('w')