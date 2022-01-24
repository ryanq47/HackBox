import os
import webbrowser
import sys
print(r"""
 _   _ _____ ___________   _____  _   _  _____ _____  _   __   __   _____ 
| | | /  ___|  ___| ___ \ /  __ \| | | ||  ___/  __ \| | / /  /  | |  _  |
| | | \ `--.| |__ | |_/ / | /  \/| |_| || |__ | /  \/| |/ /   `| | | |/' |
| | | |`--. \  __||    /  | |    |  _  ||  __|| |    |    \    | | |  /| |
| |_| /\__/ / |___| |\ \  | \__/\| | | || |___| \__/\| |\  \  _| |_\ |_/ /
 \___/\____/\____/\_| \_|  \____/\_| |_/\____/ \____/\_| \_/  \___(_)___/ 
            """)

print('USERCHECK! Find where a username is being used! Type help for help, or type in a username!')

statement = input("").lower()

while True:
    if 'check' in statement:
        print('USERCHECK: Checking common sites for users...')
        statement =statement.replace("check ", "")
        webbrowser.open_new_tab('https://knowem.com/checkusernames.php?u={}'.format(statement))


    elif 'help' in statement:
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print("'check USERNAME': Searches most common sites for usernames in use")
        print("EX: check bobbert123")
        print('')
        print("'exit': Exits back to HackBox")
        #print("'NOT: enter 'socialsearch' to enter socialsearch at any time!")
        print("-----------------------------------------------------------------")

        print("USERCHECK: Anyone else you wanna spy on creep?")

    #elif statement == 'socialsearch':   
        #print('USERCHECK: Opening SocialSearch')
        #exec(open('socialsearch.py').read()) 
    elif statement == 'exit':   
        print('USERCHECK: Exiting USERCHECK')
        exec(open('HackBox.py').read()) 


        
        

    else:
        print('USERCHECK: Invalid Paramater, type help for help, or exit to exit')


    statement = input("").lower()



    ## maybe make this pop out on its own window - OR create a settings page taht the user can edit