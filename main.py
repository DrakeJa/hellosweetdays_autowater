import pyautogui
from time import sleep
from params import PARAMS

BUTTONS = PARAMS['buttons']

def water():
    count = 0
    while True:
        if count == PARAMS['times_to_water']:
            restart_app()
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


def restart_app():
    # close SweetDays
    pyautogui.moveTo(BUTTONS['close_app']['x'], BUTTONS['close_app']['y'], 2)
    pyautogui.click()
    sleep(1)

    # open SweetDays
    pyautogui.moveTo(BUTTONS['open_app']['x'], BUTTONS['open_app']['y'], 2)
    pyautogui.click()
    sleep(60)

    # Tap to start
    pyautogui.moveTo(BUTTONS['tap_to_start']['x'], BUTTONS['tap_to_start']['y'], 2)
    pyautogui.click()
    sleep(10)

    # Go out
    pyautogui.moveTo(BUTTONS['go_out']['x'], BUTTONS['go_out']['y'], 2)
    pyautogui.click()

    # start watering sequence
    water()


if __name__ == '__main__':
    restart_app()

