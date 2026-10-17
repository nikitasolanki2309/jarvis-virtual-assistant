import platform
import psutil


def get_system_info():
    system = platform.system()
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent(interval=1)

    return system, ram, cpu

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent