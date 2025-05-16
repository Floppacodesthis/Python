import pyautogui
import win32api, win32con
import time
import keyboard

# GUARANTEED TO WORK ON https://www.agame.com/game/magic-piano-tiles

class Bot:
    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def detect(self):
        time.sleep(10)
        while not keyboard.is_pressed('q'):
            if pyautogui.pixel(754, 1001)[0] == 0:
                self.click(754, 1001)
            if pyautogui.pixel(920, 1001)[0] == 0:
                self.click(920, 1001)
            if pyautogui.pixel(1104, 1001)[0] == 0:
                self.click(1104, 1001)
            if pyautogui.pixel(1250, 1001)[0] == 0:
                self.click(1250, 1001)


bot = Bot()

if __name__ == "__main__":
    bot.detect()


#tile 1; X:  754 Y:  1001
#tile 2; X:  920 Y:  1001
#tile 3; X: 1104 Y:  1001
#tile 4; X: 1250 Y:  1001 