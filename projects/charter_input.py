from datetime import datetime

def age_calculate(age):
    """ Calculate the year when the age will turn 100 years old

    Parameters
    ----------
    age: int
        Current age

    Returns
    -------
    string
        The year when the age holder will turn 100 years old
    """
    current_year = datetime.now().year
    remaining_years_to_100 = 100 - age
    year_when_turn_100 = current_year + remaining_years_to_100
    return year_when_turn_100


def main():
    """ Main function

    Parameters
    ---------
    None

    Returns
    -------
    None
    """
    while True:
        name = input("Please provide your name: ")
        age = input("Please provide your current age: ")
        while not age.isnumeric():
            print("That is not a valid integer number")
            age = input("Please provide your current age: ")
        loops = input("How many times you want to get the response printed: ")
        while not loops.isnumeric():
            print("That is not a valid integer number")
            loops = input("How many times you want to get the response printed: ")
        loops = int(loops)
        year_when_turn_100 = age_calculate(int(age))
        printed_output = "Hello {} you will turn 100 in {}! \n".format(name, year_when_turn_100)
        printed_output *= loops
        print(printed_output)
        continue_loop = input("Try again Y/N?").upper()
        if continue_loop == 'N':
            break

if __name__ == "__main__":
    main()
