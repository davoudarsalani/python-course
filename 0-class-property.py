#!/usr/bin/env python


class MovieRating:
    def __init__(self, rtng):
        self.rating = rtng

    @property
    def rating(self):
        return self.__rating    

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError('No Zero Rating Allowed')
        self.__rating = value


inst = MovieRating(5)
print(inst.rating)

inst.rating = 1
print(inst.rating)
