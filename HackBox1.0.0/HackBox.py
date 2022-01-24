#V 1.0 by Ryan Kleffman 
#12/20/2021
#Basic interface, can take modules, forward commands, and open reddit (/s)

#ideas: change command output color?

#imports

#import speech_recognition as sr

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
#file imports




#VARS:
WEB = ['.com', ".edu", "org", ".gov"]
NETWORK = ['ping', 'ipconfig']


print('Loading Hackbox....................................................................')

print(r"""
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
                    """)




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

        print("'Search', 'Google', or 'Find'   : Find Relevant info in less clicks - works just like a search bar")
        print("'Summary'                       : Gives wikipedia summary, sometimes crashes so proceed at your own risk")
        print("'SITENAME'.com - ex; reddit.com : Type this in wherever, and it'll open said site,")
        print("                                : make sure to include .com, or .edu, etc!")
        print(" --- Custom Tools/Modules --- ")
        print("Netreport : A 'quick' net report of IP addresses, and connected ports to give an overview of your system's connections")
        print("-----------------------------------------------------------------")
        print("Note: Case does not matter - upper and lower work the same")
        print("Note pt2: Any standard CMD commands will work within Hackbox, just type it in")
        print(".................................................................")
        print("HackBox: Anything I can do for you?")


# -- passthrough commands
#Connection Shiz


#QOL
    #Terminal
    elif statement == ('new'):
        os.system('wt -w 0 nt')



# -- Personal Tools -------------------------------------------------------------------
    #NetReport - A "quick" net report of IP addresses, Connected Ports, and __ all congregated in one spot

        #print('anything else I can do?')
    elif statement == ('netreport'):
        #import netreport
        subprocess.call('start python modules/netreport.py', shell=True)
        print('Generating Report in new window...')
        print('HackBox: Anything else I can do?')
                

#------------------------------------------------------------------------------
#Internet
#Search Feature: 
 
    elif 'search' in statement:
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

    elif '.org' in statement:
	    
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)

    elif '.edu' in statement:
	    
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)

    elif '.gov' in statement:
	
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)

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


