#!/usr/bin/env python


from pathlib import Path, WindowsPath


path = '/home/nino/main/python-course/sample'


ips = [
    '1.2.3.4',
    '5.6.7.8',
]


## with is a context manager
with open(path, 'w') as f:
    for ip in ips:
        f.write(f'{ip}\n')
