import pyautogui
import time
print("Initializing QuickClicker... \n")
print("QuickClicker is a open-source and totally free autoclicker program. Copyright 2022")
time.sleep(5)
timeint = float(input("Seconds between clicks "))
clickno = int(input("Clicks per time "))
count = 0
print("QuickClicker started...")
while True:
    while count <= clickno:
        pyautogui.click()
        count += 1
    time.sleep(timeint)
    count = 0