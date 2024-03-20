import pandas as pd

df = pd.read_csv('MRegularSeasonDetailedResults.csv')

wins_df = df.rename(columns={'WTeamID': 'TeamID', 'WScore': 'Score', 'LTeamID': 'Opp_TeamID', 
                             'LScore' : 'Opp_Score', 'WLoc' : 'Loc', 'WFGM' : 'FGM', 'WFGA' : 'FGA', 
                             'WFGM3' : 'FGM3', 'WFGA3' : 'FGA3', 'WFTM' : 'FTM', 'WFTA' : 'FTA', 'WOR' : 'OR', 
                             'WDR': 'DR', 'WAst' : 'Ast', 'WTO' : 'TO', 'WStl' : 'Stl', 'WBlk' : 'Blk', 'WPF' : 'PF', 
                             'LFGM' : 'Opp_FGM', 'LFGA' : 'Opp_FGA', 'LFGM3' : 'Opp_FGM3', 'LFGA3' : 'Opp_FGA3', 
                             'LFTM' : 'Opp_FTM', 'LFTA' : 'Opp_FTA', 'LOR' : 'Opp_OR', 'LDR' : 'Opp_DR', 
                             'LAst' : 'Opp_Ast', 'LTO' : 'Opp_TO', 'LStl' : 'Opp_Stl', 'LBlk' : 'Opp_Blk', 'LPF' : 'Opp_PF'}) 
wins_df['Win'] = 1

losses_df = df.rename(columns={'LTeamID': 'TeamID', 'LScore': 'Score', 'WTeamID': 'Opp_TeamID', 
                             'WScore' : 'Opp_Score', 'WLoc' : 'Loc', 'LFGM' : 'FGM', 'LFGA' : 'FGA', 
                             'LFGM3' : 'FGM3', 'LFGA3' : 'FGA3', 'LFTM' : 'FTM', 'LFTA' : 'FTA', 'LOR' : 'OR', 
                             'LDR': 'DR', 'LAst' : 'Ast', 'LTO' : 'TO', 'LStl' : 'Stl', 'LBlk' : 'Blk', 'LPF' : 'PF', 
                             'WFGM' : 'Opp_FGM', 'WFGA' : 'Opp_FGA', 'WFGM3' : 'Opp_FGM3', 'WFGA3' : 'Opp_FGA3', 
                             'WFTM' : 'Opp_FTM', 'WFTA' : 'Opp_FTA', 'WOR' : 'Opp_OR', 'WDR' : 'Opp_DR', 
                             'WAst' : 'Opp_Ast', 'WTO' : 'Opp_TO', 'WStl' : 'Opp_Stl', 'WBlk' : 'Opp_Blk', 'WPF' : 'Opp_PF'}) 
losses_df['Win'] = 0
losses_df['Loc'] = losses_df['Loc'].replace({'H': 'A', 'A': 'H'})

reg_szn_results_df = pd.concat([wins_df, losses_df], ignore_index=True)
reg_szn_results_df['Games'] = 1

stat_agg_df = reg_szn_results_df.drop(columns = ['DayNum', 'Opp_TeamID', 'Loc', 'NumOT']).groupby(['Season', 'TeamID']).agg('sum').reset_index()

stat_agg_df['PPG'] = stat_agg_df['Score'] / stat_agg_df['Games']
stat_agg_df['OPPG'] = stat_agg_df['Opp_Score'] / stat_agg_df['Games']
stat_agg_df['FGM2'] = stat_agg_df['FGM'] - stat_agg_df['FGM3']
stat_agg_df['FGA2'] = stat_agg_df['FGA'] - stat_agg_df['FGA3']
stat_agg_df['FGP2'] = stat_agg_df['FGM2'] / stat_agg_df['FGA2']
stat_agg_df['OFGM2'] = stat_agg_df['Opp_FGM'] - stat_agg_df['Opp_FGM3']
stat_agg_df['OFGA2'] = stat_agg_df['Opp_FGA'] - stat_agg_df['Opp_FGA3']
stat_agg_df['OFGP2'] = stat_agg_df['OFGM2'] / stat_agg_df['OFGA2']
stat_agg_df['FGP3'] = stat_agg_df['FGM3'] / stat_agg_df['FGA3']
stat_agg_df['P3FGA'] = stat_agg_df['FGA3'] / stat_agg_df['FGA']
stat_agg_df['OP3FGA'] = stat_agg_df['Opp_FGA3'] / stat_agg_df['Opp_FGA']
stat_agg_df['OFGP3'] = stat_agg_df['Opp_FGM3'] / stat_agg_df['Opp_FGA3']
stat_agg_df['FTP'] = stat_agg_df['FTM'] / stat_agg_df['FTA']
stat_agg_df['FTAPG'] = stat_agg_df['FTA'] / stat_agg_df['Games']
stat_agg_df['OFTAPG'] = stat_agg_df['Opp_FTA'] / stat_agg_df['Games']
stat_agg_df['SM'] = stat_agg_df['FGA'] - stat_agg_df['FGM'] + stat_agg_df['FTA'] - stat_agg_df['FTM']
stat_agg_df['OSM'] = stat_agg_df['Opp_FGA'] - stat_agg_df['Opp_FGM'] + stat_agg_df['Opp_FTA'] - stat_agg_df['Opp_FTM']
stat_agg_df['ORR'] = stat_agg_df['OR'] / stat_agg_df['SM']
stat_agg_df['DRR'] = stat_agg_df['DR'] / stat_agg_df['OSM']
stat_agg_df['APG'] = stat_agg_df['Ast'] / stat_agg_df['Games']
stat_agg_df['TOPG'] = stat_agg_df['TO'] / stat_agg_df['Games']
stat_agg_df['TOFPG'] = stat_agg_df['Opp_TO'] / stat_agg_df['Games']
stat_agg_df['BPG'] = stat_agg_df['Blk'] / stat_agg_df['Games']

stat_agg_df = stat_agg_df[['Season', 'TeamID', 'PPG', 'FGP2', 'FGP3', 'P3FGA', 'FTP', 'FTAPG', 'ORR', 'DRR', 'APG', 'TOPG', 'BPG', 
                           'OPPG', 'OFGP2', 'OFGP3', 'OP3FGA', 'OFTAPG', 'TOFPG']]


schedule_df = reg_szn_results_df[['Season', 'TeamID', 'Opp_TeamID', 'Win', 'Loc']]
record_df = schedule_df.groupby(['Season', 'TeamID']).agg({'Win' : 'mean'}).reset_index()
record_df = record_df.rename(columns = {'Win' : 'WP'})
schedule_df = pd.merge(schedule_df, record_df, left_on=['Season', 'Opp_TeamID'], right_on=['Season', 'TeamID'], how='inner')
schedule_df = schedule_df.rename(columns = {'WP' : 'OWP', 'TeamID_x' : 'TeamID'})
schedule_df = schedule_df[['Season', 'TeamID', 'Opp_TeamID', 'Win', 'Loc', 'OWP']]
record_df = schedule_df.groupby(['Season', 'TeamID']).agg({'Win' : 'mean', 'OWP' : 'mean'}).reset_index()
record_df = record_df.rename(columns = {'Win' : 'WP'})
schedule_df = pd.merge(schedule_df, record_df, left_on=['Season', 'Opp_TeamID'], right_on=['Season', 'TeamID'], how='inner')
schedule_df = schedule_df.rename(columns = {'OWP_x' : 'OWP', 'TeamID_x' : 'TeamID', 'OWP_y' : 'OOWP'})
schedule_df = schedule_df[['Season', 'TeamID', 'Opp_TeamID', 'Win', 'Loc', 'OWP', 'OOWP']]
record_df = schedule_df.groupby(['Season', 'TeamID']).agg({'Win' : 'mean', 'OWP' : 'mean', 'OOWP' : 'mean'}).reset_index()
record_df['SOS'] = (2*record_df['OWP'] + record_df['OOWP']) / 3
record_df = pd.merge(record_df.rename(columns={'Win': 'WP'}), 
                    schedule_df[(schedule_df['Loc'] == 'N') | 
                                (schedule_df['Loc'] == 'A')].groupby(
                                    ['Season', 'TeamID']).agg({'Win' : 'mean'}).rename(
                                        columns = {'Win': 'WPAFH'}),
                                        on=['Season', 'TeamID'], how='inner')
record_df = record_df[['Season', 'TeamID', 'WP', 'SOS', 'WPAFH']]

final_df = pd.merge(stat_agg_df, record_df, on = ['Season', 'TeamID'])

reg_szn_results_df['ptdiff'] = abs(reg_szn_results_df['Score'] - reg_szn_results_df['Opp_Score'])
close_games = reg_szn_results_df[reg_szn_results_df['ptdiff'] <= 7]
close_games = close_games.groupby(['Season', 'TeamID']).agg({'Win' : 'mean'}).reset_index()
close_games = close_games.rename(columns = {'Win' : 'CGWP'})

final_df = pd.merge(final_df, close_games, on = ['Season', 'TeamID'])

print(final_df)

final_df.to_csv('season_summaries.csv', index=False)