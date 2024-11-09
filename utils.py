def is_public(ip):
    return not is_private(ip)


def is_private(ip):
    if ip.startswith('192'):
        return True
    return False
