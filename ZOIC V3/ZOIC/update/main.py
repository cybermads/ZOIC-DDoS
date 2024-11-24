import socket
import os
import subprocess
from pystyle import Colorate, Colors

def upadate_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_cyan, """
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝   version 2.3  
        """))
    
    subprocess.run(['git', 'pull'], check=True)
    print(Colorate.Horizontal(Colors.purple_to_blue, f"[+] ZOIC Updated !!"))


    input()
