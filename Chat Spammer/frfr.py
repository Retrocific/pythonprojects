import keyboard
import os
import time
print("Press t to start and g to stop.")
def break_function():
    if keyboard.is_pressed("g"):
        return True
    elif keyboard.is_pressed("t"):
        return False

t_g = input()
if t_g == "t":
    for i in range(69420):
        time.sleep(2)
        keyboard.write("sup bun")
        keyboard.press("Enter")
        if break_function():
            break


















































#MADE BY RETROCIFIC ON GITHUB (nice line)
