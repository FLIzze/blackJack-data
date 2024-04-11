import csv


def get_data():
    message_list = []
    message = {}
    with open('probabilities.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    for i in range(1, len(data)):
        message[data[0][0]] = data[i][0]
        match data[i][1]:
            case 0:
                message[data[0][1]] = 'Win'
            case 1:
                message[data[0][1]] = 'Lose'
            case _:
                message[data[0][1]] = 'Draw'
        message[data[0][2]] = data[i][2]
        message[data[0][3]] = data[i][3]
        message_list.append(message)
        message = {}
    return message_list