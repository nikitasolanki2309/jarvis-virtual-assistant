import os

def restart_computer():
    os.system("shutdown /r /t 0")

def shutdown_computer():
    os.system("shutdown /s /t 0")

def sleep_computer():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")