# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:09:26 2026

@author: joshu
"""
#pip install pyautogui
#please note that websites may have latency

import pyautogui
import time

##""" use this to determine coordinates pf device, uncomment and run

# print("Hover your mouse over the target color on the website. Press Ctrl+C to stop.")
# try:
#     while True:
#         x, y = pyautogui.position()
#         print(f"X: {x}, Y: {y} | Color: {pyautogui.pixel(x, y)}")
#         time.sleep(1)
# except KeyboardInterrupt:
#     pass

##"""



# ==== Configurable Parameters ====

pyautogui.PAUSE = 0          # Disable the default 0.1s pause


#target_x, target_y = 981, 906   #5
#target_x, target_y = 1227, 578   #2
#target_x, target_y = 929, 390   #0
target_x, target_y = 1125, 491   #1
#target_x, target_y = stuff, stuff          # <--- CHANGE THIS to the X,Y coordinates on your screen
target_color = (59, 60, 61)            # The RGB of the dark grey image you provided
tolerance = 5                          # Small tolerance, as solid dark colors are usually very consistent
check_interval = 0.01                   # Check every 0.01 seconds

print(f"Looking for color {target_color} at ({target_x}, {target_y})... Press Ctrl+C to stop.")

try:
    while True:
        # Get the RGB color at the specified coordinate on your screen
        current_color = pyautogui.pixel(target_x, target_y)
        
        # Check if the current color matches the target color (within tolerance)
        if all(abs(c - t) <= tolerance for c, t in zip(current_color, target_color)):
            print(f"Detected! Color was {current_color}. Pressing spacebar...")
            pyautogui.press('space')
            time.sleep(1)  # Wait half a second to prevent spamming spacebar
        time.sleep(check_interval)
except KeyboardInterrupt:
    print("\nStopped.")