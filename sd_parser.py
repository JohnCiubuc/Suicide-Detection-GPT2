import pandas as pd
import os
#premake folders and download the csv from https://www.kaggle.com/nikhileswarkomati/suicide-watch?select=Suicide_Detection.csv
data= pd.read_csv('Suicide_Detection.csv', lineterminator = '\n')
count = [0,0]
s = []
ns = []
for index, row in data.iterrows():
    if row['class'] == 'suicide':
        s.append(row['text'])
    else:
        ns.append(row['text'])
    
for i in range(0,10000):
    f = open(os.path.join('./SD_Data/'+"train"+'/suicide/' + str(i) + '.txt'), 'w')
    f.write(s[i])
    f.close()
   
for i in range(10001, 15000):
    f = open(os.path.join('./SD_Data/'+"test"+'/suicide/' + str(i) + '.txt'), 'w')
    f.write(s[i])
    f.close()
for i in range(0,10000):
    f = open(os.path.join('./SD_Data/'+"train"+'/non-suicide/' + str(i) + '.txt'), 'w')
    f.write(ns[i])
    f.close()
for i in range(10001, 15000):
    f = open(os.path.join('./SD_Data/'+"test"+'/non-suicide/' + str(i) + '.txt'), 'w')
    f.write(ns[i])
    f.close()