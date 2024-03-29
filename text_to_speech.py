import os
from time import sleep
import pyttsx3

SETTINGS_FILE = 'settings.txt'

engine = pyttsx3.init('sapi5')


def save(content, filename='tts', gender='male'):
    full_filename = f'{filename}.mp3'
    # Voice gender
    if gender[0] == 'm':
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
    else:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

    if filename == '':
        filename = 'tts'
    engine.save_to_file(content, full_filename)
    engine.runAndWait()
    print('File %s saved successfully' % full_filename)


def speak(content, gender='male'):
    # Voice gender
    if gender[0] == 'm':
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
    else:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

    engine.say(content)
    engine.runAndWait()


def create_settings(settings_file):
    """ Handles the setup of a settings.txt file """
    settings = []

    print("------------BEGIN CREATING SETTINGS------------\n")

    # Save file or not
    save_or_not = input("Save the text in a file? [Y]es/[N]o\n").lower()
    try:
        while save_or_not[0] not in ['y', 'n']:
            print('Invalid input. Expecting: "YES" or "NO"')
            save_or_not = settings.append(input("YES or NO\n").lower())
        else:
            settings.append(save_or_not)
    except IndexError:  # Default to Name
        save_or_not = 'no'
        print(save_or_not)
        settings.append(save_or_not)

    # Voice gender
    male_or_female = input("[M]ale or [F]emale voice?\n").lower()
    try:
        while male_or_female[0] not in ['m', 'f']:
            print('Invalid input. Expecting: "MALE" or "FEMALE"')
            male_or_female = settings.append(input("MALE or FEMALE\n").lower())
        else:
            settings.append(male_or_female)
    except IndexError:
        male_or_female = 'male'
        print(male_or_female)
        settings.append(male_or_female)

    # Write the settings down and exit the file
    with open(settings_file, 'w') as f:
        counter = 0
        for setting in settings:
            if counter != len(settings) - 1:
                f.write("%s\n" % setting)
            else:  # Don't put a newline after the last setting
                f.write(setting)
            counter += 1
    close_app("\n\nThe app will now close.\nPlease reopen it for changes to take effect.")


def check_for_stop(string_to_check: str):
    if string_to_check.lower() == 's' or string_to_check.lower() == 'stop' or string_to_check.lower() == 'exit':
        close_app("Thank you for using the app!\nHave a nice day!")


def check_for_setup(string_to_check: str):
    if string_to_check.lower() == 'setup':  # The user requested a new setup
        try:
            os.remove(SETTINGS_FILE)
            create_settings(SETTINGS_FILE)
        except FileNotFoundError:
            with open(SETTINGS_FILE, 'x') as f:
                pass
            create_settings(SETTINGS_FILE)


def close_app(message, sleep_time=3):
    print(message)
    sleep(sleep_time)
    exit(1)
