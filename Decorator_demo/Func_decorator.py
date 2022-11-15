# @trace
# def square(x):
#     return x*x


enable_tracing = True
# enable_tracing = False
if enable_tracing:
    debug_log = open('debug.log', 'w')


def trace(func):
    if enable_tracing:
        def callf(*args, **kwargs):
            debug_log.write('Calling {}: {}, {}'.format(func.__name__, args, kwargs))
            r = func(*args, **kwargs)
            debug_log.write('\n{} returned {}\n'.format(func.__name__, r))
            return r
        return callf
    else:
        return func


@trace
def square(x):
    return x*x


# some_number = square(10)
print(square(10))

