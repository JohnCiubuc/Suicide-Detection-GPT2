import pandas as pd
import os
#premake folders and download the csv from https://www.kaggle.com/nikhileswarkomati/suicide-watch?select=Suicide_Detection.csv
# this can definitely be improved beyond a doubt. Just a quick dirty parser to make files for gpt-2 training
data= pd.read_csv('Suicide_Detection.csv', lineterminator = '\n')
s = []
ns = []
train_count=10000
test_count=5000
for index, row in data.iterrows():
    if row['class'] == 'suicide':
        s.append(row['text'])
    else:
        ns.append(row['text'])
    
for i in range(0,train_count):
    f = open(os.path.join('./SD_Data/'+"train"+'/suicide/' + str(i) + '.txt'), 'w')
    f.write(s[i])
    f.close()
   
for i in range(train_count+1, train_count+test_count+1):
    f = open(os.path.join('./SD_Data/'+"test"+'/suicide/' + str(i) + '.txt'), 'w')
    f.write(s[i])
    f.close()

for i in range(0,train_count):
    f = open(os.path.join('./SD_Data/'+"train"+'/non-suicide/' + str(i) + '.txt'), 'w')
    f.write(ns[i])
    f.close()

for i in range(train_count+1, train_count+test_count+1):
    f = open(os.path.join('./SD_Data/'+"test"+'/non-suicide/' + str(i) + '.txt'), 'w')
    f.write(ns[i])
    f.close()
