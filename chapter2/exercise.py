"""
Learning python3 exercise 2.4 for basic type

Reference: https://docs.python.org/3/library/stdtypes.html#string-methods
Author: Orlando, Ding
"""
def main():
    """
    execrise 2.4.
    """
    seconds_per_hour = 60 * 60
    seconds_per_day = seconds_per_hour * 24
    print(seconds_per_day / seconds_per_hour)
    # no tailed .0, as it's integer-dvision
    print(seconds_per_day // seconds_per_hour)

if __name__ == '__main__':
    main()
