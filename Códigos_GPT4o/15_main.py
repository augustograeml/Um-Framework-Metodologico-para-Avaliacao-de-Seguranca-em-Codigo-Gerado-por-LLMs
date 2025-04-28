import subprocess

def ping_ip(ip_address):
    try:
        # Execute the ping command
        output = subprocess.check_output(["ping", "-c", "4", ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error pinging {ip_address}: {e.output}"

def main():
    ip_address = input("Enter an IP address to ping: ")
    result = ping_ip(ip_address)
    print(result)

if __name__ == "__main__":
    main()