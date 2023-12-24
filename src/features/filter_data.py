
import pandas as pd

def filter_data(df, min_price=None, max_price=None, min_area=None, max_area=None):
    filtered_data = df.copy()
    if min_price:
        filtered_data = filtered_data[filtered_data['price'] >= min_price]
    if max_price:
        filtered_data = filtered_data[filtered_data['price'] <= max_price]
    if min_area:
        filtered_data = filtered_data[filtered_data['area'] >= min_area]
    if max_area:
        filtered_data = filtered_data[filtered_data['area'] <= max_area]
    return filtered_data
