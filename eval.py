import pandas as pd

def get_date_info(path):

    data_all = pd.read_csv(path, index_col=0, parse_dates=['Valutadatum'])

    min_date = data_all['Valutadatum'].min()
    max_date = data_all['Valutadatum'].max()

    date_info = {
        'min': min_date,
        'max': max_date,
        'delta': max_date - min_date
    }

    return date_info