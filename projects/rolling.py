from random import randint

def rolling_dice(number_of_dices):
    """ Return random integers based on the numeber of dices

    Parameters
    ----------
    number_of_dices: int
        Number of dices

    Returns
    -------
    list
        Random integers on a list
    """
    random_integers = []
    for tries in range(number_of_dices):
        random_integers.append(randint(1, 6))

    return random_integers

def main():
    """ Main function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    while True:
        # Infinit loop for roolling the dice
        print("Random dices tries: {}".format(rolling_dice(3)))
        continue_rolling = input("continue Y/N: ")
        if continue_rolling.upper() == "N":
            break


if __name__ == "__main__":
    main()
