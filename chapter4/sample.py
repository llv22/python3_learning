"""
Learning python3
"""
def document_it(func):
    '''
    '''
    def new_function(*args, **kwargs):
        '''
        '''
        print('Running functions:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

@document_it
def add_ints0(a, b):
    '''
    '''
    return a + b

def square_it(func):
    '''
    '''
    def new_function(*args, **kwargs):
        '''
        '''
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints1(a, b):
    '''
    '''
    return a + b


@square_it
@document_it
def add_ints2(a, b):
    '''
    '''
    return a + b