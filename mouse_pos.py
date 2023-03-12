import pyautogui
from time import sleep

# Use this script to find coordinates of buttons


def main():
    while True:
        print(pyautogui.position())
        sleep(1)


if __name__ == '__main__':
    main()