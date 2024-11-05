from os import listdirs


def is_public(ip):
    return not is_private(ip)


def is_private(ip):
    if ip.startswith('10'):
        return True
    return False
