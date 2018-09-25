
def is_odd(number):
    """ Validate number even or odd

    Parameters
    ----------
    number: int
        Number to be evaluated

    Returns
    -------
    bool
        Returns 1 if the provided number is odd or 0 if it's even
    """
    if number == 4:
        return(4)
    else:
        return(number % 2)

def main():
    """ Main function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    number = input("Please provide a number: ")
    while not number.isnumeric():
        number = input("Please provide a number: ")

    number = int(number)
    result = is_odd(number)
    print(result)

    if result == 1:
        print("The number is odd")
    elif result == 4:
        print("The number is even and 4!")
    else:
        print("The number is even!")


if __name__ == "__main__":
    main()
