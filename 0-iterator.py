#!/usr/bin/env python


## ietrable
names = ['Ali', 'Shahrokh', 'David']

## iterator
names_i = iter(names)

try:
    print(names_i.__next__())
    print(next(names_i))
    print(next(names_i))
    print(next(names_i))  ## StopIteration
except StopIteration:
    print('no more names.')

print('end')




for n in names:
    print(n)
