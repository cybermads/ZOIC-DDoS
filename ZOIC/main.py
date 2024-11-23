import os
import sys
from module.l4 import *
from module.l7 import *
from Tools.dns import *
from Tools.rdns import *
from update.main import *

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, """
███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║       
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗  
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝ 
          
--------------------------------------
Revolt : https://rvlt.gg/PeewQeV9
Github : https://github.com/madanokr001
coded by 건우Sec
--------------------------------------

ZOIC commands line:

update  |  update tool
exit    |  exit zoic  

l4      |  SYN FLOOD , UDP FLOOD   
l7      |  HTTP FLOOD , OVERFLOW  

dns     |  dns lockup
rdns    |  dns reverse                          
                   
"""))


def main():
    while True:
        logo()
        select = input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@ZOIC~$]                                                                   
═══> 
"""))
                                         
        if select == "update" or select.lower() == "1":
            upadate_main()

        elif select == "l4" or select.lower() == "4":
            layer4()

        elif select == "l7" or select.lower() == "5":
            layer7()

        elif select == "dns" or select.lower() == "5":
            dnslockup()

        elif select == "rdns" or select.lower() == "7":
            rdns()
            
        elif select == "exit" or select.lower() == "2":
            sys.exit()
    
             


if __name__ == "__main__":
    main()
