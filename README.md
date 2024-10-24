# Clipboard Typing Automation
This Python script allows you to automatically type text copied to the clipboard into any application of your choice. It listens for specific keyboard events to start, stop, and exit the typing process.

## Features

**Clipboard Access**: Automatically retrieves text from the clipboard.
**Keyboard Control**: Start typing with Shift, stop with Ctrl, and exit with Alt.
**Fast Typing**: Simulates typing with configurable delays for faster input.

## Requirements

Make sure you have Python installed on your machine. You'll also need the following Python packages:
- pyperclip
- pyautogui
- keyboard

You can install the required packages using pip:
pip install pyperclip pyautogui keyboard

## Usage

1. **Copy Text**: Copy any text to your clipboard that you want to type out.
2. **Run the Script**: Execute the script in your terminal or command prompt.
   python clipboard_typing.py

3. **Keyboard Controls**:
   - Press **Shift**: Starts typing the copied text. You have 2 seconds to switch to the desired application.
   - Press **Ctrl**: Stops the typing process.
   - Press **Alt**: Exits the script.

## Example

1. Copy the text you want to type.
2. Run the script.
3. Press **Shift** to start typing in your chosen application.
4. Press **Ctrl** to pause typing, and **Shift** to resume.
5. Press **Alt** to exit the program.

## Notes

- Make sure the application you want to type into is in focus when you start the typing process.
- Use caution when using automation scripts as they can interfere with other applications.

## License

This project is licensed under the MIT License. Feel free to modify and use it as per your needs.
