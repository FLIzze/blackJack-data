import pandas as pd

df = pd.read_csv('probabilities.csv')

win_count = df[df['PlayerWin'] == 0].shape[0]
push_count = df[df['PlayerWin'] == 2].shape[0]


total_games = df.shape[0]

win_percentage = (win_count / total_games) * 100
push_pourcentage = (push_count / total_games) * 100
lose_percentage = 100.0-win_percentage-push_pourcentage

print(f'win: {win_percentage}%')
print(f'push: {push_pourcentage}%')
print(f'lose: {lose_percentage}%')
