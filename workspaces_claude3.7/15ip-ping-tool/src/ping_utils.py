def ping_ip(ip_address):
    import subprocess

    try:
        # Execute the ping command
        output = subprocess.check_output(["ping", "-c", "4", ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output}"