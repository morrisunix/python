
def is_palindrome(provided_word):
    """ Returns True or False if the provided word is a palindrome

    Parameters
    ----------
    provided_word: str
        Provided word to evaluate

    Returns
    -------
    bool
        Returns True or false if is or is not a palindrome
    """
    reverse_palindrome = ''.join(list(provided_word)[::-1])
    print(reverse_palindrome)
    if provided_word == reverse_palindrome:
        palindrome = True
    else:
        palindrome = False

    return palindrome


def main():
    """ Main function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    provided_word = input("Plese provide a word to evaluete: ")
    while not provided_word.isalpha():
        provided_word = input("Plese provide a word to evaluete: ")
    else:
        if is_palindrome(provided_word):
            print("The provided word '{}' is a palindrome :)".format(provided_word))
        else:
            print("The provided word '{}' is not a palindrome :(".format(provided_word))


if __name__ == "__main__":
    main()
