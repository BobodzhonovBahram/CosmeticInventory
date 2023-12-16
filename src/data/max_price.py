import pandas as pd
df = pd.read_csv(r"C:\Users\vivar\PycharmProjects\Russia Real Estate2021\data\external\all_v2.csv")
def максимальная_стоимость_по_региону(data):
    макс_стоимость_по_региону = data.groupby('region')['price'].max().reset_index()

    объединенные_данные = pd.merge(макс_стоимость_по_региону, data, on=['region', 'price'], how='left')

    return объединенные_данные

результат = максимальная_стоимость_по_региону(df)

print(результат)
