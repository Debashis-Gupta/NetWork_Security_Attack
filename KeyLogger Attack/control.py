"""

Here i added keyboard controller just to show how you can play with pynput
Here this will print the Author : Debashis Gupta line where your cursor last pointed
Author : Debashis Gupta

"""


#controling the keyboard
from pynput.keyboard import Controller

def control_keyboard():
    keyboard = Controller()
    keyboard.type("Author : Debashis Gupta")
control_keyboard()
