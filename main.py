import subprocess
import pygetwindow as gw
import pyautogui as pag
import time
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    Tiny_Game_Path = r'D:\\WindowsApps\\30397Cole.S.Minesweep_5.0.0.0_x64__e2hnr0kcjxe4m\\Minesweep.exe'
    Game_Process = subprocess.Popen(Tiny_Game_Path)

    pag.sleep(1)

    windows = gw.getWindowsWithTitle('Minesweep')
    if windows:
        window = windows[0]
        width = window.width
        height = window.height
        left = window.left
        right = window.right
        top = window.top
        bottom = window.bottom
    else:
        print("Window not found")
        exit()

    cur = Point(0, 0)
    cur.x = left + window.width // 2
    cur.y = bottom - window.height // 2

    sz = 39
    gap = 5
    # left top corner = (453, 742)
    # pag.click(453, 742)

    # pag.click(491, 742 - sz + 1)




    # Game_Process.terminate()

