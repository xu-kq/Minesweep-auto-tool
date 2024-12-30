import subprocess
import pygetwindow as gw
import pyautogui as pag
import time
import cv2
import numpy as np
import pyautogui

from utils import find_match_points


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

    img_entire = cv2.imread("./imgs/entire.png")
    img_gray = cv2.imread("./imgs/gray.png")
    match_points = find_match_points(img_entire, img_gray)

    background = pag.screenshot(region=(window.left, window.top, window.width, window.height))
    background.save("./imgs/background.png")
    background = np.array(background)
    res = cv2.matchTemplate(image=background,
                            templ=img_entire,
                            method=cv2.TM_CCOEFF_NORMED,
                            )

    res = res.transpose()
    loc = np.unravel_index(np.argmax(res), res.shape)

    l = loc[0] + window.left
    t = window.top + loc[1]
    r = l + img_entire.shape[1]
    b = t + img_entire.shape[0]

    sz = img_gray.shape[0]
    gap = (img_entire.shape[0] - img_gray.shape[0] * 9) // 8

    x, y = match_points[0]
    pag.click(window.left + l + x, window.top + t + y)

    res = cv2.matchTemplate(image=img_gray,
                            templ=img_entire,
                            method=cv2.TM_CCOEFF_NORMED,
                            ).transpose()

    loc = np.where(res >= 0.8)
    while loc[0].size > 0:
        x = loc[0][0] + l + sz // 2
        y = loc[1][0] + t + sz // 2
        pag.click(x, y)
        pag.sleep(0.1)
        img_entire = np.array(pag.screenshot(region=(int(l), int(t), int(r - l), int(b - t))))
        res = cv2.matchTemplate(image=img_gray,
                                templ=img_entire,
                                method=cv2.TM_CCOEFF_NORMED,
                                ).transpose()

        loc = np.where(res >= 0.8)

    print("Done")
    Game_Process.terminate()

