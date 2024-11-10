import pandas as pd

def calculateStats(df, column):
    statsdf = pd.DataFrame()
    statsdf['Pollutant'] = [column]
    statsdf['Mean'] = df[column].mean()
    statsdf['Median'] = df[column].median()
    statsdf['Standard Deviation'] = df[column].std()
    statsdf['Minimum'] = df[column].min()
    statsdf['Maximum'] = df[column].max()
    statsdf['25th Percentile'] = df[column].quantile(0.25)
    statsdf['75th Percentile'] = df[column].quantile(0.75)
    statsdf = statsdf.pivot_table(index='Pollutant').T
    return statsdf