#!/usr/bin/env python3
"""
Subdomain Discovery & HTTP Status Checker
Author: Md Hamzah (@hamzahethical)
"""

import socket
import urllib.request
import argparse
from concurrent.futures import ThreadPoolExecutor

def check_subdomain(domain, sub, timeout=3.0):
    fqdn = f"{sub.strip()}.{domain}"
    try:
        ip = socket.gethostbyname(fqdn)
        status = "DNS-Resolved"
        try:
            req = urllib.request.Request(f"https://{fqdn}", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                status = f"HTTPS {resp.status}"
        except Exception:
            try:
                req = urllib.request.Request(f"http://{fqdn}", headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    status = f"HTTP {resp.status}"
            except Exception:
                pass
        print(f"[FOUND] {fqdn:35s} -> {ip:15s} [{status}]")
        return fqdn
    except socket.gaierror:
        return None

def main():
    parser = argparse.ArgumentParser(description="Subdomain Recon Prober")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g. example.com)")
    parser.add_argument("-w", "--wordlist", help="Path to subdomains wordlist file")
    parser.add_argument("-th", "--threads", type=int, default=20, help="Threads count")
    args = parser.parse_args()

    default_subs = ["www", "mail", "api", "dev", "admin", "vpn", "portal", "test", "staging", "auth", "login", "cdn", "cloud", "remote", "secure"]
    subs = default_subs
    if args.wordlist:
        with open(args.wordlist, "r") as f:
            subs = [line.strip() for line in f if line.strip()]

    print(f"[*] Probing {len(subs)} subdomains for {args.domain}...\n")
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for sub in subs:
            executor.submit(check_subdomain, args.domain, sub)

if __name__ == "__main__":
    main()
