import os
import sys
from pystyle import Colorate, Colors

def method_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.cyan_to_green,"""
                              
                       ┌┬┐┌─┐┌┬┐┬ ┬┌─┐┌┬┐
                       │││├┤  │ ├─┤│ │ ││
                       ┴ ┴└─┘ ┴ ┴ ┴└─┘─┴┘ 
                                                                                    
            ╔═════════════════════════════════════╗
            ║                                     ║
            ║  - layer7  |  show l7 module        ║
            ║  - layer4  |  show l4 module        ║
            ║  - Tools   |  show Tools module     ║
            ║                                     ║
            ║  - PLS PROJECT STAR                 ║
            ║  - GOD BLESS YOU                    ║
            ║                                     ║  
            ╚═════════════════════════════════════╝
 
"""))
    
    input(Colorate.Horizontal(Colors.cyan_to_green,"[ZOIC] Enter the continue..."))
