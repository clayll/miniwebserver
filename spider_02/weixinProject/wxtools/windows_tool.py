#coding:utf-8
import win32con
import win32gui
import win32api
import time
import os

def solvedexplore(filepath,dialogName=u'打开'):
    # 有个bug打开后过快就没反应，停2秒先
    time.sleep(3)
    print("开始等打开窗口")

    while not win32gui.FindWindow(None, dialogName):time.sleep(1)  # 等到窗口出现
    dialog = win32gui.FindWindow(None, dialogName)

    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    button = win32gui.FindWindowEx(dialog, 0, None, u"打开(O)")


    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, os.path.abspath(filepath))
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

def waring():
    win32api.MessageBox(0, u"数据库内数据不够", u"错误提示", win32con.MB_OK)
