import time

# some_var = 0

def some_func(some_var_param):

    in_some_func = some_var_param + 2
    print('some_var is ... {}'.format(some_var_param))
    return in_some_func

some_var = 0

while True:

    new_var = some_func(some_var)
    some_var = new_var
    time.sleep(1)





