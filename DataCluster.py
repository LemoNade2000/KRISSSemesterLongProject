import numpy as np
import pandas as pd
from sklearn.cluster import OPTICS, KMeans, SpectralClustering, FeatureAgglomeration
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns

def vectorizeCSV():
    origin = os.getcwd()
    filepath = "{}\\Data\\TransformedData".format(origin)
    totalDF = pd.DataFrame()
    termDF = pd.DataFrame()
    for filename in os.listdir(filepath):
        f = os.path.join(filepath, filename)
        df = pd.read_csv(f)
        row = df['RecoveryDate']
        termRow = df['RecoveryTerm']
        row.name = filename[:-4]
        termRow.name = filename[:-4]
        # row = row.transpose()
        totalDF = totalDF.append(row)
        termDF = termDF.append(termRow)
    totalDF = totalDF.apply(lambda x: x.fillna(x.median()),axis=0)
    termDF = termDF.apply(lambda x: x.fillna(x.median()),axis=0)
    return totalDF, termDF

def cluster(start):
    df, termDF = vectorizeCSV()
    df = df.drop(columns = np.arange(start, 34), axis = 1)
    termDF = termDF.drop(columns = np.arange(start, 34), axis = 1)
    df_reduced = FeatureAgglomeration(n_clusters=2)
    df_reduced.fit_transform(df)
    featureLabel = df_reduced.labels_
    # print(df_reduced.labels_)
    plot_df = df_reduced.transform(df)
    df_reduced = df_reduced.transform(df)
    df_reduced = pd.DataFrame(df_reduced)
    df_reduced.index = df.index
    # print(df_reduced)
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(plot_df)
    plt.savefig('Feature1.png')
    plt.clf()
    cluster = OPTICS(min_cluster_size=0.1).fit(df_reduced)
    labels = cluster.labels_
    label_0 = df_reduced[labels == -1]
    label_1 = df_reduced[labels == 0]
    label_2 = df_reduced[labels == 1]
    df_reduced['MeanRecoveryTerm'] = termDF.loc[:,featureLabel == 0].mean(axis = 1)
    df_reduced['AltMeanRecoveryTerm'] = termDF.loc[:,featureLabel == 1].mean(axis = 1)
    df_reduced['Cluster'] = labels
    df_reduced.to_csv("TermInformation.csv")
    sns.scatterplot(data = label_0, x = label_0[0], y = label_0[1], color = 'black')
    sns.scatterplot(data = label_1, x = label_1[0], y = label_1[1], color = 'red')
    try :
        sns.scatterplot(data = label_2, x = label_2[0], y = label_2[1], color = 'blue')
    except :
        print("No third clustrer")
    plt.xlim([0, 30])
    plt.ylim([0, 30])
    plt.savefig('Scatterplot.png')
    # print(df.index[labels == 0])
    # print(df.index[labels == 1])
    return df.index[labels == 0]

def retroactive():
    df, termDF = vectorizeCSV()
    df_reduced = FeatureAgglomeration(n_clusters=2)
    df_reduced.fit_transform(df)
    featureLabel = df_reduced.labels_
    # print(df_reduced.labels_)
    plot_df = df_reduced.transform(df)
    df_reduced = df_reduced.transform(df)
    df_reduced = pd.DataFrame(df_reduced)
    df_reduced.index = df.index
    # print(df_reduced)
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(plot_df)
    plt.savefig('Feature1Retro.png')
    plt.clf()
    cluster = OPTICS(min_cluster_size=0.1).fit(df_reduced)
    labels = cluster.labels_
    label_0 = df_reduced[labels == -1]
    label_1 = df_reduced[labels == 0]
    label_2 = df_reduced[labels == 1]
    df_reduced['MeanRecoveryTerm'] = termDF.loc[:,featureLabel == 0].mean(axis = 1)
    df_reduced['AltMeanRecoveryTerm'] = termDF.loc[:,featureLabel == 1].mean(axis = 1)
    df_reduced['Cluster'] = labels
    df_reduced.to_csv("TermInformationRetroactive.csv")
    sns.scatterplot(data = label_0, x = label_0[0], y = label_0[1], color = 'black')
    sns.scatterplot(data = label_1, x = label_1[0], y = label_1[1], color = 'red')
    try :
        sns.scatterplot(data = label_2, x = label_2[0], y = label_2[1], color = 'blue')
    except :
        print("No third clustrer")
    plt.xlim([0, 30])
    plt.ylim([0, 30])
    plt.savefig('ScatterplotRetroactive.png')
    # print(df.index[labels == 0])
    # print(df.index[labels == 1])
    return df.index[labels == 0]

# main()
# retroactive()

