import ctypes


def empty_recycle_bin():
    result = ctypes.windll.shell32.SHEmptyRecycleBinW(
        None,
        None,
        0
    )

    return result == 0