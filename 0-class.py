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

    @classmethod  ## <- decorator
    def get_name(cls):
        return f'name is {cls.__name__} with id {id(cls)}'

    #################################

    ## magic method
    def __str__(self):
        return f'Name: {self.name} || Country: {self.country} || Price: {self.price}'

    ## constructor
    def __init__(self, name, country):
        ## instance attributes
        self.price = 100
        self.name = name
        self.country = country
        self.bookmarks = {}
        print(f'instance {id(self)} saved')

    def __getitem__(self, key):
        ## robot.get('python')
        ## instead of 
        ## robot.bookmarks.get('python')
        return self.bookmarks.get(key, None)

    ## instance method
    def walk(self):
        print(f'{self.name} is walking')


## robot is an object
## robot is an instance of Robot class
## this process is called: instantiation
robot = Robot(name='Xman', country='Canada')

## call instance method
# robot.walk()

# print(isinstance(robot, Robot))

## add instance attribute
robot.weight = '20KG'

## call class method
name_of_class = Robot.get_name()



robot.bookmarks['python'] = 'My Favorite'


value = robot.bookmarks.get('python')
