import socket
import os
from pystyle import Colorate, Colors

def dnslockup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, """
██╗      ██████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ 
██║     ██╔═══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗
██║     ██║   ██║██║     █████╔╝ ██║   ██║██████╔╝
██║     ██║   ██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
███████╗╚██████╔╝╚██████╗██║  ██╗╚██████╔╝██║     
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝         
        """))
    
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    url = input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@URL]                                                                   
═══> 
"""))

    ip = socket.gethostbyname(url)

    print(Colorate.Horizontal(Colors.blue_to_cyan, f"""

    ════════════════════════════════
            DNS LOCKUP INFO
    ════════════════════════════════

    IP Address : {ip}

    Host name  : {url}

    ════════════════════════════════
        
        """))


    input()



