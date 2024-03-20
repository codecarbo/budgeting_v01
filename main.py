from data_import import *
import eval
from datetime import date
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# import_path = input("File path: ")
# import_info = import_banking_csv(import_path)
# print(import_info)

# date_info = eval.get_date_info(PATH_DATA_ALL)
# print(date_info)


data_all = pd.read_csv(PATH_DATA_ALL, index_col=0, parse_dates=['Valutadatum'])

# Get data within date range
#
start_year = 2024
start_month = 1
end_year = 2024
end_month = 3

start_date = pd.to_datetime(date(start_year, start_month, 1))

if start_month == 12 & end_month == 12:
    end_month = 1
    end_year = end_year + 1

end_date = pd.to_datetime(date(end_year, end_month + 1, 1))
# # needs to be converted to datetime for comparison to work

mask = (data_all['Valutadatum'] >= start_date) & (data_all['Valutadatum'] < end_date)
data_masked = data_all.loc[mask]

# Convert values to float
data_masked['Betrag'] = data_masked['Betrag'].str.replace(',', '.')
data_masked['Betrag'] = pd.to_numeric(data_masked['Betrag'])

income = data_masked.loc[data_masked['Betrag'] > 0, 'Betrag'].sum()
expenses = data_masked.loc[data_masked['Betrag'] < 0, 'Betrag'].sum()
total = income + expenses

print(f"Income: {income}")
print(f"Expenses: {expenses}")
print(f"Total: {total}")