import socket
import os

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
    RADICAL_RED = "\033[38;5;160m"
    BRIGHT_LIME_GREEN_RGB = '\033[38;2;50;205;50m'
    SUPER_BRIGHT_LIME_GREEN = '\033[38;2;102;255;102m'

def dnslockup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.SUPER_BRIGHT_LIME_GREEN + """
██╗      ██████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ 
██║     ██╔═══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗
██║     ██║   ██║██║     █████╔╝ ██║   ██║██████╔╝
██║     ██║   ██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
███████╗╚██████╔╝╚██████╗██║  ██╗╚██████╔╝██║     
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝         
        """+ TextColors.RESET)
    
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    url = input(TextColors.SUPER_BRIGHT_LIME_GREEN + """═══[root@URL]                                                                   
═══> """ + TextColors.RESET)

    ip = socket.gethostbyname(url)

    print(TextColors.CYAN + f"""

    ════════════════════════════════
            DNS LOCKUP INFO
    ════════════════════════════════

    IP Address : {ip}

    Host name  : {url}

    ════════════════════════════════
        
        """+ TextColors.RESET)


    input()



