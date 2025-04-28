def validate_ip(ip_address):
    import re
    
    # Regular expression for validating an IP address
    ip_pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    
    if ip_pattern.match(ip_address):
        # Split the IP address into octets and check if each is in the valid range
        octets = ip_address.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)
    
    return False