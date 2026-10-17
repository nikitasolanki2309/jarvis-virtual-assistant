import pyperclip


def get_clipboard():
    return pyperclip.paste()

def copy_to_clipboard(text):
    pyperclip.copy(text)