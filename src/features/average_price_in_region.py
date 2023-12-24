import click
import pandas as pd

def calculate_average_price_in_region_impl(csv_path, region):
    df = pd.read_csv(csv_path)
    region_data = df.copy()
    region_data['region'] = region_data['region'].astype(int)
    region_data = region_data[region_data['region'] == region]
    region_data = region_data[region_data['price'].notna()]

    if region_data.empty:
        return None  # Возвращаем None, если нет данных для вычисления среднего значения

    region_data['price'] = region_data['price'].astype(int)
    average_price = region_data['price'].mean()
    return average_price

if __name__ == '__main__':
    pass
