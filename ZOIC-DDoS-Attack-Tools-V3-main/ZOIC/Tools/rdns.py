import socket
import os
from pystyle import Colorate, Colors

def rdns():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_cyan, """
██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗
██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝
██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗  
██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  
██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝ 
        """))
    
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    ip = input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@HOST-IP]                                                                   
═══> 
"""))

    domain = socket.gethostbyaddr(ip)

    print(Colorate.Horizontal(Colors.blue_to_cyan, f"""

    ════════════════════════════════
            REVERSE DNS INFO
    ════════════════════════════════

    IP Address     : {ip}

    Domain server  : {domain}

    ════════════════════════════════
        
        """))


    input()
