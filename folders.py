import os


folders = {
    "downloads": os.path.expanduser("~/Downloads"),
    "documents": os.path.expanduser("~/Documents"),
    "desktop": r"C:\Users\HP\OneDrive\Desktop",
    "pictures": os.path.expanduser("~/Pictures"),
    "screenshots": os.path.join(os.getcwd(), "screenshots"),
    "videos": os.path.expanduser("~/Videos"),
    "music": os.path.expanduser("~/Music")
}


def open_folder(name):
    if name in folders:
        os.startfile(folders[name])
        return True

    return False