import csv
import pandas as pd


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

def get_total_games():
    data = open_data()
    total_games = 0
    for i in range(1, len(data)):
        total_games += int(data[i][7])
    return total_games

def get_total_wins():
    data = open_data()
    total_wins = 0
    for i in range(1, len(data)):
        total_wins += int(data[i][4])
    return total_wins

def get_total_losses():
    data = open_data()
    total_losses = 0
    for i in range(1, len(data)):
        total_losses += int(data[i][5])
    return total_losses

def get_total_pushes():
    data = open_data()
    total_pushes = 0
    for i in range(1, len(data)):
        total_pushes += int(data[i][6])
    return total_pushes

def get_total_win_rate():
    return round(get_total_wins() / get_total_games()*100, 2)

def get_total_loss_rate():
    return round(get_total_losses() / get_total_games()*100, 2)

def get_total_push_rate():
    return round(get_total_pushes() / get_total_games()*100, 2)

def get_total_games_win_loss_push():
    return {
        'total_games': get_total_games(),
        'total_wins': get_total_wins(),
        'total_losses': get_total_losses(),
        'total_pushes': get_total_pushes(),
        'total_win_rate': get_total_win_rate(),
        'total_loss_rate': get_total_loss_rate(),
        'total_push_rate': get_total_push_rate()}

def get_best_choice():
    with open('winning_rows.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    best_choice = {}
    best_choice_list = []
    for i in range(1, len(data)):
        best_choice[data[0][0]]= data[i][0]
        best_choice[data[0][1]]= data[i][1]
        best_choice[data[0][2]]= data[i][2]
        best_choice[data[0][3]]= data[i][3]
        best_choice_list.append(best_choice)
        best_choice = {}
    return best_choice_list

def get_hand_stats(hand:list)->list:
    data = pd.read_csv('filterProba.csv')
    hand_stats = data.loc[(data['PlayerCard1'] == hand[0]) & (data['PlayerCard2'] == hand[1]) & (data['DealerHand'] == hand[2])]
    stats = {}
    for kk in hand_stats.values.tolist():
        stats[kk[3]] = {
            'Win': round(kk[4]/kk[7]*100, 2),
            'Loss': round(kk[5]/kk[7]*100, 2),
            'Push': round(kk[6]/kk[7]*100, 2),
        }
    print(stats)
    return stats