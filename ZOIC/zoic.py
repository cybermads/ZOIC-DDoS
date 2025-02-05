import os
import sys
import time
import subprocess
from module.l7 import *
from module.l4 import *
from module.l3 import *

zoic = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{zoic}
███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║     
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝       
{clear}""")
    
    print(f"[{zoic}ZOIC{clear}] {white}Welcome ZOIC DDoS Attack Tools{clear}")
    print(f"[{zoic}ZOIC{clear}] {white}Join DoxGroup !! https://rvlt.gg/PnjMbQwH{clear}")
    os.system("pip install aiohttp --break-system-packages")
    input(f"[{zoic}ZOIC{clear}] {white}Enter the continue...{clear}")
    
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{zoic}
███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║       
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝{clear}
          
╔═════════════════════════════════════════════════════╗
║ {zoic}*{clear} Github    {zoic}:{clear}   https://github.com/madanokr001      ║
║ {zoic}*{clear} DoxServer {zoic}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {zoic}*{clear} version   {zoic}:{clear}   4.0                                 ║
║ {zoic}*{clear} Created   {zoic}:{clear}   CyberMAD                            ║
╚═════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════╗
║ {zoic}[{clear}1{zoic}]{clear} Update ZOIC                                     ║
║ {zoic}[{clear}2{zoic}]{clear} Layer3 Attack Methods                           ║     
║ {zoic}[{clear}3{zoic}]{clear} Layer4 Attack Methods                           ║               
║ {zoic}[{clear}4{zoic}]{clear} Layer7 Attack Methods                           ║
║ {zoic}[{clear}5{zoic}]{clear} nmap                                            ║                                    
║ {zoic}[{clear}6{zoic}]{clear} Exit ZOIC                                       ║          
╚═════════════════════════════════════════════════════╝                              
""")


def main():
    while True:
        logo()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
                                        
        if select == "1" or select.lower() == "u":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{zoic}
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                  {clear}""")
            subprocess.run("git pull", shell=True, stdout=subprocess.DEVNULL)
            print(f"[{zoic}ZOIC{clear}] Update Success!")
            input(f"[{zoic}ZOIC{clear}] Enter the continue...")

        elif select == "6" or select.lower() == "e":
            sys.exit()

        elif select == "5" or select.lower() == "e":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{zoic}
███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
                {clear}""")
            
            target = input(f"[{zoic}ZOIC{clear}] IP       {zoic}>{clear} ")
            
            os.system(f"nmap {target}")
            input(f"[{zoic}ZOIC{clear}] Enter the continue...")

        elif select == "2" or select.lower() == "2":
            layer3()

        elif select == "3" or select.lower() == "3":
            layer4()

        elif select == "4" or select.lower() == "4":
            layer7()
            
    
             


if __name__ == "__main__":
    check_main()
    main()
