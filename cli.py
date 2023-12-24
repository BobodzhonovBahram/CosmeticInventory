# cli.py
import click
from src.features import my_filter_data
from src.features import average_price_in_region
import pandas as pd

@click.group()
def main():
    pass

@click.command()
@click.argument('csv_path', type=click.Path(exists=True))
@click.option('--min_price', type=float, help='Minimum price filter')
@click.option('--max_price', type=float, help='Maximum price filter')
@click.option('--min_area', type=float, help='Minimum area filter')
@click.option('--max_area', type=float, help='Maximum area filter')
def filter_data_cmd(csv_path, min_price, max_price, min_area, max_area):
    my_filter_data.filter_data(csv_path, min_price, max_price, min_area, max_area)

@click.command()
@click.argument('csv_path', type=click.Path(exists=True))
@click.argument('region', type=int)
def calculate_average_price_in_region_cmd(csv_path, region):
    result = average_price_in_region.calculate_average_price_in_region_impl(csv_path, region)

    if result is not None:
        print(f"Average Price in Region {region}: {result}")
    else:
        print("Unable to calculate average price due to missing values.")

if __name__ == '__main__':
    main.add_command(filter_data_cmd, name='filter_data_cmd')
    main.add_command(calculate_average_price_in_region_cmd, name='calculate_average_price_in_region_cmd')
    main()
