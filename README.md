# simple-screenshotter
Lightweight script for creating multiple screenshots that can be bound to a single key.

Created to replace the default Windows screenshot function, which only sends a screenshot to the clipboard. This script sends a fullscreen screenshot the desktop or another customizable path. Running the script multiple times doesn't overwrite existing screenshots in that path.

Instructions: 

1. Ensure the pyautogui package is installed.
2. Ensure download path is set correctly in screenshotter.pyw: download_path = os.path.abspath(r'C:\Users\YOURUSERNAMEHERE\Desktop')
3. Hook the script to your keyboard. On Windows, this can be done with a tool like AutoHotkey.
4. If you're using AutoHotkey, check the provided ahk file and ensure it includes the correct paths to your python installation and the location of the screenshotter script.
