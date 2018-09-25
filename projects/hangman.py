import csv
from random import randint

def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

def main():
    file_name = input("Provide file name: ")
    data = read_data(file_name)
    data_len = (len(data[0]))
    while True:
        random_index = randint(0, (data_len - 1))
        print(data[0][random_index])
        continue_answer = input("Continue Y/N : ")
        if continue_answer.upper() == 'N':
            break

if __name__ == "__main__":
    main()
