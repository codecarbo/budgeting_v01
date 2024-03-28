from data_import import *
import eval
from acc_data import *
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
# no depreciated warning

# Monthly inc/exp/total for every account and all accounts
# generate list (dataframe and csv) and export/save
# columns: account, year, month, inc, exp, total

# 1. give month/year range
# 2. get inc/exp/total of every account and all for year/month
# # -> select date range function
# # add function to select according to account -> select dataframe of specific account or all
# 3. add to dataframe
# 4. next month/year; go through all and create dataframe
# 5. export dataframe to csv

dict = {
    'Konto': [],
    'Name': [],
    'Jahr': [],
    'Monat': [],
    'Einnahmen': [],
    'Ausgaben': [],
    'Überschuss': []
}

df_new = pd.DataFrame(dict)

df_all = read_data_all()

years = range(2023, 2023 - 1, -1)
months = range(12, 1 - 1, -1)

for year in years:
    # print(f'Jahr: {year}')
    for month in months:
        # print(f'Monat: {month}')
        for acc in ACC_NUMS:
            # print(f'Konto: {acc}')
            df_tmp_date = eval.select_date_range(df_all, year, month, year, month)
            df_tmp_acc = eval.select_account(df_tmp_date, [acc])
            dict_tmp = eval.get_inc_exp_total(df_tmp_acc)
            df_new.loc[len(df_new.index)] = [acc, 'name', year, month, dict_tmp['income'], dict_tmp['expenses'], dict_tmp['total']]

print(df_new)