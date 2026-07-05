import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import sys


def ping_host(ip):
    
    command = ["ping", "-n", "1", "-w", "500", ip] if sys.platform == "win32" else ["ping", "-c", "1", "-W", "1", ip]

    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0  


def check_and_print_host(ip):     
    if ping_host(str(ip)):
        print(f"[+] Host ALIVE: {ip}")


def discover_hosts(subnet):
    print(f"[*] Scanning subnet: {subnet}")
    
    start_time = datetime.now()
    
    network = ipaddress.ip_network(subnet, strict=False)
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in network.hosts():
            executor.submit(check_and_print_host, ip) 
            
    duration = datetime.now() - start_time
    print(f"\n[*] Discovery completed in {duration}")
    
if __name__ == "__main__":
    discover_hosts("192.168.18.0/24")