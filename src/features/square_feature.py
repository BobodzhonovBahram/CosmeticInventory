import pandas as pd
def area_ratio(data):
    data['area_ratio'] = data['kitchen_area'] / data['area']

    return data


df = area_ratio(df)# Вызов функции с вашим набором данных
