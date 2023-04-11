import pyautogui
from time import sleep
from params import PARAMS
from helpers import restart_app

BUTTONS = PARAMS['buttons']


def water():
    count = 0
    while True:
        if count == PARAMS['times_to_water']:
            restart_app()
            water()
        sleep(1)

        # walk
        pyautogui.moveTo(BUTTONS['walk']['x'], BUTTONS['walk']['y'], 2)
        pyautogui.click()
        pyautogui.PAUSE = 7

        # water/get fruit
        pyautogui.move(BUTTONS['fruit']['x'], BUTTONS['fruit']['y'], 2)
        pyautogui.click()
        pyautogui.PAUSE = 2
        count += 1


if __name__ == '__main__':
    restart_app()

    # start watering sequence
    water()
