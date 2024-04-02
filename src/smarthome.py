import src.logger as lg
from PyP100 import PyL530

ip = "192.168.178.25"
email = "Florian_Weber89@web.de"
password = "#Dernau19!"


def lamp_control_logic():
    lamp = PyL530.L530(ip, email, password)
    lg.print_like_human("Connecting to lightsource...")
    lamp.handshake()
    lamp.login()
    client = lamp.getDeviceName()
    lg.print_like_human("Connected to " + client + "!")
    control_options(lamp)


def control_options(lamp):
    options = ['Turn on', 'Turn off', 'Brightness', 'Exit the process']

    while True:
        for idx, entry in enumerate(options, start=1):
            lg.print_like_human(lg.COLORS['yellow'] + f"{idx}. {entry}")
        choice = lg.input_like_human(
            lg.COLORS['blue'] + 'Choose a option by number. You can leave a mode by typing "exit". \nOption: ')
        try:
            selected_option = int(choice)
        except ValueError:
            lg.print_like_human("Please enter a valid number.")
            continue

        if selected_option < 1 or selected_option > len(options):
            print("Invalid option. Please try again.")
            continue

        if selected_option == 1:
            lamp.turnOn()
        elif selected_option == 2:
            lamp.turnOff()
        elif selected_option == 3:
            value = lg.input_like_human(lg.COLORS['blue'] + 'Choose a brightness between 1 and 100.')
            convertedvalue = int(value)
            if convertedvalue < 1 or convertedvalue > 100:
                print("Invalid option. Please try again.")
                continue
            lamp.setBrightness(convertedvalue)
        elif selected_option == 4:
            break
