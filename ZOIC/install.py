import os
import sys
from pystyle import Colorate, Colors

def install():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.cyan_to_green,"""
                              
                    ┌─┐┌─┐┌┬┐┬ ┬┌─┐
                    └─┐├┤  │ │ │├─┘
                    └─┘└─┘ ┴ └─┘┴    
                                                                    
            Dox                    Doxweb [close]
                            
  https://rvlt.gg/PnjMbQwH   https://doxwebd.serveo.net          
                              
           
                            
"""))
    print("""
     ██╗ ██████╗ ██╗  ██╗███╗   ██╗    ██████╗     ██╗ ██████╗ 
     ██║██╔═══██╗██║  ██║████╗  ██║    ╚════██╗██╗███║██╔════╝ 
     ██║██║   ██║███████║██╔██╗ ██║     █████╔╝╚═╝╚██║███████╗ 
██   ██║██║   ██║██╔══██║██║╚██╗██║     ╚═══██╗██╗ ██║██╔═══██╗
╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║    ██████╔╝╚═╝ ██║╚██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═════╝     ╚═╝ ╚═════╝
          """)
    os.system("pip install aiosonic --break-system-packages")
    os.system("pip install re --break-system-packages")
    os.system("pip install cloudscraper --break-system-packages")
    os.system("pip install aiohttp --break-system-packages")
    os.system("pip install scapy --break-system-packages")
    os.system("git pull")

if __name__ == "__main__":
    install()
