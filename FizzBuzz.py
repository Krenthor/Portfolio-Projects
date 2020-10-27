import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

layout = [[sg.Text("Please input integer to see if multiple of 3 or 5")],
          [sg.InputText(key='IP')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Fizz_Buzz', layout)

# Display and interact with the Window using an Event Loop

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    ip = int(values['IP'])

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif ip % 5 == 0 and ip % 3 == 0:
        ip = "Fizz_Buzz "
    elif ip % 3 == 0:
        ip ="Fizz "
    elif ip % 5 == 0:
        ip ="Buzz "

    else:
        ip = "Plop "

    # Output a message to the window

    window['-OUTPUT-'].update('Your answer :' + ip + "! Thanks for trying ")

# Finish up by removing from the screen
window.close()