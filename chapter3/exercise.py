# pylint: disable=line-too-long
"""
Learning python3 exercise 3.8 for basic type

Reference:
1. range() - https://docs.python.org/3/library/stdtypes.html?highlight=range#range
2. format() string - https://pyformat.info/
3, map() & lambda - http://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
Author: Orlando, Ding
"""
def main():
    """
    execrise 3.8.
    """
    # question 1
    years_list = list(range(1981, 1981+6, 1))
    # question 2
    print("the year of 3 year old is: {:d}".format(years_list[3]))
    # question 3
    print("the year of elder in year_list is: {:d}".format(years_list[-1]))
    # question 4
    things = ["mozzarella", "cinderella", "salmonella"]
    # question 5
    capitial_name_things = list(map(lambda x: x.capitalize() if x == "cinderella" else x, things))
    print(capitial_name_things)
    capitial_name_things = [x.capitalize() if x == "cinderella" else x for x in things]
    print(capitial_name_things)
    # question 6
    upper_food_things = list(map(lambda x: x.upper() if x == "mozzarella" else x, things))
    print(upper_food_things)
    upper_food_things = [x.upper() if x == "mozzarella" else x for x in things]
    print(upper_food_things)
    # question 7
    # or del things[-1] or del things[2]
    print(things.remove("salmonella"))
    # question 8
    surpise = ["Groucho", "Chico", "Harpo"]
    # quesiton 9, see page 29-31 for string splitting with index
    surpise[-1] = surpise[-1][-1::-1].lower().capitalize()
    print(surpise)
    # question 10
    e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
    # question 11
    print(e2f['walrus'])
    # question 12
    f2e = {}
    for english, franch in e2f.items():
        f2e[english] = franch
    print(f2e)
    # question 13
    print(f2e['chien'])
    # question 14
    print(e2f.keys())

if __name__ == '__main__':
    main()
