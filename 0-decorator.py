#!/usr/bin/env python


from time import perf_counter


def timer(func):
    def decor():
        print('decor started...')
        start = perf_counter()  ## 53635345436
        print('running...')
        result = func()
        end = perf_counter()
        print('decor done')

        print(f'Took: {end - start}')

        return result

    return decor
    

@timer  ## <- decorator
def create_list():  ## <- decorated function
    return [i for i in range(50_000_000)]


result = create_list()

print('end of script')
