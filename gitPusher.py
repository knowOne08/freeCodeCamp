from pynput.keyboard import Key, Controller
import os
import time
keyboard =  Controller()
fldrIni = input("Enter the folder Initial: ")
cmtNo = str(input("Enter no of  commit: "))
# tab = keyboard.press(Key.tab)


for char in "git add "  + fldrIni:
    keyboard.press(char)
    keyboard.release(char)

keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

for char in f'git commit -m "Todays freeCodeCamp commit {cmtNo}"':
    keyboard.press(char)
    keyboard.release(char)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

for char in 'git push':
    keyboard.press(char)
    keyboard.release(char)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

# os.system('git commit -m \"Todays freeCodeCamp Commit\"')


# os.system("git push")
