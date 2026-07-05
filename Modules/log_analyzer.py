import re
from datetime import datetime
from collections import defaultdict

PATTERNS = {
    "failed_login": r"Failed password|authentication failure|Invalid user",
    "successful_login": r"Accepted password|session opened",
    "port_scan": r"Invalid user|Did not receive identification",
    "sudo_attempt": r"sudo.+COMMAND",
}

def analyze_log(filepath):
    
    with open(filepath, "r") as f:
    
        for line in f:
            for pattern_name, pattern in PATTERNS.items():
                if re.search(pattern, line):
                    print(f"[!] DETECTED {pattern_name}: {line.strip()}")
                
                

def detect_brute_force(filepath, threshold=5):
    """
    Counts failed login attempts per IP.
    Flags any IP that exceeds the threshold as a brute force attack.
    """
    failed_attempts = defaultdict(int)
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    with open(filepath, "r") as f:
        for line in f:
            if re.search(PATTERNS["failed_login"], line):
                ip_match = re.search(ip_pattern, line)
                if ip_match:
                    ip = ip_match.group()
                    failed_attempts[ip] += 1

    print(f"\n[*] Brute Force Detection Results:")
    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(f"[!!!] BRUTE FORCE DETECTED - IP: {ip} | Failed attempts: {count}")
        else:
            print(f"[*] IP: {ip} | Failed attempts: {count}")
            
            
if __name__ == "__main__":
    # Create a fake log file to test against
    with open("test.log", "w") as f:
        f.write("Failed password for root from 192.168.1.100\n" * 10)
        f.write("Accepted password for user from 192.168.1.200\n")
        f.write("Failed password for admin from 192.168.1.105\n" * 3)

    analyze_log("test.log")
    detect_brute_force("test.log", threshold=5)