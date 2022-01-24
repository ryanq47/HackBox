#V 1.0 by Ryan Kleffman 
#12/20/2021
#Basic interface, can take modules, forward commands, and open reddit (/s)

#ideas: change command output color?

#imports

#import all needed below, otherwise exe errors out

import datetime
import wikipedia
import webbrowser
import keyboard
import smtplib
#import pynput.keyboard 
import os
#import sys
#import signal
import time
import subprocess
#import wolframalpha
import json
import requests
#file imports


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#VARS:
WEB = ['.com', ".edu", "org", ".gov"]
NETWORK = ['ping', 'ipconfig']


print('Loading Hackbox....................................................................')

print(r"""f"{bcolors.WARNING}
                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`              
               | |       ,.`  `,` `, | |  _,...(   (      _',               
   -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
    -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/             
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /          -HACKBOX SHELL-
  ,>,_ )_,..(    )\          -,,_-`  _--`                -RYANQ.47-
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```
                    {bcolors.ENDC}""")




print("HackBox: Hello, What Can I do for you?")
print("--(type help for a list of commands)--")

statement = input("").lower()
while True:
#Intro
    if statement == ("hi"):
	    print ("Hackbox: Hello"); print("Hackbox: Anything else I can do?")

    elif statement == ("help"):
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print("'new'                           : Opens a Blank Empty shell in new window")
        print("'refresh'                       : Reloads Hackbox") 
        
        print("'Search', 'Google', or 'Find'   : Find Relevant info in less clicks - works just like a search bar")
        print("'Summary'                       : Gives wikipedia summary, sometimes crashes so proceed at your own risk")
        print("'SITENAME'.com - ex; reddit.com : Type this in wherever, and it'll open said site,")
        print("                                : make sure to include .com, or .edu, etc!")
        print("-----------------------------------------------------------------")
        print(" --- Custom Tools/Modules --- ")
        print("NETREPORT    : A 'quick' net report of IP addresses, and connected ports to give an overview of your system's connections!")
        print("SCRIPTRUNNER    : A built in easy script execution shell, just pop your script in the scripts folder!")       
        print(" --- External Tools/Modules --- ")
        print("IPCAM        : A free database of publicly accessible cameras all over the world")
        print("USERCHECK    : See if a username is being used anywhere!")
        print("SOCIALSEARCH : Open a direct FB, Insta, and Linkedin Page with just a (valid) username!")
        print("KEYLOGGER    : A Keylogger that records to a file, or sends to your email - use at your own discretion")
        print("-----------------------------------------------------------------")
        print(" --- Arguments ---")
        print("'-w'                           : Opens any tool in a new window")
        print("-----------------------------------------------------------------")
        print("Note:")
        print("-  Case does not matter - upper and lower work the same")
        print("-  Any standard CMD commands should work within Hackbox, just type it in")
        print(".................................................................")
        print("HackBox: Anything I can do for you?")


# -- passthrough commands
#Connection Shiz


#QOL
    #Terminal
    elif statement == ('new'):
        os.system('wt -w 0 nt')

    elif statement == 'refresh':
        os.system('cls')
        exec(open('HackBox.py').read()) 



# -- Personal Tools -------------------------------------------------------------------
    #NetReport - A "quick" net report of IP addresses, Connected Ports, and __ all congregated in one spot

        #print('anything else I can do?')
    elif statement == ('netreport'):
        #import netreport
        subprocess.call('start python modules/netreport.py', shell=True)
        print('Generating Report in new window...')
        print('HackBox: Anything else I can do?')

    elif statement == ('scriptrunner -w'):
        subprocess.call('start python modules/programs/scriptrunner/scriptrunner.py', shell=True)
        print('Opening Scriptrunner in new window...')
        print('HackBox: Anything else I can do?')
    elif statement == ('scriptrunner'):
        exec(open('modules/programs/scriptrunner/scriptrunner.py').read()) 
        print('Opening Scriptrunner in new window...')
        print('HackBox: Anything else I can do?')

# --- programs --- 
# --- tools not created by me, but useful for a variety of things ---
    elif statement == 'ipcam':
        #print('hi')
        exec(open('Modules/programs/surveillance/ipcam.py').read()) 
    elif statement == 'ipcam -w':
        #print('hi')
        subprocess.call('start python Modules/programs/surveillance/ipcam.py', shell=True)
        print('HackBox: Anything else I can do?')


    elif statement == 'usercheck':
        #print('hi')
        exec(open('Modules/programs/surveillance/usercheck.py').read()) 
    elif statement == 'usercheck -w':
        #print('hi')
        subprocess.call('start python Modules/programs/surveillance/usercheck.py', shell=True)
        print('HackBox: Anything else I can do?')



    elif statement == 'socialsearch':
        #print('hi')
        exec(open('Modules/programs/surveillance/socialsearch.py').read()) 
    elif statement == 'socialsearch -w':
        #print('hi')
        subprocess.call('start python Modules/programs/surveillance/socialsearch.py', shell=True)
        print('HackBox: Anything else I can do?')
        
    elif statement == 'keylogger':
        exec(open('Modules/programs/keylogger/keylogger.py').read()) 
    elif statement == 'keylogger -w':
        subprocess.call('start python Modules/programs/keylogger/keylogger.py', shell=True)
        print('HackBox: Anything else I can do?')
        
        #add email or file option, and a -f for fast start
# -- Functions --

        #exec(open('Modules/programs/scripts/{}'.format(statement)))
        #statement =statement.replace("script ", "")


#------------------------------------------------------------------------------
#Internet
#Search Feature: 
 
    elif 'search' in statement and statement != 'socialsearch':
        print('Searching The Internet for' , statement, "...")
        statement =statement.replace("search", "")
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(statement))

        print('HackBox: Anything else I can do?')

    elif 'google' in statement:
        print('Searching The Internet for' , statement, "...")
        statement =statement.replace("google", "")
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(statement))
 
        print('HackBox: Anything else I can do?')

    elif 'find' in statement:
        
        statement =statement.replace("find", "")
        print('Searching The Internet for' , statement, "...")
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(statement))

        print('HackBox: Anything else I can do?')

    elif 'summary' in statement:
        print('Searching The Internet...')
        statement =statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=2)
        print("---------------------------------------------------------------")
        print("According to the Internet:")
        print(results)  
        print("---------------------------------------------------------------")
        print('HackBox: Anything else I can do?')

        # direct website connect
    elif '.com' in statement:
	
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)
        print("Anything else I can do for you?")

    elif '.org' in statement:
	    
        webbrowser.open_new_tab('https://{}'.format(statement))
        
        print("Going to", statement)
        print("Anything else I can do for you?")

    elif '.edu' in statement:
	    
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)
        print("Anything else I can do for you?")

    elif '.gov' in statement:
	
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)
        print("Anything else I can do for you?")

    #This is a loop that allows for any value in CMD to be checked, and run MUST GO LAST
    elif any((c in NETWORK) for c in NETWORK):
        print('---------------------------------------------------')
        os.system(statement)
        print('---------------------------------------------------')
        print("Anything else I can do for you?")
#------------------------------------------------------------------------------
    else:
        print('invalid command - type new for standard shell')
    statement = input("").lower()



os.system('pause')


