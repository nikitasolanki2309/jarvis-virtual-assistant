import ctypes


def lock_computer():
    ctypes.windll.user32.LockWorkStation()