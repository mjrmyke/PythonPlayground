import pyautogui

width, height = pyautogui.size()
pyautogui.FAILSAFE = True

while True:
    try:
        pyautogui.click(width/2, height/2,25)

    except pyautogui.FailSafeException:
        raise
