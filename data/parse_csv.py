import csv

def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

def get_min_score_difference(parsed_data):
    parsed_data.pop(0)
    goals = [x[5] for x in parsed_data]
    goals_allowed = [x[6] for x in parsed_data]
    values = [int(x) - int(y) for x, y in zip(goals, goals_allowed)]
    return values.index(min(values))

def get_team(index_value, parsed_data):
    teams = [x[0] for x in parsed_data]
    return teams[index_value]


# ---- run code ---- #

data = "football.csv"
read_data(data)
