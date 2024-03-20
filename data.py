import pandas as pd

mm_games = pd.read_csv('MNCAATourneyCompactResults.csv')
mm_games = mm_games[['Season', 'WTeamID', 'LTeamID']]

team_info = pd.read_csv('season_summaries.csv')

winner_data = pd.merge(mm_games, team_info, left_on=['Season', 'WTeamID'], right_on=['Season', 'TeamID'], how='inner')
winner_data = winner_data.drop(columns = 'TeamID')
winner_data = pd.merge(winner_data, team_info, left_on = ['Season', 'LTeamID'], right_on=['Season', 'TeamID'], how='inner')
winner_data = winner_data.drop(columns = ['Season', 'WTeamID', 'LTeamID', 'TeamID'])
winner_data['Win'] = 1

loser_data = pd.merge(mm_games, team_info, left_on=['Season', 'LTeamID'], right_on=['Season', 'TeamID'], how='inner')
loser_data = loser_data.drop(columns = 'TeamID')
loser_data = pd.merge(loser_data, team_info, left_on = ['Season', 'WTeamID'], right_on=['Season', 'TeamID'], how='inner')
loser_data = loser_data.drop(columns = ['Season', 'WTeamID', 'LTeamID', 'TeamID'])
loser_data['Win'] = 0


training_data = pd.concat([winner_data, loser_data])

print(training_data)

training_data.to_csv('training_data.csv', index=False)