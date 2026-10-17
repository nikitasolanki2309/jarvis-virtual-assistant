import os


def search_file(filename):
    search_folders = [
        r"C:\Users\HP\OneDrive\Documents",
        os.path.expanduser("~/Downloads"),
        r"C:\Users\HP\OneDrive\Desktop"
    ]

    for folder in search_folders:
        for root, directories, files in os.walk(folder):
            for file in files:
                if filename.lower() in file.lower():
                    return os.path.join(root, file)

    return None