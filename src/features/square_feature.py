import pandas as pd
df = pd.read_csv(r"C:\Users\vivar\PycharmProjects\Russia Real Estate2021\data\external\all_v2.csv")
def добавить_фичу_отношение_площади(data):
    data['отношение_площадей'] = data['kitchen_area'] / data['area']

    return data


df = добавить_фичу_отношение_площади(df)# Вызов функции с вашим набором данных


print(df.head())