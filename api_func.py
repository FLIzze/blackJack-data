import csv


def get_data():
    message_list = []
    message = {}
    with open('filterProba.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    for i in range(1, len(data)):
        message[data[0][0]] = data[i][0]
        message[data[0][1]] = data[i][1]
        message[data[0][2]] = data[i][2]
        message[data[0][3]] = data[i][3]
        message[data[0][4]] = data[i][4]
        message[data[0][5]] = data[i][5]
        message[data[0][6]] = data[i][6]
        message[data[0][7]] = data[i][7]
        message_list.append(message)
        message = {}
    return message_list
