import socket

print("=== Simple Port Scanner ===")

target = input("Enter target IP (e.g., 192.168.1.1): ")
start_port = int(input("Enter starting port (e.g., 1): "))
end_port = int(input("Enter ending port (e.g., 100): "))

print(f"\n Scanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f" Port {port} is OPEN")
    
    sock.close()

print("\n Scan complete.")
