"""

argument  wielowartosciowy - *arg

"""


import  time

def function_performance (func, *arg, how_many_times = 1):
    sum = 0

    for i in range (0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end - start)

    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

def is_element_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False

print(function_performance(is_element_in, 1, setContainer, how_many_times = 500000))
print(function_performance(is_element_in, 1, listContainer, how_many_times = 500000))


"""Argumenty pozycyjne (nienazwane) muszabyc  przed argumentami nazwanymi!!!"""
