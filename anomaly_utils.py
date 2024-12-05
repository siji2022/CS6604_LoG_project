import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import libpysal as lps
from scipy.spatial.distance import pdist, squareform
from sklearn.neighbors import KernelDensity

import matplotlib.dates as mdates

# add readable datetime format for dataframe
def add_datetime(df):
    df['dt']=pd.to_datetime(df['timestamp'], unit='s')    
    df['datetime'] = df['dt'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df

def plot_bar_anomaly_good_missing(df, col='humidity'):
    ab=df.groupby('nodeid')[f'anomaly_{col}'].sum().reset_index()
    # count the nan value by nodeid
    missing=df.groupby('nodeid')[[col]].apply(lambda x: x.isnull().sum()).reset_index()
    # count humidity value by nodeid
    collected=df.groupby('nodeid')[[col]].apply(lambda x: x.notnull().sum()).reset_index()
    # merge the missing and collected
    ab=pd.merge(ab,missing,on='nodeid')
    ab=pd.merge(ab,collected,on='nodeid')
    ab.columns=['nodeid',f'anomaly_{col}',f'missing',f'collected']
    ab['collected_not_anomaly']=ab['collected']-ab[f'anomaly_{col}']
    # remove column: collected_humidity
    ab.drop('collected',axis=1,inplace=True)
    plt.figure(figsize=(8,5))
    ab.plot(x='nodeid',kind='bar',stacked=True,figsize=(8,5),color=['red','grey','orange'])
    plt.show()
    
def plot_anomaly_by_nodeid(df, col='humidity'):
    plt.figure(figsize=(8,5))
    sns.barplot(x='nodeid', y=f'anomaly_{col}', data=df.groupby('nodeid')[f'anomaly_{col}'].sum().reset_index())
    plt.title(f'{col} anomaly count by nodeid')
    # rotate the x-axis
    plt.xticks(rotation=90)
    plt.show()