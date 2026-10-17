import os

def open_settings(page):
    pages = {
        "wifi": "ms-settings:network-wifi",
        "bluetooth": "ms-settings:bluetooth",
        "display": "ms-settings:display",
        "sound": "ms-settings:sound"
    }

    if page in pages:
        os.startfile(pages[page])
        return True

    return False