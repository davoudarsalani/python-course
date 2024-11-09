#!/usr/bin/env python


'''
    1. create switches: Cisco, 3com, ...
    2. inverstigate market
    3. decide to buy/sell/... the switches
'''


class Robot:
    ## function inside a class is a 'method'
    def walk(self):
        print(f'robot {id(self)} is walking')

    def get_type(self):
        return type(self)


## robot is an object
## robot is an instance of Robot class
## this process is called: instantiation
robot = Robot()


## call a method
robot.walk()

print(robot.get_type())
