#!/usr/bin/env python


class Asset:
    def __init__(self):
        print('Asset init running')
        self.guarantee = True


# class Printer:
#     def __init__(self, make, model):
#         self.a4_capable = True
#         self.power = 220


class Server(Asset):
    ## overrides parent's method
    def __init__(self):
        print('Server init running')
        self.weight = 5

        super().__init__()


# printer1 = Printer(make='HP', model='1320')
server1  = Server()

print(server1.weight)
print(server1.guarantee)


# print(isinstance(server1, Server))
# print(isinstance(server1, Asset))
# print(isinstance(Asset, object))
# print(issubclass(Server, Asset))
# print(issubclass(Server, object))
