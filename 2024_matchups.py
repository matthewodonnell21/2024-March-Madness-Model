import pandas as pd

df = pd.read_csv('2024_tourney_seeds.csv')

team_ids = df['TeamID']
team_names = df[['TeamID', 'Name']]

team1 = []
team2 = []

for id in team_ids:
    for id2 in team_ids:
        if id != id2:
            team1.append(id)
            team2.append(id2)

matchups = pd.DataFrame({'Team X': team1, 'Team Y': team2})

matchups = pd.merge(matchups, team_names, left_on=['Team X'], right_on=['TeamID'], how='inner')
matchups = pd.merge(matchups, team_names, left_on=['Team Y'], right_on=['TeamID'], how='inner')
matchups = matchups.drop(columns = ['TeamID_x', 'TeamID_y'])

team_info = pd.read_csv('season_summaries.csv')

team_info = team_info[team_info['Season'] == 2024]

game_data = pd.merge(matchups, team_info, left_on=['Team X'], right_on=['TeamID'], how='inner')
game_data = game_data.drop(columns = ['TeamID', 'Season'])
game_data = pd.merge(game_data, team_info, left_on = ['Team Y'], right_on=['TeamID'], how='inner')
game_data = game_data.drop(columns = ['Season', 'TeamID'])


game_data.to_csv('matchup_data2024.csv', index=False)

