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
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
     ██╗ ██████╗ ██╗  ██╗███╗   ██╗    ██████╗     ██╗ ██████╗ 
     ██║██╔═══██╗██║  ██║████╗  ██║    ╚════██╗██╗███║██╔════╝ 
     ██║██║   ██║███████║██╔██╗ ██║     █████╔╝╚═╝╚██║███████╗ 
██   ██║██║   ██║██╔══██║██║╚██╗██║     ╚═══██╗██╗ ██║██╔═══██╗
╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║    ██████╔╝╚═╝ ██║╚██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═════╝     ╚═╝ ╚═════╝
          """)
    os.system("pip install aiosonic")
    os.system("pip install re")
    os.system("pip install cloudscraper")
    os.system("pip install aiohttp")
    os.system("pip install scapy")
    os.system("git pull")

if __name__ == "__main__":
    install()
