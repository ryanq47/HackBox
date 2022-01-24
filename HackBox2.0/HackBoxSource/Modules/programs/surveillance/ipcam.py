
import webbrowser
print(r"""
 ___________   _____   ___  ___  ___   __   _____ 
|_   _| ___ \ /  __ \ / _ \ |  \/  |  /  | |  _  |
  | | | |_/ / | /  \// /_\ \| .  . |  `| | | |/' |
  | | |  __/  | |    |  _  || |\/| |   | | |  /| |
 _| |_| |     | \__/\| | | || |  | |  _| |_\ |_/ /
 \___/\_|      \____/\_| |_/\_|  |_/  \___(_)___/ 
                                                    
                """)

print('IPCAM! Find Publicly available cameras on the internet! Type Help For help!')

statement = input("").lower()

while True:
    if statement == 'ipcam':
        print('IPCAM: Pulling up cameras...')
        webbrowser.open_new_tab('http://www.insecam.org/en/byrating/')

    elif 'country' in statement:
        print('IPCAM: Pulling up cameras in', statement, '...')
        statement =statement.replace("country ", "")
        webbrowser.open_new_tab('http://www.insecam.org/en/bycountry/{}'.format(statement))

    elif 'place' in statement:
        print('IPCAM: Pulling up cameras in', statement, '...')
        statement =statement.replace("place ", "")
        webbrowser.open_new_tab('http://www.insecam.org/en/bytag/{}'.format(statement))

    elif 'city' in statement:
        print('IPCAM: Pulling up cameras in the', statement, '...')
        statement =statement.replace("city ", "")
        webbrowser.open_new_tab('http://www.insecam.org/en/bycity/{}'.format(statement))

    elif 'cameratype' in statement:
        print('IPCAM: Pulling up cameras in', statement, '...')
        statement =statement.replace("cameratype ", "")
        webbrowser.open_new_tab('http://www.insecam.org/en/bytype/{}'.format(statement))

    elif 'help' in statement:
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print("'Country __': Searches for cameras in said country, Please Use 2 letter code for countries")
        print("EX: 'country RU' for Russia")
        print('')
        print("'Place ___'                       : Pulls up cameras in certain places")
        print("EX: 'Place beach' to search a beach")
        print('')
        print("'City ___'                        : Pulls up cameras in Cities with open cams")
        print('')
        print("'Cameratype ___'                  : Pulls up cameras made by specific manufacturers, may be useful if exploit for") 
        print("                                    said camera is discovered")
        print("-----------------------------------------------------------------")

        print("IPCAM: Anything I can do for you?")
    elif statement == 'exit':
        print('IPCAM: Exiting IPCAM')
        
        exec(open('HackBox.py').read()) 
    else:
        print('IPCAM: Invalid Paramater, type help for help, or exit to exit')

    statement = input("").lower()




    ## maybe make this pop out on its own window - OR create a settings page taht the user can edit