import pyautogui
from time import sleep
from params import params


def water():
    count = 0
    while True:
        if count == params['times_to_water']:
            restart_app()
        sleep(1)

        # walk
        pyautogui.moveTo(params['buttons']['walk']['x'], params['buttons']['walk']['y'], 2)
        pyautogui.click()
        pyautogui.PAUSE = 7

        # water/get fruit
        pyautogui.move(params['buttons']['fruit']['x'], params['buttons']['fruit']['y'], 2)
        pyautogui.click()
        pyautogui.PAUSE = 2
        count += 1


def restart_app():
    # close SweetDays
    pyautogui.moveTo(params['buttons']['close_app']['x'], params['buttons']['close_app']['y'], 2)
    pyautogui.click()
    sleep(1)

    # open SweetDays
    pyautogui.moveTo(params['buttons']['open_app']['x'], params['buttons']['open_app']['y'], 2)
    pyautogui.click()
    sleep(60)

    # Tap to start
    pyautogui.moveTo(params['buttons']['tap_to_start']['x'], params['buttons']['tap_to_start']['y'], 2)
    pyautogui.click()
    sleep(10)

    # Go out
    pyautogui.moveTo(params['buttons']['go_out']['x'], params['buttons']['go_out']['y'], 2)
    pyautogui.click()

    # start watering sequence
    water()


if __name__ == '__main__':
    restart_app()

