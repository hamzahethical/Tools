#!/usr/bin/env python3
"""
Fast Multithreaded TCP Port Scanner with Banner Grabbing
Author: Md Hamzah (@hamzahethical)
"""

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 111: "RPCBIND", 135: "MSRPC",
    139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    993: "IMAPS", 995: "POP3S", 1433: "MSSQL", 1521: "Oracle",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    8080: "HTTP-Proxy", 8443: "HTTPS-Alt"
}

def grab_banner(target, port, timeout=2.0):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((target, port))
        try:
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            first_line = banner.splitlines()[0] if banner else ""
            return first_line
        except Exception:
            return ""
        finally:
            s.close()
    except Exception:
        return ""

def scan_port(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            banner = grab_banner(target, port, timeout)
            banner_info = f" | Banner: {banner}" if banner else ""
            print(f"[+] Port {port:5d}/TCP open  [{service}]{banner_info}")
            return port
    except Exception:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="Multithreaded TCP Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g., 1-1024, 80,443)")
    parser.add_argument("-th", "--threads", type=int, default=50, help="Number of concurrent threads")
    parser.add_argument("--timeout", type=float, default=1.5, help="Socket timeout in seconds")
    args = parser.parse_args()

    print(f"[*] Scanning Target: {args.target}")
    ports = []
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = list(range(start, end + 1))
    elif "," in args.ports:
        ports = [int(p.strip()) for p in args.ports.split(",")]
    else:
        ports = [int(args.ports)]

    print(f"[*] Scanning {len(ports)} ports using {args.threads} threads...\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for port in ports:
            executor.submit(scan_port, args.target, port, args.timeout)

if __name__ == "__main__":
    main()
