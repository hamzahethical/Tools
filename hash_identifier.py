#!/usr/bin/env python3
"""
Cryptographic Hash Algorithm Identifier
Author: Md Hamzah (@hamzahethical)
"""

import re
import argparse

HASH_PATTERNS = [
    (r"^[a-fA-F0-9]{32}$", ["MD5", "NTLM", "MD4", "LM", "RIPEMD-128"]),
    (r"^[a-fA-F0-9]{40}$", ["SHA-1", "RIPEMD-160", "MySQL5"]),
    (r"^[a-fA-F0-9]{56}$", ["SHA-224", "SHA3-224"]),
    (r"^[a-fA-F0-9]{64}$", ["SHA-256", "SHA3-256", "RIPEMD-256"]),
    (r"^[a-fA-F0-9]{96}$", ["SHA-384", "SHA3-384"]),
    (r"^[a-fA-F0-9]{128}$", ["SHA-512", "SHA3-512", "Whirlpool"]),
    (r"^\$2[aby]?\$\d{2}\$[./A-Za-z0-9]{53}$", ["bcrypt"]),
    (r"^\$6\$[a-zA-Z0-9./]{1,16}\$[a-zA-Z0-9./]{86}$", ["SHA-512 Crypt (Linux shadow)"]),
    (r"^\$1\$[a-zA-Z0-9./]{1,8}\$[a-zA-Z0-9./]{22}$", ["MD5 Crypt (Linux shadow)"]),
    (r"^\$argon2(i|d|id)\$v=\d+\$m=\d+,t=\d+,p=\d+\$", ["Argon2"]),
]

def identify_hash(hash_str):
    hash_str = hash_str.strip()
    matches = []
    for pattern, algos in HASH_PATTERNS:
        if re.match(pattern, hash_str):
            matches.extend(algos)
    return matches

def main():
    parser = argparse.ArgumentParser(description="Cryptographic Hash Identifier")
    parser.add_argument("-s", "--string", required=True, help="Hash string to analyze")
    args = parser.parse_args()

    results = identify_hash(args.string)
    print(f"\n[*] Hash Length: {len(args.string.strip())} characters")
    if results:
        print("[+] Probable Hash Algorithms:")
        for r in results:
            print(f"    - {r}")
    else:
        print("[-] Unknown or unsupported hash format.")

if __name__ == "__main__":
    main()
