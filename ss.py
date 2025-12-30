import pyautogui
import time

time.sleep(3)
pyautogui.moveTo(693, 348, duration=0.2)
pyautogui.click(button='left')
time.sleep(0.3)
pyautogui.moveTo(798, 399, duration=0.2)
pyautogui.click(button='left')
time.sleep(0.3)

#press agree to select box
pyautogui.moveTo(661, 418, duration=0.5)
pyautogui.click(button='left')
time.sleep(0.5)

#click on next button to proceed
pyautogui.moveTo(1203, 475, duration=0.5)
pyautogui.click(button='left')
print("Proceeded with application.")

#wait for email verification page to load
time.sleep(20)

#switch to email tab
pyautogui.hotkey('ctrl', '4')
time.sleep(0.5)
time.sleep(5)

#click on latest email
pyautogui.moveTo(404, 498, duration=0.3)
pyautogui.click(button='left')
time.sleep(3)

#select verification numbers
pyautogui.moveTo(1131, 490, duration=0.3)
pyautogui.doubleClick(button='left')
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
print("Copied verification code from email.")
time.sleep(0.5)

#switch back to job application tab
pyautogui.hotkey('ctrl', '2')
time.sleep(1)

#paste verification code
pyautogui.moveTo(816, 345, duration=0.3)
pyautogui.click(button='left')
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'v')

print("Pasted verification code into application.")
time.sleep(0.5)

#press verify button
pyautogui.moveTo(947, 421, duration=0.3)
pyautogui.click(button='left')
print("Submitted verification code.")
time.sleep(25)

#press remove previous resume button
pyautogui.moveTo(951, 817, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)

#press upload new resume button
pyautogui.moveTo(946, 794, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(2)

#click on filter by date dropdown (twice to ensure menu opens)
pyautogui.moveTo(506, 124, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(1)

#double click latest file (should be at top)
pyautogui.moveTo(343, 192, duration=0.3)
time.sleep(0.2)
pyautogui.doubleClick(button='left')
time.sleep(2)

#go to bottom of page
pyautogui.hotkey('end')
time.sleep(1)

#click submit button
pyautogui.moveTo(1231, 891, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')

#brings up back to missing fields

#click disability category dropdown
pyautogui.moveTo(660, 565, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.typewrite('no', interval=0.05)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('enter')
time.sleep(0.5)

#click  go to next issue
pyautogui.moveTo(1654, 606, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)

#click ethnicity dropdown
pyautogui.moveTo(643, 561, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.typewrite('I b', interval=0.05)
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('enter')

#click  go to next issue
pyautogui.moveTo(1654, 606, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)

#click gender dropdown
pyautogui.moveTo(651, 559, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.typewrite('ma', interval=0.05)
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('enter')

#click  go to next issue
pyautogui.moveTo(1654, 606, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)

#click indigenous dropdown
pyautogui.moveTo(646, 565, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.typewrite('no', interval=0.05)
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('enter')

#click  go to next issue
pyautogui.moveTo(1654, 606, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)

#click suports LGBTQ+ dropdown
pyautogui.moveTo(662, 564, duration=0.3)
time.sleep(0.2)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('enter')
