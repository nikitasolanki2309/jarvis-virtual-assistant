import json
import os
import threading
import time
from datetime import datetime, timedelta

FILE_NAME = "reminders.json"


def add_reminder(text):
    reminders = get_reminders()
    reminders.append(text)

    with open(FILE_NAME, "w") as file:
        json.dump(reminders, file)

    return True


def get_reminders():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []

def clear_reminders():
    with open(FILE_NAME, "w") as file:
        json.dump([], file)

    return True

def timed_reminder(text, seconds, speak_function):
        reminder_time = datetime.now() + timedelta(seconds=seconds)

        reminder = {
            "text": text,
            "time": reminder_time.isoformat()
        }

        reminders = get_timed_reminders()
        reminders.append(reminder)

        with open("timed_reminders.json", "w") as file:
            json.dump(reminders, file)

        reminder_thread = threading.Thread(
            target=wait_and_speak,
            args=(text, seconds, speak_function)
        )

        reminder_thread.start()


def wait_and_speak(text, seconds, speak_function):
    time.sleep(seconds)
    speak_function(f"Reminder: {text}")

    reminders = get_timed_reminders()

    reminders = [
        reminder for reminder in reminders
        if reminder["text"] != text
    ]

    with open("timed_reminders.json", "w") as file:
        json.dump(reminders, file)

def get_timed_reminders():
    if not os.path.exists("timed_reminders.json"):
        return []

    try:
        with open("timed_reminders.json", "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []

def load_timed_reminders(speak_function):
    reminders = get_timed_reminders()
    remaining_reminders = []

    for reminder in reminders:
        try:
            reminder_time = datetime.fromisoformat(reminder["time"])
        except (ValueError, KeyError):
            continue
        
        seconds = (reminder_time - datetime.now()).total_seconds()

        if seconds > 0:
            remaining_reminders.append(reminder)

            timed_reminder(
                reminder["text"],
                seconds,
                speak_function
            )

        else:
            speak_function(f"Reminder: {reminder['text']}")

    with open("timed_reminders.json", "w") as file:
        json.dump(remaining_reminders, file)