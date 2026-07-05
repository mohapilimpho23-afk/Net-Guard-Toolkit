#!/usr/bin/env python3
"""
NetGuard - Network Security Monitoring Toolkit
-----------------------------------------------
Main entry point. Run any module from a single CLI command.

Usage:
    python main.py scan --target 192.168.1.1 --start 1 --end 1000
    python main.py discover --subnet 192.168.18.0/24
    python main.py integrity --action create --path ./
    python main.py integrity --action check --path ./
    python main.py analyze --log test.log
"""

import argparse
import sys
import os

# Tell Python where to find our modules
sys.path.append(os.path.join(os.path.dirname(__file__), "Modules"))

from scanner import threaded_scan
from monitor import discover_hosts
from integrity import create_baseline, check_integrity
from log_analyzer import analyze_log, detect_brute_force
from reporter import save_json_report, save_html_report


def print_banner():
    """Prints the NetGuard banner on startup."""
    print("""
    ███╗   ██╗███████╗████████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
    ████╗  ██║██╔════╝╚══██╔══╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
    ██╔██╗ ██║█████╗     ██║   ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
    ██║╚██╗██║██╔══╝     ██║   ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
    ██║ ╚████║███████╗   ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
    
    🛡️  Network Security Monitoring Toolkit
    ⚠️  For authorized use only
    """)


def handle_scan(args):
    """Handles the port scan module."""
    if not args.target:
        print("[!] Error: --target is required for scan")
        sys.exit(1)
    
    start = args.start or 1
    end = args.end or 1024
    
    results = {"target": args.target, "open_ports": []}
    print(f"\n[*] Starting port scan on {args.target}...\n")
    threaded_scan(args.target, start, end)
    
    if args.report:
        save_json_report(results, "scan_report")
        save_html_report(results, "scan_report")


def handle_discover(args):
    """Handles the host discovery module."""
    if not args.subnet:
        print("[!] Error: --subnet is required for discover")
        sys.exit(1)
    
    print(f"\n[*] Starting host discovery on {args.subnet}...\n")
    discover_hosts(args.subnet)
    
    if args.report:
        results = {"subnet": args.subnet}
        save_json_report(results, "discovery_report")
        save_html_report(results, "discovery_report")


def handle_integrity(args):
    """Handles the file integrity checker module."""
    if not args.path:
        print("[!] Error: --path is required for integrity")
        sys.exit(1)
    if not args.action:
        print("[!] Error: --action (create or check) is required for integrity")
        sys.exit(1)

    if args.action == "create":
        print(f"\n[*] Creating baseline for {args.path}...\n")
        create_baseline(args.path)
    elif args.action == "check":
        print(f"\n[*] Checking integrity of {args.path}...\n")
        check_integrity(args.path)
    else:
        print("[!] Error: --action must be 'create' or 'check'")
        sys.exit(1)


def handle_analyze(args):
    """Handles the log analyzer module."""
    if not args.log:
        print("[!] Error: --log is required for analyze")
        sys.exit(1)

    print(f"\n[*] Analyzing log file: {args.log}...\n")
    analyze_log(args.log)
    detect_brute_force(args.log)

    if args.report:
        results = {"log_file": args.log}
        save_json_report(results, "log_report")
        save_html_report(results, "log_report")


def main():
    """Main entry point — parses CLI arguments and routes to the right module."""
    print_banner()

    parser = argparse.ArgumentParser(
        description="NetGuard - Network Security Monitoring Toolkit",
        epilog="Always use on systems you own or have explicit permission to test."
    )

    # Which module to run
    parser.add_argument(
        "module",
        choices=["scan", "discover", "integrity", "analyze"],
        help="Module to run"
    )

    # Scan options
    parser.add_argument("--target", help="Target IP or hostname (for scan)")
    parser.add_argument("--start", type=int, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, help="End port (default: 1024)")

    # Discover options
    parser.add_argument("--subnet", help="Subnet to scan e.g. 192.168.1.0/24")

    # Integrity options
    parser.add_argument("--path", help="Directory path to monitor")
    parser.add_argument("--action", choices=["create", "check"], help="Create or check baseline")

    # Analyze options
    parser.add_argument("--log", help="Path to log file to analyze")

    # Shared options
    parser.add_argument("--report", action="store_true", help="Save results as JSON and HTML report")

    args = parser.parse_args()

    # Route to the right module
    if args.module == "scan":
        handle_scan(args)
    elif args.module == "discover":
        handle_discover(args)
    elif args.module == "integrity":
        handle_integrity(args)
    elif args.module == "analyze":
        handle_analyze(args)


if __name__ == "__main__":
    main()