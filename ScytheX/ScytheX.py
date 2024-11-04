import os
import sys
from Tools.main import *
from module.layer3 import *
from module.layer4 import *
from module.layer7 import *
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

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.BOLD + """
               ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#    
                    
 - update    |    update scytheX
 - Tools     |    ip tools
 - l3        |    Layer3 menu
 - l4        |    Layer4 menu
 - l7        |    Layer7 menu
 - exit      |    leave scytheX main 

    """ + TextColors.RESET)

def main():
    while True:
        logo()
        select = input(TextColors.BOLD + "root@ScytheX > " + TextColors.RESET)

        if select == "Tools" or select.lower() == "h":
            Tools()

        elif select == "update" or select.lower() == "up":
            update()

        elif select == "l3" or select.lower() == "3":
            layer3()

        elif select == "l4" or select.lower() == "4":
            layer4()

        elif select == "l7" or select.lower() == "7":
            print("Fix soon..")
            input()
            

        elif select == "exit" or select.lower() == "e":
            print(TextColors.RED + "[-] bye :("+ TextColors.RESET)
            sys.exit()
    
             


if __name__ == "__main__":
    main()
