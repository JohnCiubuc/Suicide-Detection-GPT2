import pandas as pd
import os
#premake folders and download the csv from https://www.kaggle.com/nikhileswarkomati/suicide-watch?select=Suicide_Detection.csv
data= pd.read_csv('Suicide_Detection.csv', lineterminator = '\n')
count = [0,0]
soft_limit = 500
for index, row in data.iterrows():
    if row['class'] == 'suicide':
        count[0] = count[0] + 1
        train_test = 'train'
        if count[0] > soft_limit:
            train_test = 'test'
            
        f = open(os.path.join('./SD_Data/'+train_test+'/suicide/' + str(count[0]) + '.txt'), 'w')
        f.write(row['text'])
        f.close()
    else:
        count[1] = count[1] + 1
        train_test = 'train'
        if count[1] > soft_limit:
            train_test = 'test'
            
        f = open(os.path.join('./SD_Data/'+train_test+'/non-suicide/' + str(count[1]) + '.txt'), 'w')
        f.write(row['text'])
        f.close()
    if count[0] > (soft_limit*2) and count[1] > (soft_limit*2) :
        break