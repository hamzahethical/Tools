# 🛠️ Ethical Hacking & Pentesting Tools

A curated suite of custom Python and Shell tools built by **Md Hamzah (@hamzahethical)** for reconnaissance, network scanning, cryptographic hash identification, and penetration testing workflows.

---

## 🧰 Included Tools

| Tool | Language | Description |
| :--- | :---: | :--- |
| [`port_scanner.py`](#1-fast-port-scanner-port_scannerpy) | Python 3 | Multithreaded TCP port scanner with service detection and banner grabbing. |
| [`sub_recon.py`](#2-subdomain-recon-sub_reconpy) | Python 3 | Subdomain probe and HTTP status responder for reconnaissance workflows. |
| [`hash_identifier.py`](#3-hash-identifier-hash_identifierpy) | Python 3 | Identifies hash algorithms (MD5, SHA1, SHA256, NTLM, bcrypt, etc.). |
| [`recon_suite.sh`](#4-recon-automation-recon_suitesh) | Bash | Automated bash pipeline for network enumeration and target probing. |

---

## 🚀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/hamzahethical/Tools.git
cd Tools

# Install required dependencies
pip install -r requirements.txt
```

---

## 📖 Usage Examples

### 1. Fast Port Scanner (`port_scanner.py`)
Scan top ports or a specific range with concurrent worker threads:
```bash
python port_scanner.py -t 192.168.1.1 -p 1-1000 -th 50
```

### 2. Subdomain Recon (`sub_recon.py`)
Probe list of subdomains for live HTTP/HTTPS services:
```bash
python sub_recon.py -d example.com -w subdomains.txt
```

### 3. Hash Identifier (`hash_identifier.py`)
Identify unknown hash types from capture dumps:
```bash
python hash_identifier.py -s 5f4dcc3b5aa765d61d8327deb882cf99
```

---

## ⚠️ Disclaimer
These tools are provided strictly for **educational and authorized security testing purposes**. Do not target any systems without prior written authorization from the owner.
