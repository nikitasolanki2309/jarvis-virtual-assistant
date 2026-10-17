import subprocess


def open_app(name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "file explorer": "explorer.exe",
        "vs code": r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd",
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "task manager": "taskmgr.exe",
        "command prompt": "cmd.exe"
    }

    if name in apps:
        subprocess.Popen(apps[name])
        return True

    return False