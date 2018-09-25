
def get_divisors(provided_number):
    """ Returns a list with the divisors of that provided_number

    Parameters
    ----------
    provided_number: int
        Number what we are looking for a divisor

    Returns
    -------
    list
        Contains the divisors
    """
    divisors_list = []
    list_to_compare = range(2, provided_number)
    for divisor in list_to_compare:
        if not provided_number % divisor:
            divisors_list.append(str(divisor))

    return(divisors_list)



def main():
    """ Main function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    provided_number = input("Please provide a number to test the divisors: ")
    while not provided_number.isnumeric():
        provided_number = input("Please provide a number to test the divisors: ")
    provided_number = int(provided_number)

    divisors = ", ".join(get_divisors(provided_number))

    print("The divisors of {} are {}".format(provided_number, divisors))



if __name__ == "__main__":
    main()
