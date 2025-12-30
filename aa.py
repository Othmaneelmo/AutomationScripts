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


# Step 6: Open the prompt text file in default editor 
file_path = r"C:\Users\XXX\gptprompt.txt"  #file path
pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.typewrite(f'notepad "{file_path}"\n', interval=0.01)
time.sleep(1.5)  # wait for Notepad to open

# Step 7: Jump to marker line --- XXX DESCRIPTION ---
pyautogui.hotkey('ctrl', 'f')
time.sleep(0.3)
pyautogui.typewrite('--- XXX DESCRIPTION ---', interval=0.05)
time.sleep(0.3)
pyautogui.press('Enter')
time.sleep(1)
pyautogui.press(['tab', 'tab', 'tab', 'tab',])  # close find dialog
pyautogui.press('Enter')
time.sleep(0.3)

# Step 8: Move cursor to end of marker line
pyautogui.press('end')
pyautogui.press('enter')  # move to new line

# Step 9: Paste copied description
pyautogui.hotkey('ctrl', 'v')
print("Pasted below --- XXX DESCRIPTION ---")
time.sleep(0.2)

#copy entire file content
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
#exit file
pyautogui.hotkey('ctrl', 'w')
time.sleep(0.2)
#select do not modify
pyautogui.press('tab')
time.sleep(0.2)
pyautogui.press('Enter')
time.sleep(0.2)
#switch to last tab 
pyautogui.hotkey('ctrl', '9')


#press new chat button
time.sleep(1)
pyautogui.moveTo(90, 172, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)

#press chat field
time.sleep(0.5)
pyautogui.moveTo(757, 513, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.2)

#paste full content
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

#submit
pyautogui.press('enter')

print("Submitted to XXX.")

#wait for response
time.sleep(35)

# Step 10: Select and copy XXX response
pyautogui.click(button='left')
time.sleep(0.2)
pyautogui.press('down', presses=5, interval=0.1)
time.sleep(0.2)
pyautogui.moveTo(1453, 774, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
pyautogui.click(button='left')
time.sleep(1)


# Step 4: Switch to third tab (XXX XXX)
time.sleep(1)
pyautogui.hotkey('ctrl', '3')
time.sleep(1.5)

#refresh page
pyautogui.hotkey('ctrl', 'r')
#changed from 5 to 1.5
time.sleep(3)

#replace existing content (XXX XXX)
pyautogui.moveTo(292, 362, duration=0.3)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'v')
print("Pasted into XXX")

#click recompile button
time.sleep(0.5)
pyautogui.moveTo(1046, 146, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')

#wait for compile
time.sleep(5)

#click download PDF button
pyautogui.moveTo(1167, 145, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
print("Downloaded updated XXX")
time.sleep(0.2)


