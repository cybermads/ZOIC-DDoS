import os
from methods.l4 import *
from methods.l7 import *
from Tools.main import *

zoic = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
clear = "\033[0m"
    
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
          {zoic}
                    ╔═╗╔═╗╦╔═╗
                    ╔═╝║ ║║║  
                    ╚═╝╚═╝╩╚═╝ V5{clear}

         Type "{zoic}help{clear}" to the view commands
""")


def main():
    while True:
        banner()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
                                        
        if select == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
          {zoic}
                    ╦ ╦╔═╗╦  ╔═╗
                    ╠═╣║╣ ║  ╠═╝
                    ╩ ╩╚═╝╩═╝╩ {clear}
                github.com/cybermads
        {zoic}╔═════════════════════════════════╗{clear}
        {zoic}║{clear}  {zoic}-{clear} l4     {zoic}|{clear} Layer4 Attack Menu  {zoic}║{clear}         
        {zoic}║{clear}  {zoic}-{clear} l7     {zoic}|{clear} Layer7 Attack Menu  {zoic}║{clear}
        {zoic}║{clear}  {zoic}-{clear} tools  {zoic}|{clear} Tools Menu          {zoic}║{clear}
        {zoic}║{clear}  {zoic}-{clear} update {zoic}|{clear} Update ZOIC         {zoic}║{clear}
        {zoic}╚═════════════════════════════════╝{clear}
                  """)
            input()


        elif select == "l4":
            layer4()

        
        elif select == "l7":
            print("")

        elif select == "tools":
            tools()

            
    
             


if __name__ == "__main__":
    main()


