
def get_lower(number_compare, list_numbers):
    """ Provides a new list with numbers lower than number_compare

    Paramaeters
    -----------
    number_compare: int
        Numbere provided to compare
    list_numbers: list
        List of numbers provided

    Returns
    -------
    list
        New list of numbers lower than number_compare
    """
    lower_list = []
    for number in list_numbers:
        if number < number_compare:
            lower_list.append(number)

    return(lower_list)


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
    number_compare = input("Please provide a maximum number: ")
    while not number_compare.isnumeric():
        number_compare = input("Please provide a maximum number: ")
    number_compare = int(number_compare)

    print(get_lower(number_compare, a))



if __name__ == "__main__":
    main()
