from random import randint

def get_random_number(maximum):
    """ Generates a random number

    Parameters
    ----------
    maximum: int
        From 0 to this number where the randmon is generated

    Returns
    -------
    int
        Randon number between 0 and maximum
    """
    return(randint(0, maximum))

def check_number(input_number):
    """ Check if the imput is an actuall integer

    Parameters
    ----------
    input_number: str
        String provided, looking to be a number

    Returns
    -------
    bool
        Is or is not a number
    """
    if input_number.isnumeric():
        return True
    else:
        return False

def compare_numbers(input_number, maximum):
    """ Compare two integer numbers

    Parameters
    ----------
    input_number: int
        Input number
    maximum: int
        Max randomize number

    Retunrs
    -------
    bool
        True or False
    """
    random_number = get_random_number(maximum)
    if input_number == random_number:
        return ("Equal", random_number)
    elif input_number > random_number:
        return ("Higher", random_number)
    else:
        return ("Lower", random_number)

def main():
    """ Main function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    maximum = 10
    while True:
        number = input("Guess the number between 0 and {}: ".format(maximum))
        checked_number = check_number(number)
        if checked_number:
            result = compare_numbers(int(checked_number), maximum)
            print("Random number: {}".format(result[1]))
            if result[0] == "Equal":
                print("You Win!!!!")
            elif result[0] == "Higher":
                print("Too high!")
            else:
                print("Too Low!")
        else:
            print("This is not a number")


if __name__ == "__main__":
    main()
