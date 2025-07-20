# Simple Host Discovery Tool - No Libraries

print("=== Host Discovery Tool ===")

# Ask user to input their default gateway manually
gateway = input("Enter your Default Gateway IP (e.g., 192.168.1.1): ")

# Validate IP format (basic)
parts = gateway.split('.')
if len(parts) != 4:
    print(" Invalid IP format!")
else:
    try:
        first = int(parts[0])
        if not (0 <= first <= 255):
            raise ValueError
        
        # Determine IP class
        if 1 <= first <= 126:
            ip_class = "Class A"
        elif 128 <= first <= 191:
            ip_class = "Class B"
        elif 192 <= first <= 223:
            ip_class = "Class C"
        elif 224 <= first <= 239:
            ip_class = "Class D (Multicast)"
        elif 240 <= first <= 254:
            ip_class = "Class E (Experimental)"
        else:
            ip_class = "Unknown Class"

        print(f" Gateway IP: {gateway}")
        print(f" IP Class: {ip_class}")
    
    except:
        print(" Invalid IP address. Please use numbers only.")
