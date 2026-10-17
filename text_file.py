import os


def create_text_file(filename, content):
    if not filename.endswith(".txt"):
        filename += ".txt"

    path = os.path.join(
        os.path.expanduser("~/Downloads"),
        filename
    )

    with open(path, "w") as file:
        file.write(content)

    return path