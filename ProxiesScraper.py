from requests import get
import os
import platform

class Colors:
    end = '\x1b[0m'
    green = '\x1b[0;32m'

def updatetitle():
    if platform.system() == 'Windows':
        content = f"Proxies Scraper"
        os.system(f"title {content}")
def clear():
    if platform.system() != 'Windows':
        os.system('clear')
        return None
    os.system('cls')
def choices():
    clear()
    logo = f'''{Colors.green}
  _____               _                _____                                
 |  __ \\             (_)              / ____|                               
 | |__) | __ _____  ___  ___  ___    | (___   ___ _ __ __ _ _ __   ___ _ __ 
 |  ___/ '__/ _ \\ \\/ / |/ _ \\/ __|    \\___ \\ / __| '__/ _` | '_ \\ / _ \\ '__|
 | |   | | | (_) >  <| |  __/\\__ \\    ____) | (__| | | (_| | |_) |  __/ |   
 |_|   |_|  \\___/_/\\_\\_|\\___||___/   |_____/ \\___|_|  \\__,_| .__/ \\___|_|   
                                                           | |              
                                                           |_|              
{Colors.end}'''
    print(logo)
    print(f'''
    │ {Colors.green}Proxies :{Colors.end}
    ├──────────
    │
    │ [{Colors.green}1{Colors.end}] HTTP                [{Colors.green}3{Colors.end}] socks 4
    │ [{Colors.green}2{Colors.end}] HTTPS               [{Colors.green}4{Colors.end}] socks 5
    │''')
    choice = input("    └───> ")

    if choice == "1": Proxies("-http")
    elif choice == "2": Proxies("-https")
    elif choice == "3": Proxies("-socks4")
    elif choice == "4": Proxies("-socks5")
    else: choices()

def Proxies(Type):
    r = get(f'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies{Type}.txt')
    data = r.text
    if Type == "":
    	file = f"Proxies-All.txt"
    else:
    	file = f"Proxies{Type}.txt"
    with open(file, "w+") as f:
        f.write(str(data))
    print(f"\t\t\tProxies successfully update !\n\t\t\tSave in : {Colors.green}{file}{Colors.end}")
    input("\n\n\t\t\t Press enter to exit >")
    choices()
updatetitle()
choices()
