import pyperclip
import pyautogui

#  PyAutoGUI中文输入需要用粘贴实现
#  Python 2版本的pyperclip提供中文复制
def paste(foo):
    pyperclip.copy(foo)
    pyautogui.hotkey('ctrl', 'v')

foo = u'学而时习之'
#  移动到文本框
# pyautogui.click(130,30)
paste(foo)