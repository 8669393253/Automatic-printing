import pyperclip
import time
import pyautogui
import keyboard

def write_copied_text():
    print("Copy text to the clipboard. Press 'Shift' to start typing, 'Ctrl' to stop, and 'Alt' to exit.")
    
    typing = False
    text = ""

    while True:
        # Check if Alt is pressed to exit
        if keyboard.is_pressed('alt'):
            print("Exiting the program.")
            break

        # Start typing when Shift is pressed
        if keyboard.is_pressed('shift') and not typing:
            text = pyperclip.paste()
            if not text:
                print("No text found in clipboard. Exiting.")
                break
            print("Typing started. Switch to your desired application...")
            time.sleep(2)
            typing = True

        # Handle typing and stopping
        if typing:
            for char in text:
                if keyboard.is_pressed('ctrl'):
                    print("Typing stopped. Press 'Shift' to continue...")
                    typing = False
                    break
                pyautogui.typewrite(char)
                time.sleep(0.0009)  # Reduced delay for faster typing

    print("Finished.")

if __name__ == "__main__":
    write_copied_text()
