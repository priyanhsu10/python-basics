import functools


def start_end_decorator(func):

    def wrapter(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapter


@start_end_decorator
def print_name():
    print('priynahsu')


# print_name = start_end_decorator(print_name)
print_name()


@start_end_decorator
def square(a):
    return a*a


print(square(5))


def repeat(num_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kvargs):

            for x in range(num_times):
                result = func(*args, **kvargs)
            return result
        return wrapper
    return repeat_decorator


@repeat(num_times=5)
def greet(name):
    print(f'hello {name}')


greet('priyanshu')


# class decoderors

class CountCalls:
    def __init__(self, func):
        self.num_calls = 0
        self.func = func

    def __call__(self, *args, **kwds):
        self.num_calls += 1
        print(f'this is excecuted {self.num_calls} times')
        return self.func(*args, **kwds)


@CountCalls
def say_hello():
    print('hello')


say_hello()
say_hello()
