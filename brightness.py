import screen_brightness_control as sbc


def get_brightness():
    return sbc.get_brightness()[0]


def increase_brightness():
    current = get_brightness()
    new = min(current + 10, 100)
    sbc.set_brightness(new)


def decrease_brightness():
    current = get_brightness()
    new = max(current - 10, 0)
    sbc.set_brightness(new)

def set_brightness(level):
    level = max(0, min(level, 100))
    sbc.set_brightness(level)

def get_current_brightness():
    return get_brightness()