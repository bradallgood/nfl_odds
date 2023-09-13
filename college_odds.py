import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import html5lib 
from bs4 import BeautifulSoup

odds_tables = pd.read_html('https://www.vegasinsider.com/college-football/odds/las-vegas/')

table = odds_tables[0]

i = 0
home_team = ''
home_spread = ''
away_team = ''
away_spread = ''
sep = 0 
odds_table = pd.DataFrame()

for index, row in table.iterrows():
    if i < 400:
        if  type(row['Time']) != float:
            if row['Time'] == "Matchup Movements Consensus Picks" or row['Time'] == "Consensus Picks":
                if bad_value == 0:
                    new_data = pd.DataFrame({'away_team': [away_team], 'away_spread': [away_spread], 
                                             'away_spread_money': [away_spread_money], 'home_team': [home_team], 
                                             'home_spread': [home_spread], 'home_spread_money': [home_spread_money],})
                    odds_table = pd.concat([new_data,odds_table],ignore_index=True)
                sep = 0
            else:
                if str(row['Bet365']) != 'nan' and str(str(row['Bet365']))[0] not in ['o','u','P']:
                    bad_value = 0
                    if sep == 0:
                        away_team = row['Time']
                        away_team = str(away_team).split(' ')
                        away_team = away_team[1:]
                        away_team = ' '.join(away_team)
    
                        away_spread = row['Bet365']
                        away_spread = str(away_spread).split(' ')
                        if len(away_spread) > 1:
                            away_spread_money = float(away_spread[1])
                        else:
                            aways_spread_money = 0
                        away_spread = float(away_spread[0])
                        sep = 1
                    else:
                        home_team = row['Time']
                        home_team = str(home_team).split(' ')
                        home_team = home_team[1:]
                        home_team = ' '.join(home_team)
    
                        home_spread = row['Bet365']
                        home_spread = str(home_spread).split(' ')
                        if len(home_spread) > 1:
                            home_spread_money = float(home_spread[1])
                        else:
                            home_spread_money = 0    
                        home_spread = float(home_spread[0].replace('+',''))
                else:
                    bad_value = 1
    i += 1

print(odds_table.reindex(odds_table['away_spread'].abs().sort_values().index))

fig, axs = plt.subplots(1,2,sharey=True, tight_layout=True)
axs[0].hist(odds_table['away_spread'].abs(),bins=20 )
plt.show()  