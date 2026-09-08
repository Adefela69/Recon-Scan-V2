# Recon Scan

A simple Python-based network reconnaissance and TCP port scanning tool.

Recon Scan was originally created as a basic Python port scanner and later updated with an interactive command-line interface, target resolution, custom port scanning, and basic service identification.

## Features

- IP address and domain resolution
- Quick scan of common ports
- Custom port range scanning
- Single-port scanning
- Basic service identification
- Interactive command-line interface
- Scan timing
- No external Python packages required

## Requirements

- Python 3.x
- Windows, Linux, or macOS

The project uses Python's built-in libraries, so no additional packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Recon-Scan.git
cd Recon-Scan
```

Run the program:

### Windows

```powershell
python main.py
```

### Linux / Kali

```bash
python3 main.py
```

## Usage

Start the program and select an option from the menu:

```text
Recon Scan v2.0

1. Start Scan
2. Common Ports
3. About
4. Exit

Select option:
```

### Start a scan

Select `1. Start Scan`, then enter an IP address or domain.

The program provides:

```text
1. Quick Scan
2. Port Range
3. Single Port
```

### Quick Scan

Scans a predefined list of commonly used ports.

### Port Range

Allows you to specify a custom range of ports, such as `1` to `100`.

### Single Port

Checks one specific TCP port.

## Project Structure

```text
Recon-Scan/
├── screenshots/
│   └── recon-scan.png
├── .gitignore
├── LICENSE
├── README.md
└── main.py
```

## Technologies

- Python
- Socket programming
- TCP
- DNS resolution
- Command-line interface

## Learning Objectives

This project was created to practice:

- Python programming
- Network programming
- TCP/IP concepts
- Port scanning
- DNS resolution
- Basic network reconnaissance
- Command-line application design

## Disclaimer

This tool is intended for educational purposes, cybersecurity labs, CTFs, and systems that you own or have explicit permission to test.

Do not scan systems or networks without authorization.

## Version

**Recon Scan v2.0**

### Changelog

#### v2.0

- Added interactive menu
- Added quick scanning
- Added custom port range scanning
- Added single-port scanning
- Added IP/domain resolution
- Improved terminal output
- Added basic service identification

#### v1.0

- Initial Python port scanning implementation
