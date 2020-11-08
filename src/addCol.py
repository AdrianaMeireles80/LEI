import os
import sys
import pandas as pd
import csv

df = pd.read_csv('train_validated.csv',encoding='utf-8')

if (os.path.isfile('train_validated.csv')):
	
	df.loc[df['username'] != None,'bool'] = 1

	df.loc[df['username'] == 'realdonaldtrump','bool'] = 0
	df.loc[df['username'] == 'cmjornal','bool'] = 0
	df.loc[df['username'] == 'frasesdem3rda','bool'] = 0
	df.loc[df['username'] == 'borisjohnson','bool'] = 0

	df.loc[df.hashtags.str.match('.*#nomasks.*'),'bool'] = 2

df.to_csv('train_val_col.csv', encoding="utf8", index=False)



