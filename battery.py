import psutil

def get_battery():
    battery = psutil.sensors_battery()

    if battery is None:
        return None

    percentage = battery.percent
    charging = battery.power_plugged

    return percentage, charging


def is_battery_low():
    battery = get_battery()

    if battery is None:
        return None

    percentage, charging = battery

    if percentage <= 20 and not charging:
        return True

    return False