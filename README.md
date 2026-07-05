# 🛡️ NetGuard — Network Security Monitoring Toolkit

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=flat-square)
![Security](https://img.shields.io/badge/Focus-Blue%20Team%20%7C%20Defensive-1e90ff?style=flat-square)

> A modular, command-line security monitoring toolkit built for network visibility, threat detection, and incident response workflows. Designed for security analysts, students, and blue team practitioners.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Modules](#modules)
- [Sample Output](#sample-output)
- [Roadmap](#roadmap)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Overview

NetGuard is a defensive security toolkit that brings together core blue team capabilities into a single, modular Python project. Rather than relying on heavy third-party tools for every task, NetGuard is built from the ground up to be readable, extensible, and educational — making it ideal for understanding *how* security monitoring actually works at the code level.

It covers the four pillars of basic network defense:

- **Discovery** — know what's on your network
- **Monitoring** — detect changes and anomalies
- **Detection** — find suspicious patterns in logs
- **Reporting** — document findings clearly

---

## Features

| Feature | Description |
|---|---|
| 🔍 **Threaded Port Scanner** | Fast TCP port scanning with service identification and concurrency |
| 🌐 **Host Discovery** | ICMP ping sweep to map live hosts on a subnet |
| 🔒 **File Integrity Monitor** | SHA-256 baseline hashing to detect unauthorized file changes |
| 📋 **Log Analyzer** | Pattern-based detection of brute force, suspicious IPs, and anomalies |
| 📊 **Report Generator** | JSON and HTML report output for documentation and review |

---

## Project Structure

```
netguard/
│
├── main.py                  # CLI entry point — run everything from here
├── requirements.txt         # Project dependencies
├── .gitignore
├── README.md
│
└── modules/
    ├── scanner.py           # Threaded TCP port scanner
    ├── monitor.py           # Ping sweep / host discovery
    ├── integrity.py         # File integrity checker (SHA-256)
    ├── log_analyzer.py      # Log file pattern analysis
    └── reporter.py          # JSON + HTML report output
```

Each module is self-contained and can be imported or run independently — making it easy to add features without breaking existing ones.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/netguard.git
cd netguard

# Install dependencies
pip install -r requirements.txt
```

No external security frameworks required. Core modules use Python's standard library.

---

## Usage

All modules are accessible through the main CLI:

```bash
python main.py [module] [options]
```

### Quick Examples

```bash
# Scan ports 1-1024 on a target
python main.py scan --target 192.168.1.1 --ports 1-1024

# Discover live hosts on a subnet
python main.py discover --subnet 192.168.1.0/24

# Create a file integrity baseline
python main.py integrity --path /etc --baseline create

# Check for changes against baseline
python main.py integrity --path /etc --baseline check

# Analyze a log file for suspicious activity
python main.py analyze --log /var/log/auth.log

# Generate a full HTML report from latest scan
python main.py report --format html
```

---

## Modules

### 🔍 scanner.py — Threaded Port Scanner

Performs TCP connect scans across a port range using Python's `socket` library and `concurrent.futures` for speed. Identifies services on well-known ports and supports output to the reporter module.

**Key concepts:** TCP sockets, threading, service enumeration

---

### 🌐 monitor.py — Host Discovery

Sends ICMP pings across a subnet and reports which hosts are alive. Useful for baselining what devices should be present on your network, so new or unexpected hosts can be flagged.

**Key concepts:** Subnetting, ICMP, network mapping

---

### 🔒 integrity.py — File Integrity Checker

Computes SHA-256 hashes of files in a target directory and stores a baseline. On subsequent runs, it compares current hashes against the baseline and flags any files that have been added, removed, or modified — similar in concept to tools like Tripwire or AIDE.

**Key concepts:** Hashing, HIDS (Host-based Intrusion Detection), file system monitoring

---

### 📋 log_analyzer.py — Log Analyzer

Parses system or application log files and applies regex-based detection rules to identify:

- Brute force login attempts (repeated failures)
- Authentication successes after failures (possible credential stuffing)
- Access from unusual IP addresses
- Known suspicious patterns

**Key concepts:** Log analysis, pattern matching, SOC workflows

---

### 📊 reporter.py — Report Generator

Takes output from any module and generates structured reports in:
- **JSON** — machine-readable, useful for piping into other tools
- **HTML** — human-readable, shareable with a team or included in incident documentation

**Key concepts:** Data serialization, documentation, incident response

---

## Sample Output

```
==================================================
 NetGuard — Port Scanner
==================================================
[*] Target    : 192.168.1.1
[*] Port Range: 1 - 1024
[*] Threads   : 100
[*] Started   : 2025-01-15 09:32:01

[+] Port   22   OPEN  →  SSH
[+] Port   80   OPEN  →  HTTP
[+] Port  443   OPEN  →  HTTPS

[*] Scan complete in 4.3 seconds
[*] 3 open ports found
[*] Report saved to: reports/scan_192.168.1.1_20250115.json
```

---

## Roadmap

This project is actively developed. Planned features in order of priority:

- [x] Project structure and README
- [ ] `scanner.py` — threaded port scanner
- [ ] `monitor.py` — host discovery / ping sweep
- [ ] `integrity.py` — file integrity checker
- [ ] `log_analyzer.py` — log analysis engine
- [ ] `reporter.py` — JSON + HTML reporting
- [ ] `main.py` — unified CLI entry point
- [ ] Unit tests for each module
- [ ] Configuration file support (YAML)
- [ ] Alerting via email / webhook on detection events
- [ ] Dashboard (web UI) for report visualization

---

## Disclaimer

> **NetGuard is intended strictly for educational purposes and authorized use only.**
>
> Only run this tool against systems and networks you own or have **explicit written permission** to test. Unauthorized scanning or monitoring of systems may be illegal under laws such as the Computer Fraud and Abuse Act (CFAA) and similar legislation in other countries.
>
> The author takes no responsibility for misuse of this tool.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Built for learning. Built for defense. 🛡️</p>
