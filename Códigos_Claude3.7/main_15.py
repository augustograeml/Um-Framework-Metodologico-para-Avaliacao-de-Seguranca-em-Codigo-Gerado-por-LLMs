import subprocess
from ping_utils import ping_ip
from validators import validate_ip

def main():
    ip_address = input("Enter an IP address to ping: ")
    
    if validate_ip(ip_address):
        result = ping_ip(ip_address)
        print(result)
    else:
        print("Invalid IP address format.")

if __name__ == "__main__":
    main()