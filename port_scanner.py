import socket
from datetime import datetime

# Input the target IP address
target = input("Enter the target IP address (e.g., 192.168.1.1): ")
start_port = int(input("Enter the start port (e.g., 1): "))
end_port = int(input("Enter the end port (e.g., 1024): "))

# Print banner information
print("-" * 50)
print(f"Starting scan on host: {target}")
print(f"Scanning ports {start_port} to {end_port}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)  # Set a timeout for each port scan attempt
    result = s.connect_ex((target, port))
    s.close()
    return result == 0

try:
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(port):
            print(f"Port {port} is open")
            open_ports.append(port)
except KeyboardInterrupt:
    print("\nScan interrupted by user")
except socket.gaierror:
    print("Hostname could not be resolved")
except socket.error:
    print("Could not connect to server")

# Display scan summary
print("-" * 50)
print(f"Scan completed for {target}")
print(f"Open ports: {open_ports}")
print(f"Time finished: {datetime.now()}")
print("-" * 50)

if open_ports:
    print(f"Open ports: {open_ports}")
else:
    print("No open ports found in the specified range.")
