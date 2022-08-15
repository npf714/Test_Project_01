import socket
import time

host = input("Please specify the IP address you would like to scan: ")
port_input = int(input("Enter the total number of ports to scan: "))
print(f"Scanning {port_input} ports on host {host}")

def portScanner():
    t1 = time.process_time()
    for port in range(port_input):
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = scan.connect_ex((host, port_input))
        if result == 0:
            print(f"Port {port} is open")
        else:
            False

    t2 = time.process_time()
    print("Scan time was", t2 - t1 / 60, "Minutes")

if __name__=='__main__':
    portScanner()
