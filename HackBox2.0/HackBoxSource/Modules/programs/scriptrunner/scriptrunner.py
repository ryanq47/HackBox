import datetime
import wikipedia
import webbrowser
#import pynput.keyboard 
import os
#import sys
#import signal
import time
import subprocess
#import wolframalpha
import json
import requests
import glob

#file imports
print(r"""
 _____ _____ ______ ___________ ___________ _   _ _   _  _   _  ___________    __        _____ 
/  ___/  __ \| ___ \_   _| ___ \_   _| ___ \ | | | \ | || \ | ||  ___| ___ \  /  |      |  _  |
\ `--.| /  \/| |_/ / | | | |_/ / | | | |_/ / | | |  \| ||  \| || |__ | |_/ /  `| |      | |/' |
 `--. \ |    |    /  | | |  __/  | | |    /| | | | . ` || . ` ||  __||    /    | |      |  /| |
/\__/ / \__/\| |\ \ _| |_| |     | | | |\ \| |_| | |\  || |\  || |___| |\ \   _| |_  _  \ |_/ /
\____/ \____/\_| \_|\___/\_|     \_/ \_| \_|\___/\_| \_/\_| \_/\____/\_| \_|  \___/ (_)  \___/ 
                                                                                               
                                                                                               
                                                                                              
                                                                                              
                                                                            
                                                                            
""")
print('SCRIPTRUNNER! (1.0) An easy script running tool! Type help for help, or a script name to run it! EX: test.bat')
print('Current Available Scripts: ')

print('--')
#script sorter
print('Batch Files:')
print(glob.glob("Modules\programs\scriptrunner\scripts/*.bat"))
#os.path.basename('Modules\programs\scriptrunner\scripts\*.bat')

#map(os.path.basename, glob.glob("Modules\programs\scriptrunner\scripts\*"))
print('--')

print('PowerShell Files:')
print(glob.glob("scripts/*.ps"))
print(glob.glob("Modules\programs\scriptrunner\scripts/*.ps1"))
print('--')

print('Python Files:')
print(glob.glob("Modules\programs\scriptrunner\scripts/*.py"))
print('--')

print('SCRIPTRUNNER: What should I run?')
statement = input("").lower()

## make it autodisplay availabel scripts in directory

while True:
    # -- BATCH --
    if '.bat' in statement:
        print('running', statement)
        subprocess.Popen('start Modules\programs\scriptrunner\scripts\\{}'.format(statement), shell=True)
        print('SCRIPTRUNNER: What should I run?')
        
    # -- PowerShell --
    elif '.ps' in statement:
        print('running', statement)
        subprocess.Popen('powershell .\\Modules\programs\scriptrunner\scripts\\{}'.format(statement), shell=True)
        print('SCRIPTRUNNER: What should I run?')

    elif '.ps1' in statement:
        print('running', statement)
        subprocess.Popen('powershell .\\Modules\programs\scriptrunner\scripts\\{}'.format(statement), shell=True)
        print('SCRIPTRUNNER: What should I run?')
    elif '.py' in statement:
        print('running', statement)
        subprocess.Popen('python Modules\programs\scriptrunner\scripts\\{}'.format(statement), shell=True)
        print('SCRIPTRUNNER: What should I run?')

    # -- Execution Policy
    elif statement == 'ps policy bypass' :
        # Set-ExecutionPolicy -excecutionpolicy all -Scope CurrentUser <-- command to allow PS scripts to be run
        subprocess.Popen('powershell Set-ExecutionPolicy -executionpolicy bypass -Scope CurrentUser', shell=True)
        print('PS is now allowed to ALL run .ps, and .ps1 scripts - potentially dangerous')
        print('SCRIPTRUNNER: What should I run?')
    elif statement == 'ps policy allsigned' :
        # Set-ExecutionPolicy -excecutionpolicy all -Scope CurrentUser <-- command to allow PS scripts to be run
        subprocess.Popen('powershell Set-ExecutionPolicy -executionpolicy all -Scope CurrentUser', shell=True)
        print('PS is now allowed to run signed .ps, and .ps1 scripts')
        print('SCRIPTRUNNER: What should I run?')
    elif statement == 'ps policy restricted':
        subprocess.Popen('powershell Set-ExecutionPolicy -executionpolicy restricted -Scope CurrentUser', shell=True)
        print('SCRIPTRUNNER: What should I run?')
        print('PS is now restricted from running .ps, and .ps1 scripts')

    elif statement == 'ps policy default':
        subprocess.Popen('powershell Set-ExecutionPolicy -executionpolicy undefined -Scope CurrentUser', shell=True)
        print('SCRIPTRUNNER: What should I run?')
        print('PS Policy is now set to default')

    elif 'help' in statement:
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print('')
        print("'SCRIPTNAME.FILETYPE': Runs script if found in script folder")
        print(" EX: 'test.bat")
        print('')
        print(" --- Permissions ---")
        print('')
        print(" --- useful for if you have Poweshell script execution disabled")
        print("'ps policy bypass'                       : Allows ALL PS scripts to be run on local user - Potentially dangerous!!")
        print('')
        print("'ps policy all'                       : Allows all SIGNED PS scripts to be run on local user")
        print('')
        print("'ps policy restricted'                        : restricts PS scripts from being run ")
        print('')
        print("'ps policy default'                  : Sets default settings for PS scripts, may lead to different results based") 
        print("                                       on Domain settings")
        print("-----------------------------------------------------------------")

        print("SCRIPTRUNNER: Anything I can do for you?")
    elif statement == 'exit':
        print('SCRIPTRUNNERI: Exiting SCRIPTRUNNER')
        
        exec(open('HackBox.py').read()) 
    else:
        print('SCRIPTRUNNER: Invalid Paramater, type help for help, or exit to exit')

    statement = input("").lower()




  