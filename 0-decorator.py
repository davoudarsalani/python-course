#!/usr/bin/env python


from time import perf_counter


def timer(func):  ## fund is actually create_list
    def decor(num):

        start = perf_counter()  ## 53635345436
        print('running...')
        result = func(num)  ## <<<<<<<<<<<<<<
        end = perf_counter()
        print('decor done')

        print(f'Took: {end - start}')

        return result

    return decor


@timer  ## <- decorator
def create_list(num):  ## <- decorated function
    return [i for i in range(num)]


result = create_list(num=100_000)
