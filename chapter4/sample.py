"""
Learning python3
"""
def document_it(func):
    '''
    decractor for func, only print doc of func.
    '''
    def new_function(*args, **kwargs):
        '''
        internal function for wrappering of func and print out function parameter and result.
        '''
        print('Running functions:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

@document_it
def add_ints0(add_a, add_b):
    '''
    add with decrator of @document_it.
    '''
    return add_a + add_b

def square_it(func):
    '''
    decractor for func, return square of func returned value.
    '''
    def new_function(*args, **kwargs):
        '''
        internal function for wrappering of func and return square of func as result.
        '''
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints1(add_a, add_b):
    '''
    add with decrator of @square_it @document_it in order.
    '''
    return add_a + add_b


@square_it
@document_it
def add_ints2(add_a, add_b):
    '''
    add with decrator of @document_it @square_it in order.
    '''
    return add_a + add_b
    