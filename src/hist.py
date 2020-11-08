import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

#Read data to a pandas dataframe
df = pd.read_csv('train_val_col_semNoMask.csv',encoding='utf-8')

aggregated = df.groupby(['name'])['tweet'].count().plot.bar()

plt.xticks(rotation=20, horizontalalignment="center",fontsize=7)
plt.title("Número de tweets por cada fonte")
plt.xlabel("Nome da fonte")
plt.ylabel("Número de tweets")

plt.show()
