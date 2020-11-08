import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

#Read data to a pandas dataframe
dataset = pd.read_csv('train_validated.csv',encoding='utf-8')


#Convert timestamp to datetime
dataset['DateTime'] = [datetime.fromtimestamp(int(d/1000)) for d in dataset['created_at']]
dataset['Time'] = [d.time().strftime("%H:%M") for d in dataset['DateTime']]
dataset['Date'] = [d.date().strftime("%Y-%m") for d in dataset['DateTime']]


#Create a dataframe with aggregation
aggregated = dataset.groupby(['Date']).count().reset_index()

aggregated['Date'] = pd.to_datetime(aggregated['Date'])

aggregated = aggregated.loc[aggregated['Date'] > datetime.strptime('2019-09',"%Y-%m")]

#Generate plot
fig, ax = plt.subplots(figsize=(20,12))
ax.plot(aggregated['Date'], aggregated['Time'], color='black', label='Confirmed')

plt.legend()

ax.set(xlabel='Meses', ylabel='Número de tweets',
       title='Contabilização de tweets por Meses')
plt.show()

