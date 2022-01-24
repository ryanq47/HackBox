import os

print(r"""
 _   _  _____ ___________ ___________ ___________ _____   __   _____ 
| \ | ||  ___|_   _| ___ \  ___| ___ \  _  | ___ \_   _| /  | |  _  |
|  \| || |__   | | | |_/ / |__ | |_/ / | | | |_/ / | |   `| | | |/' |
| . ` ||  __|  | | |    /|  __||  __/| | | |    /  | |    | | |  /| |
| |\  || |___  | | | |\ \| |___| |   \ \_/ / |\ \  | |   _| |_\ |_/ /
\_| \_/\____/  \_/ \_| \_\____/\_|    \___/\_| \_| \_/   \___(_)___/ 
                                                                     
                                                                      
                                                        
                    """)                                                  


N = open("sysinfo/networkreport.txt", "w")
N = open('sysinfo/networkreport.txt', "r")

print('Generating Netreport, may take a minute...')

print('------------------------------------------------------------------')
print('Grabbing Adapter Info...')
os.system('ipconfig >> sysinfo/networkreport.txt')
            ##os.system('ipconfig | findstr /i "ipv6 ada" >> networkreport.txt')
print('Done')
print('Scanning local ports... Slowest Part')
os.system('netstat >> sysinfo/networkreport.txt')
print('Writing to file...')
os.system('arp -a >> sysinfo/networkreport.txt')
print('------------------------------------------------------------------')
print(N.read())

print('^^Saved to Netreport.txt under sysinfo folder^^')

os.system('pause')