import pandas as pd
def calculate_average_price_in_region(df, region):
    region_data = df[df['region'] == region]
    average_price = region_data['price'].mean()
    return average_price
