import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except socket.error:
        pass

def main():
    target_ip = input("Enter target IP address: ")
    port_start = int(input("Enter start port number: "))
    port_end = int(input("Enter end port number: "))

    print(f"\n[*] Starting scan on {target_ip} from port {port_start} to {port_end}...\n")

    threads = []

    for port in range(port_start, port_end + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Scan completed.")

if __name__ == "__main__":
    main()
