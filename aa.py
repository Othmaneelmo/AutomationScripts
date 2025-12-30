import pyautogui
import time

# Step 4: Switch to second tab (description)
time.sleep(3)
pyautogui.hotkey('ctrl', '2')
time.sleep(0.5)
#changed from 5 to 1.5
time.sleep(3)

# Step 5: Scroll and select description text
pyautogui.hotkey('ctrl', 'end')
time.sleep(0.3)
pyautogui.press('pageup')
time.sleep(0.3)
pyautogui.moveTo(1435, 464, duration=0.5)
time.sleep(0.3)
pyautogui.mouseDown()
pyautogui.moveTo(1435, 91, duration=0.5)
#changed from 3 to 1
time.sleep(1)
pyautogui.moveTo(1435, 306, duration=0.3)
time.sleep(0.3)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl', 'c')
print("Copied from browser.")
time.sleep(0.3)
pyautogui.click(button='left')
time.sleep(0.3)
