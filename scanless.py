import socket
import threading

def show_banner():
    banner = r"""
    =================================                       
          Port Scanner - Scanless
    =================================
    """
    print(banner)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"--> [OPEN]   Port {port} detected open on {ip}")
        sock.close()
    except socket.error:
        pass

def main():
    show_banner()

    target_ip = input("Enter the target IP address: ")
    port_start = int(input("Enter the start port number: "))
    port_end = int(input("Enter the end port number: "))

    print("\n" + "="*50)
    print(f" Starting port scan for {target_ip}")
    print(f" Port range: {port_start} to {port_end}")
    print("="*50 + "\n")

    threads = []

    for port in range(port_start, port_end + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n" + "="*50)
    print(" Scan completed.")
    print("="*50)

if __name__ == "__main__":
    main()
