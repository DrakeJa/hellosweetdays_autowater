import pyautogui
from time import sleep
from params import PARAMS
from helpers import restart_app

BUTTONS = PARAMS['buttons']


def party():
    count = 0
    while True:
        if count == PARAMS['times_to_water']:
            restart_app()
            party()
        sleep(1)

        # invite
        pyautogui.moveTo(BUTTONS['invite']['x'], BUTTONS['invite']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['invitation']['x'], BUTTONS['invitation']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['get_ready']['x'], BUTTONS['get_ready']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['fruit_1']['x'], BUTTONS['fruit_1']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['fruit_2']['x'], BUTTONS['fruit_2']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['fruit_3']['x'], BUTTONS['fruit_3']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['fruit_4']['x'], BUTTONS['fruit_4']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['fruit_5']['x'], BUTTONS['fruit_5']['y'], 2)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['fruit_6']['x'], BUTTONS['fruit_6']['y'], 3)
        pyautogui.click()

        pyautogui.moveTo(BUTTONS['ok']['x'], BUTTONS['ok']['y'], 4)
        pyautogui.click()
        sleep(2)
        pyautogui.click()

        sleep(45)

        count += 1


if __name__ == '__main__':
    restart_app()

    # start partying sequence
    party()
