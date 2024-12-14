import os
import sys
import time
import subprocess
from module.l4 import *
from module.l7 import *
from module.method import *
from Tools.main import *
from pystyle import Colorate, Colors

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.cyan_to_green,"""
                              
                    ╔═╗╔═╗╦╔═╗
                    ╔═╝║ ║║║  
                    ╚═╝╚═╝╩╚═╝    
                              
            ╔════════════════════════╗
            ║   [INFO] version 3.0   ║          https://rvlt.gg/PnjMbQwH 
            ║   [INFO] John 3:16     ║
            ╚════════════════════════╝            
                     
"""))
    subprocess.run("git pull", shell=True, stdout=subprocess.DEVNULL)
    input(Colorate.Horizontal(Colors.cyan_to_green,"[INFO] Enter the continue..."))
    
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.cyan_to_green,"""
                              
                    ╔═╗╔═╗╦╔═╗
                    ╔═╝║ ║║║  
                    ╚═╝╚═╝╩╚═╝    
                              
            ╔════════════════════════╗
            ║        [method]        ║          https://rvlt.gg/PnjMbQwH 
            ║   Type to see command  ║
            ╚════════════════════════╝            
                     
"""))


def main():
    while True:
        logo()
        select = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@ZOIC]~$
╚══> """))
                                        
        if select == "method" or select.lower() == "h":
            method_main()

        elif select == "layer7" or select.lower() == "l7":
            layer7()

        elif select == "layer4" or select.lower() == "l4":
            layer4()

        elif select == "Tools" or select.lower() == "t":
            Tools_main()
            
    
             


if __name__ == "__main__":
    check_main()
    main()
