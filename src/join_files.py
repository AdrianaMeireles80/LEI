import os
import sys
import pandas as pd
import csv

#Collect all the filenames
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.remove('join_files.py')
files.remove('addCol.py')
files.remove('graphs.py')
files.remove('hist.py')
files.remove('filterEn.py')

#Write the output
for f in files:
    open('train_validated.csv','a+', encoding="utf8").writelines([l for l in open(f, encoding="utf8").readlines()])

dataset = pd.read_csv('train_validated.csv', encoding="utf8")
text = list()
for line in dataset.values:
    #Remove duplicates
    if line[10] in text:
        dataset = dataset[dataset.tweet != line[10]]
    else:
        text.append(line[10])

dataset.to_csv('train_validated.csv', encoding="utf8", index=False)



