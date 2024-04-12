import csv


def open_data():
    with open('filterProba.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def get_data(data=open_data()):
    message_list = []
    message = {}
    for i in range(1, len(data)):
        message[data[0][0]] = data[i][0]
        message[data[0][1]] = data[i][1]
        message[data[0][2]] = data[i][2]
        message[data[0][3]] = data[i][3]
        message[data[0][4]] = data[i][4]
        message[data[0][5]] = data[i][5]
        message[data[0][6]] = data[i][6]
        message[data[0][7]] = data[i][7]
        message['WinRate'] = get_win_rate(data, i)
        message['LossRate'] = get_loss_rate(data, i)
        message['PushRate'] = get_push_rate(data, i)
        message_list.append(message)
        message = {}
    return message_list

def get_win_rate(data, i):
    return round(int(data[i][4]) / int(data[i][7])*100, 2)

def get_loss_rate(data, i):
    if int(data[i][5]) == 0:
        return 0
    return round(int(data[i][5]) / int(data[i][7])*100, 2)

def get_push_rate(data, i):
    if int(data[i][6]) == 0:
        return 0
    return round(int(data[i][6]) / int(data[i][7])*100, 2)