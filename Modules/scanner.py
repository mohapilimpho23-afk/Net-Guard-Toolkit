import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime 

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Proxy",
}

def scan_port(target , port):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((target, port))
        return result == 0
    finally:
        sock.close()
        
        
# NOTE: scan_range was replaced by threaded_scan for performance.
# scan_range checked ports one at a time (slow for large ranges).
# threaded_scan checks 100 ports simultaneously using ThreadPoolExecutor.
            
def check_and_print(target, port):
    if scan_port(target, port):
        service = COMMON_PORTS.get(port, "Unknown")
        print(f"[+] Port {port} OPEN  ({service})")
        
              
            
def threaded_scan(target, start_port, end_port):
    print(f"[*] Scanning: {target}")
    print(f"[*] Port range: {start_port} - {end_port}")
    
    start_time = datetime.now()    
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(check_and_print, target, port)
    
    duration = datetime.now() - start_time 
    print(f"\n[*] Scan completed in {duration}")
            

    
   
    
        
        
        
        
if __name__ == "__main__":
    threaded_scan("scanme.nmap.org", 1, 1000)
 
 