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

    intersection_list = get_intersection(a, b)

    print("{} \n {}".format(a, b))

    print(intersection_list)


if __name__ == "__main__":
    main()
