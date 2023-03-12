import pyautogui
from time import sleep


def water():
    count = 0
    while True:
        if count == 10:
            restart_app()
        sleep(1)

        # walk
        pyautogui.moveTo(1070, 1340, 2)
        pyautogui.click()
        pyautogui.PAUSE = 7

        # water/get fruit
        pyautogui.move(300, -300, 2)
        pyautogui.click()
        pyautogui.PAUSE = 2
        count += 1


def restart_app():
    # close SweetDays
    pyautogui.moveTo(476, 18, 2)
    pyautogui.click()
    sleep(1)

    # open SweetDays
    pyautogui.moveTo(1542, 457, 2)
    pyautogui.click()
    sleep(60)

    # Tap to start
    pyautogui.moveTo(1263, 750, 2)
    pyautogui.click()
    sleep(10)

    # Go out
    pyautogui.moveTo(949, 1328, 2)
    pyautogui.click()

    # start watering sequence
    water()


if __name__ == '__main__':
    restart_app()

