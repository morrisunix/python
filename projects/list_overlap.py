from random import randint

def get_intersection(list_1, list_2):
    """ Returns a new list with the intersecion of both lists

    Parameters
    ----------
    list_1: list
        First given list
    listd_2: list
        Second given list

    Returns
    -------
    list
        The intersection list
    """
    intersection_list = set(list_1) & set(list_2)
    return list(intersection_list)

def random_list_generator(number_of_elements):
    """ Returns a list of random numbers

    Parameters
    ----------
    number_of_elements: int
        Size of the list

    Returns
    -------
    list
        New list with size number_of_elements and random elements
    """
    new_list = []
    for count in range(number_of_elements):
        new_list.append(randint(0, 100))

    return new_list

def main():
    """ Main function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    c = random_list_generator(10)
    d = random_list_generator(20)

    intersection_list = get_intersection(c, d)

    print("{} \n{}".format(c, d))

    print(intersection_list)


if __name__ == "__main__":
    main()
