#!/usr/bin/env python


class Asset:
    def __init__(self):
        self.guarantee = True


class Printer:
    def __init__(self, make, model):
        self.a4_capable = True
        self.power = 220


class Scanner:
    def __init__(self, make, model):
        self.desktop = True
        self.colored = True


class Server(Asset):
    pass


printer1 = Printer(make='HP', model='1320')
scanner1 = Scanner(make='Xerox', model='M20')
server1  = Server()

print(server1.guarantee)
