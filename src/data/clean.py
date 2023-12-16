import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\vivar\PycharmProjects\Russia Real Estate2021\data\external\all_v2.csv")


def clean_data(df):
    df.dropna(inplace=True)
    df['object_type'] = df['object_type'].astype(int)
    df.drop(['geo_lat', 'geo_lon'], axis=1, inplace=True)
    df['rooms'] = df['rooms'].replace('-1', 'студия')
    return df


if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\vivar\PycharmProjects\Russia Real Estate2021\data\external\all_v2.csv")
    cleaned_df = clean_data(df)
    print(cleaned_df.head())