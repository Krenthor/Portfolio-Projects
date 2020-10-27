import PySimpleGUI as sg

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.

layout = [[sg.Text("Sum of Multiples")],
          #[sg.Text("First Multiple    "), sg.InputText(key='1v')],
          [sg.Text("First Multiple"), sg.Spin(values=(' 1', '2', '3', '4', '5', '6', '7', '8', '9'), initial_value='1', key='1v')],
          [sg.Text("Second Multiple"), sg.Spin(values=(' 1', '2', '3', '4', '5', '6', '7', '8', '9'), initial_value='1', key='2v')],
          [sg.Text("Top of Range    "),sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=100, key='xrange')],
          [sg.Text("Your Answer"), sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Sum of Multiples', layout)

# Display and interact with the Window using an Event Loop



while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    top = int(values['xrange'])
    first_var = int(values['1v'])
    second_var = int(values['2v'])

    first = list(range(0, top, first_var))
    second = list(range(0, top, second_var))

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    else:
        for num in first:
            if num not in second:
                second.append(num)
                ip = str(sum(second))
    # Output a message to the window
                window['-OUTPUT-'].update(" " + ip + " ! Thanks for trying ")





# Finish up by removing from the screen
window.close()