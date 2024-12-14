import os
from pystyle import Colorate, Colors

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.cyan_to_green,"""
                    
                  ╔╦╗┌─┐┌─┐┬  ┌─┐
                   ║ │ ││ ││  └─┐
                   ╩ └─┘└─┘┴─┘└─┘
     
            ╔════════════════════════╗
            ║        [!help]         ║          https://rvlt.gg/PnjMbQwH 
            ║   Type to see command  ║
            ╚════════════════════════╝            
                     
"""))
    
def Tools_main():
    while True:
        logo()
        select = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@ZOIC]~$
╚══> """))
                                        
        if select == "!help" or select.lower() == "h":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Colorate.Horizontal(Colors.cyan_to_green,"""
                                      
                            ┬┬ ┬┌─┐┬  ┌─┐
                            │├─┤├┤ │  ├─┘
                            o┴ ┴└─┘┴─┘┴  
                                                                                    
                ╔═════════════════════════════════╗
                ║                                 ║
                ║  - port  |  PortScanner         ║
                ║                                 ║
                ║  - PLS PROJECT STAR             ║
                ║  - GOD BLESS YOU                ║
                ║                                 ║  
                ╚═════════════════════════════════╝

"""))
            input("")


        elif select == "port" or select.lower() == "p":

            ip_address = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@IP]~$
╚══> """))
            
            os.system(f"nmap {ip_address}")

            input(Colorate.Horizontal(Colors.cyan_to_green,"[ZOIC] Enter the continue..."))

            
            
            
    
            
    
             


if __name__ == "__main__":
    Tools_main()
