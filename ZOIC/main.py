import os
import sys
from module.l3 import *
from module.l4 import *
from module.l7 import *
from Tools.Lockup import *
from Tools.nmap import *
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

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_GREEN + """

███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║       Revolt : https://rvlt.gg/PeewQeV9  
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗  Github : https://github.com/madanokr001
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝
╔════════════════════════════════════════════════════════════════════╗
║                     https://doxwebd.serveo.net                     ║ 
║════════════════════════════════════════════════════════════════════║
║                                                                    ║                                                                        
║              [1] UPDATE   [3] LAYER 3   [6] NMAP                   ║
║              [2] EXIT     [4] LAYER 4   [7] DNSLOCKUP              ║
║                           [5] LAYER 7                              ║
║                                                                    ║
║                                                                    ║                                                                     
╚════════════════════════════════════════════════════════════════════╝
         
""")

def main():
    while True:
        logo()
        select = input(TextColors.GREEN + """═══[root@ZOIC~$]                                                                   
═══> """ + TextColors.RESET)
                                         
        if select == "1" or select.lower() == "1":
            upadate_main()
    
        elif select == "3" or select.lower() == "3":
            layer3()

        elif select == "4" or select.lower() == "4":
            layer4()

        elif select == "5" or select.lower() == "5":
            layer7()

        elif select == "7" or select.lower() == "5":
            dnslockup()

        elif select == "6" or select.lower() == "7":
            nmap_main()
            
        elif select == "2" or select.lower() == "2":
            sys.exit()
    
             


if __name__ == "__main__":
    main()
