
def bynarySearch(search_array, target):
    """ Returns if the nimber has been found on the array using a binary search

    Parameters
    ----------
    search_array: array
        The array where we are looking at
    target: int
        The numebr you are searching

    Returns
    -------
    int
        Index of the array where the value was found
    """

    min=0
    max=len(search_array)
    while True:
        guess = (min+max)//2
        if search_array[guess] == target:
            return guess
        elif search_array[guess] > target:
            max=guess-1
        else:
            min=guess+1


def main():
    """ Main function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    array=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    target=67
    index=bynarySearch(array, target)
    print("The value is: {}".format(index))

if __name__ == "__main__":
    main()
