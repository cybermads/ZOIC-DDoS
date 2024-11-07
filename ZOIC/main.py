import os
import sys
from module.l3 import *
from module.l4 import *
from module.l7 import *
from Tools.dns import *
from Tools.rdns import *
from update.main import *


class TextColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    PURPLE = '\033[35m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = "\033[01;01m"
    DARK_RED = "\033[38;5;124m"
    CRIMSON = "\033[38;5;196m"
    TOMATO = "\033[38;5;202m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m" 
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"
    LIGHT_WHITE = "\033[97m"
    DARK_GOLD = "\033[38;5;220m" 
    RICH_BLUE = "\033[38;5;32m"  
    TANGERINE = "\033[38;5;214m"
    SNOW = "\033[38;5;231m"      
    ELECTRIC_LIME = "\033[38;5;48m"
    STORMY_BLUE = "\033[38;5;24m" 
    RADICAL_RED = "\033[38;5;160m"
    DARK_GREEN = "\033[38;5;28m"
    SUPER_BRIGHT_LIME_GREEN = '\033[38;2;102;255;102m'
    BRIGHT_WHITE = '\033[97m'
    BRIGHT_LIME_GREEN_RGB = '\033[38;2;50;205;50m'

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.SUPER_BRIGHT_LIME_GREEN + """
███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║       
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗  
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝ 
    """+ TextColors.RESET)
    print(TextColors.BRIGHT_LIME_GREEN_RGB + """
--------------------------------------
Revolt : https://rvlt.gg/PeewQeV9
Github : https://github.com/madanokr001
coded by 건우Sec
--------------------------------------

ZOIC commands line:

update  |  update tool
exit    |  exit zoic  

l3      |  Layer3 module   
l4      |  Layer4 module   
l7      |  layer7 module   

dns     |  dns lockup
rdns    |  dns reverse


"""+ TextColors.RESET)


def main():
    while True:
        logo()
        select = input(TextColors.SUPER_BRIGHT_LIME_GREEN + """═══[root@ZOIC~$]                                                                   
═══> """ + TextColors.RESET)
                                         
        if select == "update" or select.lower() == "1":
            upadate_main()
    
        elif select == "l3" or select.lower() == "3":
            layer3()

        elif select == "l4" or select.lower() == "4":
            layer4()

        elif select == "l7" or select.lower() == "5":
            layer7()

        elif select == "dns" or select.lower() == "5":
            dnslockup()

        elif select == "rdns" or select.lower() == "7":
            rdns()
            
        elif select == "exit" or select.lower() == "2":
            sys.exit()
    
             


if __name__ == "__main__":
    main()
