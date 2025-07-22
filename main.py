# class Fibonacci:
#     def __init__(self):
#         self.cache = {}
#
#     def __call__(self, n):
#         if n not in self.cache:
#             if n == 0:
#                 self.cache[0] = 0
#             elif n == 1:
#                 self.cache[1] = 1
#             else:
#                 self.cache[n] = self(n-1) + self(n-2)
#         return self.cache[n]
#
#
# fib = Fibonacci()
#
# for i in range(5):
#     print(fib(i))
#
# print(fib.cache)
#
#
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def __call__(self):
# #         return "hi"
# #
# #
# # p = Person("John", 18)
# # print(p())
from functools import wraps


def func_logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        log_string = function.__name__ + " was called"
        with open("out.log", 'a') as opened_file:
            opened_file.write(log_string + '\n')
    return wrapper


# class func_logger:
#
#     _logfile = 'out.log'
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         log_string = self.func.__name__ + " was called"
#         with open(self._logfile, 'a') as opened_file:
#             opened_file.write(log_string + '\n')
#         return self.func(*args, **kwargs)


@func_logger
def say_hi(name):
    print(f"Hi, {name}")

@func_logger
def say_bye(name):
    print(f"Bye, {name}")


say_hi("Peter")
say_bye("Peter")

