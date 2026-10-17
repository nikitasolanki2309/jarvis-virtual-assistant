import speech_recognition as sr
import musicLibrary
import time
import os
import datetime
from news import get_news
from ai import aiProcess
from speech import speak
from websites import open_website, search_google, open_url
from calculator import calculate
from weather import get_weather
from reminder import add_reminder, get_reminders, clear_reminders, timed_reminder, load_timed_reminders
from apps import open_app
from screenshot import take_screenshot
from volume import volume_up, volume_down, mute, unmute, get_volume
from alarm import set_alarm
from folders import open_folder
from battery import get_battery, is_battery_low
from system_info import get_system_info, get_cpu_usage, get_ram_usage
from file_search import search_file
from text_file import create_text_file
from system_control import lock_computer
from recycle_bin import empty_recycle_bin
from clipboard import get_clipboard, copy_to_clipboard
from maps import search_maps
from settings import open_settings
from power import restart_computer, shutdown_computer, sleep_computer
from brightness import increase_brightness, decrease_brightness, set_brightness, get_current_brightness
from wifi import get_wifi_status
from internet import check_internet


recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


def processCommand(c):
    if "exit" in c.lower() or "quit" in c.lower() or "stop" in c.lower():
        speak("Goodbye.")
        exit()
    elif "open google" in c.lower():
        if open_website("google"):
            speak("Opening Google.")

    elif "open youtube" in c.lower():
        if open_website("youtube"):
            speak("Opening YouTube.")

    elif "open facebook" in c.lower():
        if open_website("facebook"):
            speak("Opening Facebook.")

    elif "open linkedin" in c.lower():
        if open_website("linkedin"):
            speak("Opening LinkedIn.")

    elif "open github" in c.lower():
        if open_website("github"):
            speak("Opening GitHub.")

    elif "open amazon" in c.lower():
        if open_website("amazon"):
            speak("Opening Amazon.")

    elif "open spotify" in c.lower():
        if open_website("spotify"):
            speak("Opening Spotify.")

    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split()[1:])

        if musicLibrary.play_song(song):
            speak(f"Playing {song}.")
        else:
            speak("Sorry, I couldn't find that song in your music library.")

    elif "news" in c.lower():
        articles = get_news()

        if articles:
            speak("Here are the top five headlines.")

            for article in articles:
                title = article.get("title")

                if title:
                    speak(title)

        else:
            speak("Sorry, I couldn't get the news right now.")

    elif "time" in c.lower():
        speak(f"The time is {time.strftime('%I:%M %p')}.")

    elif "date" in c.lower():
        today = datetime.datetime.now()
        speak(f"Today's date is {today.strftime('%d %B %Y')}")

    elif "calculate" in c.lower():
        expression = c.lower().replace("calculate", "").strip()

        parts = expression.split()

        if len(parts) == 3:
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            result = calculate(a, operator, b)
            speak(f"The answer is {result}")

        else:
            speak("Please say the calculation like: calculate 25 plus 15.")

    elif "weather" in c.lower():
        weather = get_weather("Jhajjar")

        if weather:
            temperature, wind_speed = weather
            speak(f"The temperature is {temperature} degrees Celsius. Wind speed is {wind_speed} kilometers per hour.")

        else:
            speak("Sorry, I couldn't get the weather right now.")

    elif "search maps" in c.lower():
        query = c.lower().replace("search maps", "").strip()

        if query:
            search_maps(query)
            speak("Opening Google Maps.")
        else:
            speak("What should I search for?")

    elif "search" in c.lower():
        query = c.lower().replace("search", "").strip()

        if query:
            search_google(query)
            speak(f"Searching Google for {query}.")
        else:
            speak("What should I search for?")

    elif "open website" in c.lower():
        url = c.lower().replace("open website", "").strip()

        if url:
            open_url(url)
            speak(f"Opening {url}.")
        else:
            speak("Please tell me the website you want to open.")

    elif "remind me in" in c.lower():
        parts = c.lower().split()

        number = int(parts[3])
        unit = parts[4]

        if unit.startswith("minute"):
            seconds = number * 60
        else:
            seconds = number

        reminder_text = " ".join(parts[6:])

        speak("Okay, I will remind you.")

        timed_reminder(
            reminder_text,
            seconds,
            speak
        )

    elif "remind me" in c.lower():
        reminder_text = c.lower().replace("remind me", "").strip()

        if reminder_text:
            add_reminder(reminder_text)
            speak("Okay, I will remember that.")
        else:
            speak("What should I remind you about?")

    elif "clear" in c.lower() and "reminders" in c.lower():
        clear_reminders()
        speak("All your reminders have been cleared.")


    elif "reminders" in c.lower():
        reminders = get_reminders()

        if reminders:
            speak("Your reminders are:")
            for reminder in reminders:
                speak(reminder)
        else:
            speak("You don't have any reminders.")

    elif "open notepad" in c.lower():
        if open_app("notepad"):
            speak("Opening Notepad.")
        else:
            speak("Sorry, I couldn't open Notepad.")

    elif "open calculator" in c.lower():
        if open_app("calculator"):
            speak("Opening Calculator.")
        else:
            speak("Sorry, I couldn't open Calculator.")

    elif "open file explorer" in c.lower():
        if open_app("file explorer"):
            speak("Opening File Explorer.")
        else:
            speak("Sorry, I couldn't open File Explorer.")

    elif "open vs code" in c.lower():
        if open_app("vs code"):
            speak("Opening VS Code.")
        else:
            speak("Sorry, I couldn't open VS Code.")

    elif "open edge" in c.lower():
        if open_app("edge"):
            speak("Opening Microsoft Edge.")
        else:
            speak("Sorry, I couldn't open Microsoft Edge.")

    elif "take screenshot" in c.lower():
        filename = take_screenshot()
        speak("Screenshot taken.")
        print("Screenshot saved as:", filename)

    elif "what is my volume" in c.lower() or "current volume" in c.lower():
        current_volume = get_volume()
        speak(f"Your current volume is {current_volume} percent.")

    elif "volume up" in c.lower():
        volume_up()
        speak("Volume increased.")

    elif "volume down" in c.lower():
        volume_down()
        speak("Volume decreased.")

    elif "unmute" in c.lower():
        unmute()
        speak("Volume unmuted.")

    elif "mute" in c.lower():
        mute()
        speak("Volume muted.")

    elif "set alarm" in c.lower():
        parts = c.lower().split()

        number = int(parts[3])
        unit = parts[4]

        if unit.startswith("minute"):
            seconds = number * 60
        else:
            seconds = number

        speak("Alarm set.")

        set_alarm(
            seconds,
            speak
        )

    elif "open downloads" in c.lower() or "open my downloads" in c.lower():
        if open_folder("downloads"):
            speak("Opening Downloads.")
        else:
            speak("Sorry, I couldn't open Downloads.")

    elif "open documents" in c.lower():
        if open_folder("documents"):
            speak("Opening Documents.")
        else:
            speak("Sorry, I couldn't open Documents.")

    elif "open desktop" in c.lower():
        if open_folder("desktop"):
            speak("Opening Desktop.")
        else:
            speak("Sorry, I couldn't open Desktop.")

    elif "open pictures" in c.lower() or "open my pictures" in c.lower():
        if open_folder("pictures"):
            speak("Opening Pictures.")
        else:
            speak("Sorry, I couldn't open Pictures.")

    elif "battery low" in c.lower():
        low = is_battery_low()

        if low:
            speak("Your battery is low. Please connect the charger.")
        else:
            speak("Your battery is not low.")

    elif "is my battery charging" in c.lower() or "battery charging" in c.lower():
        battery = get_battery()

        if battery:
            percentage, charging = battery

            if charging:
                speak(f"Yes, your battery is charging at {percentage} percent.")
            else:
                speak(f"No, your battery is not charging. It is at {percentage} percent.")
        else:
            speak("Sorry, I couldn't get the battery information.")

    elif "battery" in c.lower():
        battery = get_battery()

        if battery:
            percentage, charging = battery

            if charging:
                speak(f"Your battery is at {percentage} percent and it is charging.")
            else:
                speak(f"Your battery is at {percentage} percent.")
        else:
            speak("Sorry, I couldn't get the battery information.")

    elif "ram usage" in c.lower() or "ram uses" in c.lower() or "memory usage" in c.lower():
        ram = get_ram_usage()
        speak(f"Your RAM usage is {ram} percent.")

    elif "cpu usage" in c.lower() or "cpu" in c.lower():
        cpu = get_cpu_usage()
        speak(f"Your CPU usage is {cpu} percent.")

    elif "system information" in c.lower():
        system, ram, cpu = get_system_info()

        speak(
            f"You are using {system}. "
            f"RAM usage is {ram} percent. "
            f"CPU usage is {cpu} percent."
        )

    elif "find file" in c.lower():
        filename = c.lower().replace("find file", "").strip()

        if filename:
            result = search_file(filename)

            if result:
                speak("I found the file.")
                print("File found:", result)
                os.startfile(result)
            else:
                speak("Sorry, I couldn't find that file.")
        else:
            speak("Please tell me the file name.")

    elif "create file" in c.lower():
        filename = c.lower().replace("create file", "").strip()

        if filename:
            speak("What should I write in the file?")

            with sr.Microphone() as source:
                audio = recognizer.listen(source)

            content = recognizer.recognize_google(audio)

            path = create_text_file(filename, content)

            speak("Text file created.")
            print("File created:", path)

        else:
            speak("Please tell me the file name.")

    elif "lock computer" in c.lower():
        speak("Locking your computer.")
        lock_computer()

    elif "empty recycle bin" in c.lower():
        speak("Are you sure you want to empty the recycle bin?")

        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

        confirmation = recognizer.recognize_google(audio)

        if "yes" in confirmation.lower():
            if empty_recycle_bin():
                speak("Recycle bin emptied.")
            else:
                speak("Sorry, I couldn't empty the recycle bin.")
        else:
            speak("Okay, I won't empty the recycle bin.")

    elif "read clipboard" in c.lower():
        content = get_clipboard()

        if content:
            speak("Your clipboard says:")
            speak(content)
            print("Clipboard:", content)
        else:
            speak("Your clipboard is empty.")

    elif "copy text" in c.lower():
        speak("What should I copy?")

        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        copy_to_clipboard(text)

        speak("Text copied to clipboard.")

    elif "wifi settings" in c.lower() or "wi-fi settings" in c.lower():
        open_settings("wifi")
        speak("Opening Wi-Fi settings.")

    elif "bluetooth settings" in c.lower():
        open_settings("bluetooth")
        speak("Opening Bluetooth settings.")

    elif "display settings" in c.lower():
        open_settings("display")
        speak("Opening display settings.")

    elif "sound settings" in c.lower():
        open_settings("sound")
        speak("Opening sound settings.")

    elif "open settings" in c.lower():
        os.startfile("ms-settings:")
        speak("Opening Settings.")

    elif "open screenshots" in c.lower():
        if open_folder("screenshots"):
            speak("Opening Screenshots.")
        else:
            speak("Sorry, I couldn't open the Screenshots folder.")

    elif "restart computer" in c.lower():
        speak("Are you sure you want to restart your computer?")

        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

        confirmation = recognizer.recognize_google(audio)

        if "yes" in confirmation.lower():
            speak("Restarting your computer.")
            restart_computer()
        else:
            speak("Okay, I won't restart your computer.")

    elif "shut down computer" in c.lower() or "shutdown computer" in c.lower():
        speak("Are you sure you want to shut down your computer?")

        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

        confirmation = recognizer.recognize_google(audio)

        if "yes" in confirmation.lower():
            speak("Shutting down your computer.")
            shutdown_computer()
        else:
            speak("Okay, I won't shut down your computer.")

    elif "sleep computer" in c.lower():
        speak("Are you sure you want to put your computer to sleep?")

        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

        confirmation = recognizer.recognize_google(audio)

        if "yes" in confirmation.lower():
            speak("Putting your computer to sleep.")
            sleep_computer()
        else:
            speak("Okay, I won't put your computer to sleep.")

    elif "current brightness" in c.lower() or "what is my brightness" in c.lower():
        brightness = get_current_brightness()
        speak(f"Your current brightness is {brightness} percent.")

    elif "set brightness" in c.lower():
        parts = c.lower().split()

        level = int(parts[3])

        set_brightness(level)

        speak(f"Brightness set to {level} percent.")

    elif "increase brightness" in c.lower():
        increase_brightness()
        speak("Brightness increased.")

    elif "decrease brightness" in c.lower():
        decrease_brightness()
        speak("Brightness decreased.")

    elif "wifi status" in c.lower() or "is wifi connected" in c.lower() or "is wi-fi connected" in c.lower():
        if get_wifi_status():
            speak("Wi-Fi is connected.")
        else:
            speak("Wi-Fi is not connected.")

    elif "internet status" in c.lower() or "is internet working" in c.lower():
        if check_internet():
            speak("Internet is working.")
        else:
            speak("Internet is not working.")

    elif "open music" in c.lower() or "open my music" in c.lower():
        if open_folder("music"):
            speak("Opening Music.")
        else:
            speak("Sorry, I couldn't open the Music folder.")

    elif "open videos" in c.lower() or "open my videos" in c.lower():
        if open_folder("videos"):
            speak("Opening Videos.")
        else:
            speak("Sorry, I couldn't open the Videos folder.")

    elif "open task manager" in c.lower():
        if open_app("task manager"):
            speak("Opening Task Manager.")
        else:
            speak("Sorry, I couldn't open Task Manager.")

    elif "open command prompt" in c.lower():
        if open_app("command prompt"):
            speak("Opening Command Prompt.")
        else:
            speak("Sorry, I couldn't open Command Prompt.")


    else:
        #Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    load_timed_reminders(speak)

    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Calibration complete. Jarvis is ready.")

    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening for Jarvis...")

                # Give enough time to say "Jarvis"
                audio = recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Yes, I am listening")

                with sr.Microphone() as source:
                    print("Jarvis Active...")

                    try:
                        audio = recognizer.listen(
                            source,
                            timeout=5,
                            phrase_time_limit=5
                        )

                        command = recognizer.recognize_google(audio)
                        print("Command:", command)

                        processCommand(command)

                    except sr.UnknownValueError:
                        print("Could not understand the command.")
                        speak("Sorry, I didn't understand that.")

                    except sr.WaitTimeoutError:
                        print("You didn't say anything.")
                        speak("I didn't hear a command.")

        except sr.UnknownValueError:
            print("Could not understand audio. Listening again...")

        except sr.RequestError as e:
            print("Speech recognition service error:", e)

        except sr.WaitTimeoutError:
            print("Listening timed out. Listening again...")

        except Exception as e:
            print("Error:", e)