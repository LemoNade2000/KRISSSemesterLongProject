import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

rootdir = os.getcwd()

def doTransform(filepath, filename):
    dir = rootdir + "\\Data\\TransformedData\\" + filename
    df = pd.read_csv(filepath)
    df = df.set_index('Unnamed: 0')
    df= df.rename_axis(None, axis=1).rename_axis('id', axis=0)
    df = df.apply(pd.to_numeric, errors = 'coerce')
    df = df.dropna(axis = 0, how = 'any')
    df_edit = df.copy()
    df['RecoveryDate'] = df_edit.idxmin(axis = 1).astype(int)
    df_edit['min'] = df_edit.min(axis = 1)
    loopNumber = 0
    # Get the maximum after the minimum has been reachesd
    for index, row in df_edit.iterrows(): 
        max = int(row.idxmax())
        min = int(row.idxmin())
        while(max < min):
            row[row.idxmax()] = 0
            max = int(row.idxmax())
        df_edit.iloc[loopNumber] = row
        loopNumber += 1

    df['RecoveryFDate'] = df_edit.idxmax(axis = 1).astype(int)
    df['RecoveryMagnitude'] = 100 * (df_edit.max(axis = 1) - df_edit['min']) / df_edit['min'] # Percentage change from min to max
    df['RecoveryTerm'] = (df['RecoveryFDate'] - df['RecoveryDate']).astype(int)
    df.to_csv(dir)
    return 

if __name__ == '__main__':
    datadir = rootdir + "\\Data\\"
    fileNum = 0
    for filename in os.scandir(datadir):
        print(fileNum)
        if filename.is_file():
            try:
                doTransform(filename.path, filename.name)
            except:
                continue
        fileNum += 1
