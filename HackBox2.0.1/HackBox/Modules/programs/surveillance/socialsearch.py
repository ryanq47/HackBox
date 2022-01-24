
import webbrowser
print(r""")
 _____  _____ _____ _____  ___   _      _____ _____  ___  ______  _____  _   _    __   _____ 
/  ___||  _  /  __ \_   _|/ _ \ | |    /  ___|  ___|/ _ \ | ___ \/  __ \| | | |  /  | |  _  |
\ `--. | | | | /  \/ | | / /_\ \| |    \ `--.| |__ / /_\ \| |_/ /| /  \/| |_| |  `| | | |/' |
 `--. \| | | | |     | | |  _  || |     `--. \  __||  _  ||    / | |    |  _  |   | | |  /| |
/\__/ /\ \_/ / \__/\_| |_| | | || |____/\__/ / |___| | | || |\ \ | \__/\| | | |  _| |_\ |_/ /
\____/  \___/ \____/\___/\_| |_/\_____/\____/\____/\_| |_/\_| \_| \____/\_| |_/  \___(_)___/                                                                                                                                                                                          
            """)                                                                                            
                                                                                        
print('SOCIALSEARCH! Open/search profile pages faster! Works Great with USERNAMECHECK')



statement = input("").lower()

while True:
    if 'search' in statement :
        print('SOCIALSEARCH: Opening profiles for', statement, '...')
        statement =statement.replace("search ", "")
        webbrowser.open_new_tab('https://www.instagram.com/{}'.format(statement))
        webbrowser.open_new_tab('https://www.facebook.com/{}'.format(statement))
        webbrowser.open_new_tab('https://www.linkedin.com/search/results/all/?keywords={}'.format(statement))


    elif 'help' in statement:
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print("'Search USERNAME': Searches Facebook, Instagram, and Linkedin for typed username")
        print("")
        print("-----------------------------------------------------------------")

        print("SOCIALSEARCH: Anything I can do for you?")
    elif statement == 'exit':
        print('SOCIALSEARCH: Exiting SOCIALSEARCH')
        
        exec(open('HackBox.py').read()) 
    else:
        print('SOCIALSEARCH: Invalid Paramater, type help for help, or exit to exit')

    statement = input("").lower()




    ## maybe make this pop out on its own window - OR create a settings page taht the user can edit