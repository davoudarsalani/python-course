#!/usr/bin/env python


## list ------------------------------------------

# opertaing_systems = [
#     'Arch Linux',
#     'Ubuntu',
#     'CentOS',
#     'MAC OS',
#     'Linux Mint',
#     'FreeBSD',
# ]

## change nth element
# opertaing_systems[-1] = 'sth'

## add one element to list
# opertaing_systems.append('Windows')

## add multiple elements to list
# opertaing_systems.extend(['Windows', 'Unix'])

## add element to nth position
# opertaing_systems.insert(4, 'Sth')

## clear list
# opertaing_systems.clear()

## remove last element
# opertaing_systems.pop()

## remove nth element
# removed_element = opertaing_systems.pop(3)

## remove element by 'value'
# opertaing_systems.remove('CentOS')

## get index
# idx = opertaing_systems.index('MAC OS')
# print(idx)

## get occurrences of element
# count = opertaing_systems.count('CentOS')
# print(count)

## reverse
# method 1
# new = list(reversed(opertaing_systems))
#
## method 2 (changes original)
# opertaing_systems.reverse()
# print(opertaing_systems)

## sort
# method 1
# new = sorted(opertaing_systems)
#
## method 2 (changes original)
# opertaing_systems.sort()
# print(opertaing_systems)

## join elements (list -> str)
# joiend_names = ' - '.join(opertaing_systems)  ## str
#
# str -> list
# date = '2024-10-08'  ## str
# new_list = date.split('-')  ## list

## dubble numbers and save in new list
# numbers = [1, 2, 3, 4, 5]
# ## method 1:
# evens = []
# for n in numbers:
#     if n > 3:
#         new_number = n * 2
#         evens.append(new_number)
# ## method 2 (list comprehension)
# evens = [
#     n * 2
#     for n in numbers
#     if n > 3
# ]

## dictionary ------------------------------------------
'''
## define empty dictionary
student = {}

student = {
    ## key       value
    'name':      'Beniamin',
    'age':       30,
    'is_male':   True,
    'enemies':   None,
    'friends':   ['Ali', 'Iman', 'Hossein'],
    'workplace': {
        ## key       value
        'brand':     'Rahavard',
        'zip code': 634883439,
    },
}


## get value of a key
#
## method 1 (prone to throwing errors):
name    = student['name']
friends = student['friends']
brand   = student['workplace']['brand']
#
# method 2 (safe):
if 'job' in student:
    job = student['job']
#
# method 3 (safe):
job = student.get('job')  ## ---------,
job = student.get('job', None)  ## <--'
job = student.get('job', 'No Jobs Yet')


## add/replace key-value pair
##
## if key already exists, value gets updated
student['friends'] = []
##
## new key-value pair is added
student['address'] = 'Azadi Street'
##
## if key does not exist, adds it
## if key already exists, does nothing (does not replace its value to 'New Value')
student.setdefault('New Key', 'New Value')
##
## update
## if key already exists, value gets updated
car_info = {'car': 'Tiba'}
student.update(car_info)
# or
student.update(hair_color='Black')


## delete key
##
## method 1
del student['name']
##
## method 2: delete specific key-value
student.pop('age')
##
## method 3: delete last key-value pair
student.popitem()


## clear dictionary
# student = {}
# student.clear()


## copy
# teacher = student.copy()


## comprehension
# from a list
numbers = {
    i: i * 10
    for i in range(5)
}
# from a dictionary
applicants = {'Ali': 60, 'Ben': 20}
timed = {
    name: age * 10
    for name, age in applicants.items()
    if age > 30
}
'''

## tuple ------------------------------

'''
nums = (1, 2, 3)

## packing
nums = 1, 2, 3

## unpacking
num1, num2, num3 = (1, 2, 3)

## tuple with one element
num = (1,)

names = ('Ben',) * 10

## delete
del nums



people = {}
people = dict()

names = []
names = list()
## ['A', 'B', 'C', ...]

names = ()
names = tuple()
## ('A', 'B', 'C', ...)


## 1. only have unique elements
## 2. unordered
names = set()
## {'A', 'B', 'C', ...}


all_ips = [
    '1.2.3.4',
    '1.2.3.4',
    '192.168.1.2',
    '76.62.98.198',
]

unique_ips = sorted(list(set(all_ips)))
print(unique_ips)


names.add('ghghg')
'''

## function -------------------------

## 'small' is a parameter
##
def add(name, age):
    print(f'name: {name}')
    print(f'age: {age}')


# ## positional arguments
# add(10, 'Ben')

# ## keyword args
# add(age=10, name='Ben')

# optional parameter
def price_device(keyboard, mainboard=100):
    return f'{keyboard} is cheaper than {mainboard}'


def calc_age(*args):
    '''
    args is a tuple: (20, 87, 67)
    '''
    return min(args)


# print(calc_age(10, 20, 30))


def create_student(**kwargs):
    '''
    kwargs is a dict: {'name': 'Ali', 'Last Name': 'Alavi'}
    '''
    name = kwargs.get('name')
    last_name = kwargs.get('last_name')
    return f'{name} {last_name}'




result = create_student(name='Ali', last_name='Alavi')
# print(result)


## scope
'''
author = 'Glob Auth'  ## author is global

def create_book(date):  ## author is local
    author = 'Loc AUt'
    msg = f'By {author} in {date}'
    return msg


book = create_book(1900)
print(author)
'''

## filter/lambda/map/zip

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0  ## True/False


evens = filter(
    ## funtion
    is_even,

    ## lisrt
    numbers,
)

evens = filter(
    ## function
    lambda num: num % 2 == 0,

    ## list
    numbers,
)



## zip
names = ['Ben', 'Beniamin', 'Mohammad', 'Reza', 'Ali']
last_names = ['Kamali', 'Hayati', 'Alavi']
ages = [40, 87, 19]

full_names = list(zip(names, last_names, ages))





## unpacking list/set/tuple
g1 = [1, 2, 3]
g2 = [4, 5, 6]
combined = [
    *g1,
    *g2,
]  ## [1, 2, 3, 4, 5, 6]


## unpacking dict
person1 = {
    'name': 'Ali',
    'age': 10,
}
person2 = {
    'name2': 'Ben',
    'age2': 20,
}
combined = {
    **person1,
    **person2,
}


## error handling ------------------------------------------
'''
## syntax error

## logical error (Exception)

# 1
try:
    content = open('file.txt')
    age = 1 / 0

## there is an exception
except:
    print('An Error Occured')

## there is no exception
else:
    print('successful')

## no matter if there is an exception or not
finally:
    content.close()


# 2
try:
    age = 1 / 0
except Exception as exc:
    print('An Error Occured')
    print(exc)

# 3
try:
    age = 1 / 0
except ZeroDivisionError as zde_exc:
    print(zde_exc)
except ValueError as ve_exc:
    print(ve_exc)


## raise exception:
raise ValueError('Ivalid Value')

'''


## swap variables
a = 'A'
b = 'B'
a, b = (b, a)



## modules

## built-in functions (no need to be imported)
## print, str, ...

## built-in modules (no need to be installed by pip)
## os, Path, re, time, ...


'''
import os

home = os.environ['HOME']
# home = os.getenv('HOME')

directory = f'{home}/main/eterna'

## get list of files/dirs
items = os.listdir(directory)

## isfile/isdir
for item in items:
    full_path = f'{directory}/{item}'
    if os.path.isfile(full_path):
        print(f'{item} is file')
    elif os.path.isdir(full_path):
        print(f'{item} is directory')

## os info
os_info = os.uname()  ## posix.uname_result(sysname='Linux', nodename='acer', release='6.6.58-1-lts', version='#1 SMP PREEMPT_DYNAMIC Wed, 23 Oct 2024 17:28:15 +0000', machine='x86_64')
## os_info = os.name  ## on Windows

## pwd
pwd = os.getcwd()
print(pwd)

## cd
os.chdir(f'{home}/main/ariel')
'''



'''
## import methods
# 1
import os

# 2
## from os import *  <- DONT (not recommended)
from os import (
    getcwd as my_pwd,
    # listdir as get_files,
)
'''


from datetime import (
    datetime as dt,
    date,
    time,
)

now = dt.now()  ## 2024-10-30 19:24:13.846711
weekday = now.strftime('%A')  ## Wednesday
weekday = now.strftime('%a')  ## Wed
print(now)


print(date.today())
