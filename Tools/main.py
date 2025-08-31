import requests
import os
import socket
import ipaddress

zoic = "\033[38;5;118m"
red = "\033[38;5;196m"
clear = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
telegram {zoic}|{clear} t.me/cybermads {zoic}|{clear} Discord {zoic}|{clear} discord.gg/KDzjfn63
          {zoic}
                      ╔╦╗╔═╗╔═╗╦  ╔═╗
                       ║ ║ ║║ ║║  ╚═╗
                       ╩ ╚═╝╚═╝╩═╝╚═╝  {clear}
                    github.com/cybermads
           {zoic}╔═══════════════════════════════════╗{clear}
           {zoic}║{clear}  {zoic}-{clear} geoip   {zoic}|{clear} geolocation ip       {zoic}║{clear}         
           {zoic}║{clear}  {zoic}-{clear} dns     {zoic}|{clear} DNS lockup           {zoic}║{clear}
           {zoic}║{clear}  {zoic}-{clear} subnet  {zoic}|{clear} Reverse DNS lockup   {zoic}║{clear}
           {zoic}╚═══════════════════════════════════╝{clear}

""")              
    
def tools():
    while True:
        banner()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)
                                        
        if select.startswith("geoip"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{zoic}:{clear} {zoic}geoip{clear} <{zoic}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def geoip():
                r = requests.get(f"http://ip-api.com/json/{ip}")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
            {zoic}╔══════════════════════════════════{clear}
            {zoic}║{clear} IP{zoic}:{clear} {zoic}[{clear}{r.json().get("query")}{zoic}]{clear}              
            {zoic}║{clear} Country{zoic}:{clear} {zoic}[{clear}{r.json().get("country")}{zoic}]{clear}        
            {zoic}║{clear} Region{zoic}:{clear} {zoic}[{clear}{r.json().get("regionName")}{zoic}]{clear}       
            {zoic}║{clear} City{zoic}:{clear} {zoic}[{clear}{r.json().get("city")}{zoic}]{clear}               
            {zoic}║{clear} ISP{zoic}:{clear} {zoic}[{clear}{r.json().get("isp")}{zoic}]{clear}        
            {zoic}║{clear} Latitude{zoic}:{clear} {zoic}[{clear}{r.json().get("lat")}{zoic}]{clear}               
            {zoic}║{clear} Longitude{zoic}:{clear} {zoic}[{clear}{r.json().get("lon")}{zoic}]{clear}        
            {zoic}║{clear} ZIP{zoic}:{clear} {zoic}[{clear}{r.json().get("zip")}{zoic}]{clear}                     
            {zoic}╚══════════════════════════════════{clear}
                      """)
                input()

            geoip()

        elif select.startswith("dns"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{zoic}:{clear} {zoic}dns{clear} <{zoic}domain{clear}>")
                input()
                continue

            host = parts[1]

            def dnslockup():
                try:
                    dns = socket.gethostbyname(host)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
            {zoic}╔══════════════════════════════════{clear}
            {zoic}║{clear} HOST{zoic}:{clear} {zoic}[{clear}{host}{zoic}]{clear}              
            {zoic}║{clear} DNS{zoic}:{clear} {zoic}[{clear}{dns}{zoic}]{clear}          
            {zoic}╚══════════════════════════════════{clear}
                    """)
                except socket.gaierror:
                    pass
                input()

            dnslockup()


        elif select.startswith("subnet"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{zoic}:{clear} {zoic}subnet{clear} <{zoic}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def subnet():
                try:
                    n = ipaddress.ip_network(ip + "/24", strict=False)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
                {zoic}╔════════════════════════════════════════════════╗{clear}
                {zoic}║{clear} IP       {zoic}:{clear} [{ip}]
                {zoic}║{clear} SUBNET   {zoic}:{clear} [{n}]
                {zoic}║{clear} NET ADDR {zoic}:{clear} [{n.network_address}]
                {zoic}║{clear} BROADCAST{zoic}:{clear} [{n.broadcast_address}]
                {zoic}║{clear} NETMASK  {zoic}:{clear} [{n.netmask}]
                {zoic}║{clear} HOSTS    {zoic}:{clear} [{n.num_addresses}] addresses
                {zoic}╚════════════════════════════════════════════════╝{clear}
                    """)
                except Exception:
                    pass

                input()

            subnet()

if __name__ == "__main__":
    tools()


