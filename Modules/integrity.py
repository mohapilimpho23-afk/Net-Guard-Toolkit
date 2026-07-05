import hashlib
import os
import json
from datetime import datetime

def hash_file(filepath):

    """
    Reads a file and returns its SHA-256 hash as a hex string.
    A different hash means the file has been modified.
    """
    
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f: 
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def create_baseline(directory):
    baseline = {}
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != ".git"]
        files = [f for f in files if f != "baseline.json"]
        for filename in files:
            filepath = os.path.join(root, filename)
            baseline[filepath] = hash_file(filepath)
            
    
    
    with open("baseline.json", "w") as f:
        json.dump(baseline, f, indent=4)
    
    print(f"[*] Baseline created with {len(baseline)} files saved to baseline.json")
    


def check_integrity(directory):
    
    """
    Compares current file hashes against the saved baseline.
    Flags any files that have been modified, deleted or added.
    Run this after create_baseline to detect changes.
    """
    
    
    
    with open("baseline.json", "r") as f:
        baseline = json.load(f)
        
        
    current = {}
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != ".git"]
        files = [f for f in files if f != "baseline.json"]
        for filename in files:
            filepath = os.path.join(root, filename)
            current[filepath] = hash_file(filepath)
            
    for filepath in baseline:
        if filepath in current:
            if baseline[filepath] != current[filepath]:
                print(f"[!] MODIFIED: {filepath}")
        
        else:
            print(f"[-] DELETED: {filepath}")
            
    for filepath in current:
        if filepath not in baseline:
            print(f"[+] NEW FILE: {filepath}")
           




if __name__ == "__main__":
    # create_baseline("C:/Users/mohap/Elective Repos/Net-Guard-Toolkit")
    check_integrity("C:/Users/mohap/Elective Repos/Net-Guard-Toolkit")