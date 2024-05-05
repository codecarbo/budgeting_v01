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
    if start_month == 12 and end_month == 12:
        # if december, go to next year
        end_month = 1
        end_year = end_year + 1
    else:
        # add 1 to end month, because end month is excluded
        end_month = end_month + 1

    end_date = pd.to_datetime(date(end_year, end_month, 1))
    
    # Create binary mask for target date range; apply mask to data
    mask = (df['Valutadatum'] >= start_date) & (df['Valutadatum'] < end_date)
    df_masked = df.loc[mask]

    return df_masked


def select_account(df, acc_names=[]):
    '''
    Returns dataframe with selected accounts
    '''
    # return df.loc[df['IBAN Auftragskonto'] == acc_names]
    return df.loc[df['IBAN Auftragskonto'].isin(acc_names)]
    # how to set index new?


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


def create_acc_report(start_year, end_year):
    '''
    Creates dataframe from data_all.csv with inc/exp/tot for every account monthly
    '''
    dict = {
        'IBAN Auftragskonto': [],
        'Name': [],
        'Jahr': [],
        'Monat': [],
        'Einnahmen': [],
        'Ausgaben': [],
        'Überschuss': []
    }

    df_new = pd.DataFrame(dict)

    df_all = read_data_all()

    years = range(end_year, start_year - 1, -1)
    months = range(12, 1 - 1, -1)

    for year in years:
        # print(f'Jahr: {year}')
        for month in months:
            # print(f'Monat: {month}')
            df_tmp_date = select_date_range(df_all, year, month, year, month)
            # Skip empty months
            if df_tmp_date.empty:
                continue
            for acc in ACC_DATA:
                # print(f'Konto: {acc}')
                df_tmp_acc = select_account(df_tmp_date, [acc[0]])
                dict_tmp = get_inc_exp_total(df_tmp_acc)
                df_new.loc[len(df_new.index)] = [acc[0], acc[1], year, month, dict_tmp['income'], dict_tmp['expenses'], dict_tmp['total']]
            # For all accounts
            dict_tmp = get_inc_exp_total(df_tmp_date)
            # if month == 12 and year == 2023:
            #     print(f'Jahr: {year}, Monat: {month}')
            #     print(df_tmp_date)
            df_new.loc[len(df_new.index)] = [ACC_DATA_ALL[3][0], ACC_DATA_ALL[3][1], 
                                             year, month, dict_tmp['income'], dict_tmp['expenses'], dict_tmp['total']]

    return df_new