import click
import pandas as pd


@click.command()
@click.argument('csv_path', type=click.Path(exists=True))
@click.option('--min_price', type=float, help='Minimum price filter')
@click.option('--max_price', type=float, help='Maximum price filter')
@click.option('--min_area', type=float, help='Minimum area filter')
@click.option('--max_area', type=float, help='Maximum area filter')
def filter_data(csv_path, min_price, max_price, min_area, max_area):
    df = pd.read_csv(csv_path)

    filtered_data = df.copy()

    if min_price:
        filtered_data = filtered_data[filtered_data['price'] >= min_price]
    if max_price:
        filtered_data = filtered_data[filtered_data['price'] <= max_price]
    if min_area:
        filtered_data = filtered_data[filtered_data['area'] >= min_area]
    if max_area:
        filtered_data = filtered_data[filtered_data['area'] <= max_area]

    print(f"Arguments: csv_path={csv_path}, min_price={min_price}, max_price={max_price}, min_area={min_area}, max_area={max_area}")
    print("Filtered Data:")
    print(filtered_data.head(10))

if __name__ == '__main__':
    filter_data()