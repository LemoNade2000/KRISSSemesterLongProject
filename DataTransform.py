import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

rootdir = os.getcwd()

def doTransform(filepath, filename):
    dir = rootdir + "\\Data\\TransformedData\\" + filename
    # df = csv.reader(filepath)
    df = pd.DataFrame([[5.0, 1.0, 2.0, 4.0, 3.0], [6.0, 7.0, 2.0, 5.0, 3.0]])
    df_edit = df.copy()
    df['RecoveryDate'] = df_edit.idxmin(axis = 1)
    df_edit['min'] = df_edit.min(axis = 1)

    # Get the maximum after the minimum has been reachesd
    for index, row in df_edit.iterrows(): 
        while(row.idxmax(axis = 0) < row.idxmin(axis = 0)):
            row[row.idxmax(axis = 0)] = 0

    df['RecoveryFinishDate'] = df_edit.max(axis = 1)
    df['RecoveryMagnitude'] = 100 * (df_edit.max(axis = 1) - df_edit.min(axis = 1)) / df_edit['min'] # Percentage change from min to max
    df['RecoveryTerm'] = (df['RecoveryFinishDate'] - df['RecoveryDate']).astype(int)
    df.to_csv(dir)
    return 

if __name__ == '__main__':
    datadir = rootdir + "\\Data\\"
    for filename in os.scandir(datadir):
        if filename.is_file():
            doTransform(filename.path, filename.name)
