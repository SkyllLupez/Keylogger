from pynput.mouse import Controller
from pynput.keyboard import Controller

# left to right is 10, top to bottom 20 (top left is 0,0)

def controlMouse():
    mouse = Controller()
    mouse.position = (1000,1000)

#controlMouse()      

#It will write the words where the cursor is last left    

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hello again")
    
controlKeyboard()    



