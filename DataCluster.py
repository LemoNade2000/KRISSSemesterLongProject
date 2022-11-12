import numpy as np
import pandas as pd
from sklearn.cluster import OPTICS, KMeans, SpectralClustering, FeatureAgglomeration
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns

def vectorizeCSV():
    origin = os.getcwd()
    print(origin)
    filepath = "{}\\Data\\TransformedData".format(origin)
    totalDF = pd.DataFrame()
    for filename in os.listdir(filepath):
        f = os.path.join(filepath, filename)
        df = pd.read_csv(f)
        row = df['RecoveryDate']
        row.name = filename[:-4]
        # row = row.transpose()
        totalDF = totalDF.append(row)
    totalDF = totalDF.apply(lambda x: x.fillna(x.mean()),axis=0)
    return totalDF

def main():
    df = vectorizeCSV()
    print(df.shape)
    df_reduced = FeatureAgglomeration(n_clusters = 2).fit_transform(df)
    print(df_reduced.shape)
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(df_reduced)
    plt.savefig('Feature1.png')
    plt.clf()
    cluster = OPTICS(min_cluster_size=0.1).fit(df_reduced)
    labels = cluster.labels_
    label_0 = df_reduced[labels == -1]
    label_1 = df_reduced[labels == 0]
    sns.scatterplot(data = label_0, x = label_0[:, 0], y = label_0[:, 1], color = 'black')
    sns.scatterplot(data = label_1, x = label_1[:, 0], y = label_1[:, 1], color = 'red')
    plt.xlim([0, 30])
    plt.ylim([0, 30])
    plt.savefig('Scatterplot.png')
    print(cluster.labels_)
    return 0

if __name__ == "__main__":
    main()

