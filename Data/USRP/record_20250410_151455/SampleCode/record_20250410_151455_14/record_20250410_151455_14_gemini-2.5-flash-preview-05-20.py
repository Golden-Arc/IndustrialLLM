import pyautogui
import time

time.sleep(1)
pyautogui.click(100, 100)
time.sleep(0.5)
pyautogui.write("Hello")
time.sleep(0.7)
pyautogui.press("enter")
time.sleep(0.8)
pyautogui.scroll(10)
time.sleep(0.8)
pyautogui.moveTo(200, 200)
time.sleep(0.7)
pyautogui.dragTo(300, 300, duration=0.5)
time.sleep(1.0)
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)
pyautogui.click(400, 400)
time.sleep(0.8)
pyautogui.write("World")
time.sleep(0.7)
pyautogui.press("space")
time.sleep(0.5)
pyautogui.hotkey("alt", "tab")