import PySimpleGUI as sg

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.

layout = [[sg.Text("Check if its a palindrome")],
          [sg.InputText(key='IP')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Palindrome Checker', layout)

# Display and interact with the Window using an Event Loop


while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    ip = values['IP']
    new_word = ip[::-1].replace(" ", "").lower()
    old_word = ip.replace(" ", "").lower()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif old_word == new_word:
        window['-OUTPUT-'].update('Your answer is a PALINDROME! Thanks for trying ')

    else:
        window['-OUTPUT-'].update('Your answer is not a palindrome... Thanks for trying i guess')

    # Output a message to the window

    # window['-OUTPUT-'].update('Your answer :' + ip + "! Thanks for trying ")

# Finish up by removing from the screen
window.close()