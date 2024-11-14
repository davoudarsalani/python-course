#!/usr/bin/env python


'''
    1. create switches: Cisco, 3com, ...
    2. inverstigate market
    3. decide to buy/sell/... the switches
'''


class Robot:
    ## class attributes
    ## available for all instances
    color = 'White'

    def __init__(self, name, country):
        ## instance attributes
        self.price = 100
        self.name = name
        self.country = country
        print(f'instance {id(self)} saved')

    def walk(self):
        print(f'{self.name} is walking')

    def get_type(self):
        return type(self)


## robot is an object
## robot is an instance of Robot class
## this process is called: instantiation
robot = Robot(name='Xman', country='Canada')

## call a method
# robot.walk()

# print(isinstance(robot, Robot))

print(robot.country)

## add instance attribute
robot.weight = '20KG'
