"""
Learning python3 exercise 3.8 for basic type

Reference:
1. range() - https://docs.python.org/3/library/stdtypes.html?highlight=range#range
2. format() string - https://pyformat.info/
3, map() with lambda - http://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
Author: Orlando, Ding
"""
def main():
    """
    execrise 3.8.
    """
    years_list = list(range(1981, 1981+6, 1))
    print("the year of 3 year old is: {:d}".format(years_list[3]))
    print("the year of elder in year_list is: {:d}".format(years_list[-1]))
    things = ["mozzarella", "cinderella", "salmonella"]
    capitial_things = list(map(lambda x: x.capitalize(), things))
    capitial_things = [x.capitalize() for x in capitial_things]

if __name__ == '__main__':
    main()
