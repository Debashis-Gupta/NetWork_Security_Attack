"""

Here i added mouse Listener just to show how you can keep track mouse position
Author : Debashis Gupta

"""

from pynput.mouse import Listener

def realTime_mouse_tracker(x,y):
    print("Position X axis {} and Y axis {}".format(x,y))
with Listener(on_move=realTime_mouse_tracker) as l:
    l.join()
