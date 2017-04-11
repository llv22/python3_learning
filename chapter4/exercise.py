"""
Learning python3 exercise 4.13 for basic type

Reference:
Author: Orlando, Ding
"""
def main():
    """
    execrise 4.13.
    """
    # question 1
    guess_me = 7
    if guess_me < 7:
        print('too low')
    elif guess_me == 7:
        print('just right')
    else:
        print('too high')
    # question 2
    guess_me = 7
    start = 1
    while(True):
        if start < guess_me:
            print('too low')
        elif start == guess_me:
            print('found it!')
            break
        else:
            print('ooop')
            break
        start += 1
    # question 3
    for number in range(3, -1, -1):
        print(number)
    # question 4
    even_list = [x for x in range(10) if x % 2 == 0]
    print(even_list)
    # question 5
    squares = {x: x * x for x in range(10)}
    print(squares)
    # question 5
    odd = {x for x in range(10) if x % 2 == 1}
    print(odd)
    # question 6
    for thing in ('Got %s' % x for x in range(10)):
        print(thing)
    # question 7
    def good():
        return ['Harry', 'Ron', 'Hermione']
    def get_odds():
        for x in range(1, 10, 2):
            yield x
    for x, number in enumerate(get_odds(), 1):
        print(x,number)
        if x == 3:
            print(number)
            break
    # question 8
    def test(func):
        def new_function(*args, **kwargs):
            print('start')
            # wrapper function
            result = func(*args, **kwargs)
            print('end')
            return result
        return new_function
    @test
    def call_func():
        print('in call func')
    call_func()
    # question 9
    class OopsException(Exception):
        pass
    try:
        raise OopsException
    except OopsException as exc:
        print('Caught an oops')
    titles = ['Creature of Habit', 'Crewel Fate']
    plots = ['A nun turns into a monster', 'A haunted yarn shop']
    dicts = dict(zip(titles, plots))
    print(dicts)

if __name__ == '__main__':
    main()
