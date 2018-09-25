import csv
from random import randint

def read_data(data):
    try:
        with open(data, 'r') as f:
            data = [row for row in csv.reader(f.read().splitlines())]
        return data
    except NoneType:
        print("Wrong file")

def compare_answer(random_color, answer):
    """ Compare the random color vs the given answer

    Parameters
    ----------
    random_color: str
        Random color
    answer: str
        given character

    Returns
    -------
    list
        retunrs a list of integers if found as index or False if it wasnt found the answer on the random color
    """
    indexes = []
    for index in range(len(random_color)):
        if random_color[index] == answer:
            indexes.append(index)
        if len(indexes) > 0:
            return indexes
        else:
            return False

def main():
    file_name = input("Provide file name: ")
    data = read_data(file_name)
    data_len = (len(data[0]))
    while True:
        win = 0
        random_index = randint(0, (data_len - 1))
        random_color = data[0][random_index].upper()
        tries = len(random_color)
        print("-" * tries)
        out_screen = "-" * tries
        while tries > 0:
            answer = input("Provide a letter: ").upper()
            if answer.isalpha() and answer in random_color:
                for index in range(len(random_color)):
                    if random_color[index] == answer:
                        out_screen = out_screen[:index] + answer + out_screen[index+1:]
            else:
                tries -= 1

            if out_screen.find('-') == -1:
                print("You won!")
                win = 1
                break
            print(out_screen)
        if not win:
            print("You lost!")
        continue_answer = input("Continue Y/N : ")
        if continue_answer.upper() == 'N':
            break

if __name__ == "__main__":
    main()
