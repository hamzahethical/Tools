#!/usr/bin/env bash
# Reconnaissance Automation Pipeline
# Author: Md Hamzah (@hamzahethical)

TARGET=$1
if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target-domain-or-ip>"
    exit 1
fi

OUTPUT_DIR="recon_results_${TARGET}"
mkdir -p "$OUTPUT_DIR"

echo "=========================================="
echo " Starting Reconnaissance on: $TARGET"
echo " Results will be saved to: $OUTPUT_DIR"
echo "=========================================="

echo "[1] Checking DNS Records..."
dig +nocmd "$TARGET" any +multiline +noall +answer > "$OUTPUT_DIR/dns_records.txt" 2>/dev/null

echo "[2] Running Whois Lookup..."
whois "$TARGET" > "$OUTPUT_DIR/whois.txt" 2>/dev/null

echo "[3] Performing TCP Port Sweep on Top Ports..."
if command -v nmap &> /dev/null; then
    nmap -sV -sC -T4 --top-ports 100 "$TARGET" -oN "$OUTPUT_DIR/nmap_top100.txt"
fi

echo "[✓] Reconnaissance complete. Results saved in $OUTPUT_DIR"
