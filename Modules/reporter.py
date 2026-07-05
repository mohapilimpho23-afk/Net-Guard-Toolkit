import json
from datetime import datetime

def save_json_report(data , filename):
    
    data["timestamp"] = datetime.now().isoformat()
    
    with open(f"{filename}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"[*] Report saved to {filename}")
    


def save_html_report(data, filename):
    """
    Saves scan results as a readable HTML report.
    """
    html = f"""
    <html>
    <head>
        <title>NetGuard Report</title>
        <style>
            body {{ font-family: Arial; background: #1a1a2e; color: #eee; padding: 20px; }}
            h1 {{ color: #00ff88; }}
            pre {{ background: #16213e; padding: 15px; border-radius: 8px; }}
            .timestamp {{ color: #888; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <h1>🛡️ NetGuard Security Report</h1>
        <p class="timestamp">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <pre>{json.dumps(data, indent=4)}</pre>
    </body>
    </html>
    """
    
    with open(f"{filename}.html", "w", encoding="utf-8") as file:
        file.write(html)
    print(f"[*] Report saved to {filename}")
    
    
if __name__ == "__main__":
    test_data = {
        "scan_target": "scanme.nmap.org",
        "open_ports": [22, 80],
        "hosts_alive": ["192.168.18.1", "192.168.18.4"],
        "threats_detected": ["Brute force from 192.168.1.100"]
    }
    
    save_json_report(test_data, "netguard_report")
    save_html_report(test_data, "netguard_report")