import pandas as pd
from datetime import date
from data_import import *
from acc_data import *


def get_date_info(df):
    '''
    Get min/max date and delta of dataframe.
    '''
    min_date = df['Valutadatum'].min()
    max_date = df['Valutadatum'].max()

    date_info = {
        'min': min_date,
        'max': max_date,
        'delta': max_date - min_date
    }

    return date_info


def select_date_range(df, start_year, start_month, end_year, end_month):
    '''
    Returns dataframe within given start and end date from data_all.csv.
    Set start and end dates identical to get data of given month
    '''
    # Convert input years and months to dates
    # # needs to be converted to datetime for comparison to work
    start_date = pd.to_datetime(date(start_year, start_month, 1))
    # For one month, enter same month and year as start and end; adjust end dates to next month
    if start_month == 12 & end_month == 12:
        end_month = 1
        end_year = end_year + 1

    end_date = pd.to_datetime(date(end_year, end_month + 1, 1))
    
    # Create binary mask for target date range; apply mask to data
    mask = (df['Valutadatum'] >= start_date) & (df['Valutadatum'] < end_date)
    df_masked = df.loc[mask]

    return df_masked


def select_account(df, acc_name=[]):
    # better to give account list...
    if acc_name == ACC_S:
        pass
    elif acc_name == ACC_K:
        pass
    elif acc_name == ACC_H:
        pass
    else:
        # all accounts
        pass


def get_inc_exp_total(df):
    '''
    Simple income, expenses, total evaluation for given dataframe.
    Returns dict with values.
    Dataframe needs 'Betrag' column.
    '''
    # Convert Betrag values from string to float
    df['Betrag'] = df['Betrag'].str.replace(',', '.')
    df['Betrag'] = pd.to_numeric(df['Betrag'])

    # Locate data of criteria (larger/smaller 0) and sum 'Betrag' column
    income = df.loc[df['Betrag'] > 0, 'Betrag'].sum()
    expenses = df.loc[df['Betrag'] < 0, 'Betrag'].sum()
    total = income + expenses

    dict_ret = {
        'income': income,
        'expenses': expenses,
        'total': total
    }

    return dict_ret
