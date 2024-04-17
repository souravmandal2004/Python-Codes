import time

def cache (fn):

    cache_value = {}
    print (cache_value)

    def wrapper (*args):

        if args in cache_value:
            return cache_value[args]

        result = fn (*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def long_running_function (num1, num2):
    time.sleep (4)
    return num1 + num2

print (long_running_function (2, 3))
print (long_running_function (2, 3))