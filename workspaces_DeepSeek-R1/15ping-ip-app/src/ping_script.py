def ping_ip(ip_address):
    import subprocess

    try:
        # Execute the ping command
        output = subprocess.check_output(["ping", "-c", "4", ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error pinging {ip_address}: {e.output}"

if __name__ == "__main__":
    ip = input("Enter an IP address to ping: ")
    result = ping_ip(ip)
    print(result)