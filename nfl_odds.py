import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import html5lib 
from bs4 import BeautifulSoup

odds_tables = pd.read_html('https://www.vegasinsider.com/nfl/nfl-odds-week-2-2023/')
#odds_tables = pd.read_html('https://www.oddsshark.com/nfl/odds')

table = odds_tables[0]


table[['Away','Home']]= table['Matchup'].str.split("vs", expand = True)
table[['AwayPC','HomePC']] =table['Spread'].str.split(')',n=1, expand = True)
table[['AwayPts','AwayMny']] = table['AwayPC'].str.split('(', expand = True)
table[['HomePts','HomeMny']] = table['HomePC'].str.split('(', expand = True)
table['AwayMny']=table['AwayMny'].str.replace(')','',regex=False)
table['HomeMny']=table['HomeMny'].str.replace(')','',regex=False)
table[['OversTmp','UndersTmp']] =table['Total'].str.split(')',n=1, expand = True)
table[['Overs','OversMny']] = table['OversTmp'].str.split('(', expand = True)
table[['Unders','UndersMny']] = table['UndersTmp'].str.split('(', expand = True)
table['OversMny']=table['OversMny'].str.replace(')','',regex=False)
table['UndersMny']=table['UndersMny'].str.replace(')','',regex=False)
table['Overs']=table['Overs'].str.replace('o','',regex=False)
table['Unders']=table['Overs'].str.replace('u','',regex=False)
table.drop(columns=['Matchup', 'Spread','AwayPC','HomePC','Total','OversTmp','UndersTmp'],inplace=True) 
table['AwayPts'] = table['AwayPts'].apply(pd.to_numeric)
table['HomePts'] = table['HomePts'].apply(pd.to_numeric)
print(table.reindex(table['AwayPts'].abs().sort_values().index))