import nmap

print("=== Nmap Port Scanner Tool ===")


target = input("Enter target IP or hostname: ")
ports = input("Enter port range (e.g., 20-100): ")


scanner = nmap.PortScanner()

print(f"\n Scanning {target} on ports {ports}...\n")


scanner.scan(hosts=target, ports=ports, arguments='-sS')

if target in scanner.all_hosts():
    print(f" Host: {target}")
    print(f" State: {scanner[target].state()}")

    for proto in scanner[target].all_protocols():
        print(f"\n[+] Protocol: {proto}")
        ports = scanner[target][proto].keys()
        for port in sorted(ports):
            state = scanner[target][proto][port]['state']
            print(f"Port {port}: {state}")
else:
    print(" Host is down or unreachable.")

print("\n Scan complete.")
