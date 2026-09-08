import socket
import time


# =========================
# Recon Scan v2.0
# =========================

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Alt"
}


def scan_port(target, port):
    """Check if a TCP port is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            return True

    except socket.error:
        pass

    finally:
        sock.close()

    return False


def resolve_target(target):
    """Resolve a hostname or IP address."""
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None


def quick_scan(target):
    """Scan common ports."""
    print("\nStarting quick scan...")
    print("Target:", target)
    print()

    open_ports = []
    start_time = time.time()

    for port, service in COMMON_PORTS.items():
        if scan_port(target, port):
            print(f"[+] Port {port:<5} OPEN    {service}")
            open_ports.append((port, service))

    elapsed = time.time() - start_time

    print("\nScan complete.")
    print("Open ports:", len(open_ports))
    print(f"Scan time: {elapsed:.2f} seconds")

    if not open_ports:
        print("No open ports found.")

    return open_ports


def range_scan(target):
    """Scan a custom range of ports."""
    try:
        start = int(input("Start port: "))
        end = int(input("End port: "))

        if start < 1 or end > 65535:
            print("Port must be between 1 and 65535.")
            return

        if start > end:
            print("Start port cannot be greater than end port.")
            return

    except ValueError:
        print("Please enter valid port numbers.")
        return

    print(f"\nScanning ports {start}-{end}...")
    print()

    open_ports = []
    start_time = time.time()

    for port in range(start, end + 1):
        if scan_port(target, port):
            service = COMMON_PORTS.get(port, "Unknown")
            print(f"[+] Port {port:<5} OPEN    {service}")
            open_ports.append((port, service))

    elapsed = time.time() - start_time

    print("\nScan complete.")
    print("Open ports:", len(open_ports))
    print(f"Scan time: {elapsed:.2f} seconds")


def single_port_scan(target):
    """Scan one port."""
    try:
        port = int(input("Enter port: "))

        if port < 1 or port > 65535:
            print("Invalid port.")
            return

    except ValueError:
        print("Please enter a valid port.")
        return

    print(f"\nChecking port {port}...")

    if scan_port(target, port):
        service = COMMON_PORTS.get(port, "Unknown")
        print(f"[+] Port {port} is OPEN")
        print(f"[+] Service: {service}")
    else:
        print(f"[-] Port {port} is CLOSED")


def show_common_ports():
    """Display common ports."""
    print("\nCommon Ports")
    print()

    for port, service in COMMON_PORTS.items():
        print(f"{port:<6} {service}")


def start_scan():
    """Start a scan."""
    print("\nRecon Scan v2.0")
    print("----------------")
    print()

    target = input("Enter IP address or domain: ").strip()

    if not target:
        print("Target cannot be empty.")
        return

    print(f"\nResolving {target}...")

    ip = resolve_target(target)

    if not ip:
        print("Unable to resolve target.")
        return

    print(f"Target resolved to {ip}")

    print("""

Scan type:

1. Quick Scan
2. Port Range
3. Single Port
""")

    choice = input("Select option: ").strip()

    if choice == "1":
        quick_scan(ip)
    elif choice == "2":
        range_scan(ip)
    elif choice == "3":
        single_port_scan(ip)
    else:
        print("Invalid option.")


def main():
    print("Recon Scan v2.0")
    print()

    print("1. Start Scan")
    print("2. Exit")
    print()

    choice = input("Select option: ").strip()

    if choice == "1":
        start_scan()

    elif choice == "2":
        print("Exiting...")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
