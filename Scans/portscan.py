import socket
import sys

host = "localhost"


def scan(host, ports, timeout=0.5):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(timeout)
            code = client.connect_ex((host, int(port)))
            if code == 0:
                print(f"[+] {port} open")
    except:
        print("error, something is wrong")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(",")
        else:
            ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]
        
        scan(host, ports)
    else:
        print("Usage: python portscan.py google.com 22,23,80,443")