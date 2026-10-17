import threading
import time


def set_alarm(seconds, speak_function):
    alarm_thread = threading.Thread(
        target=wait_for_alarm,
        args=(seconds, speak_function)
    )

    alarm_thread.start()


def wait_for_alarm(seconds, speak_function):
    time.sleep(seconds)

    speak_function("Alarm! Wake up!")