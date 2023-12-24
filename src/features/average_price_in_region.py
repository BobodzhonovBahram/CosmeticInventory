import click
import pandas as pd


def calculate_average_price_in_region_impl(df, region):
    region_data = df[df['region'] == region]
    region_data = region_data[region_data['price'].notna()]

    if region_data.empty:
        return None  # Возвращаем None, если нет данных для вычисления среднего значения

    region_data['price'] = region_data['price'].astype(int)
    average_price = region_data['price'].mean()
    return average_price


@click.command()
@click.argument('csv_path', type=click.Path(exists=True))
@click.argument('region', type=int)
def calculate_average_price_in_region_cli(csv_path, region):
    df = pd.read_csv(csv_path)
    result = calculate_average_price_in_region_impl(df, region)

    if result is not None:
        print(f"Average Price in Region {region}: {result}")
    else:
        print("Unable to calculate average price due to missing values.")


if __name__ == '__main__':
    calculate_average_price_in_region_cli()