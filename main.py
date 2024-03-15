import pandas as pd
import shutil
import tray

# TODO: fix stuff (see output)
# # duplicates are not dropped
# # TODO: pandas removes 0 after . somehow, entries are not identical
# # # maybe work with , numbers instead and keep separator as ; ??

# Take new input data of both accounts and concatenate
# Clean new data: delete irrelevant columns
# Add new data to existing data and remove duplicates
# Basic evaluations: get income, expenses and balance for given month

# data_s = pd.read_csv("data/Umsaetze_DE20661900000010541999_2024-02-20.csv",
#                      sep=';', on_bad_lines='warn')

# data_k = pd.read_csv("data/Umsaetze_DE15661900000010100933_2024-02-10.csv",
#                      sep=';', on_bad_lines='warn')

# data = pd.concat([data_s, data_k], axis=0, ignore_index=True)

path = input("File path: ")

data_import = pd.read_csv(path,
                          sep=';', on_bad_lines='warn')

# Only relevant cols
relevant_cols = ['IBAN Auftragskonto',
                 'Valutadatum',
                 'Name Zahlungsbeteiligter',
                 'Verwendungszweck',
                 'Betrag',
                 'Saldo nach Buchung']

# data_new = data[relevant_cols] this is only a selection!
data_new = data_import.drop(data_import.columns.difference(relevant_cols), axis=1)  # axis=1: columns
data_new['Valutadatum'] = pd.to_datetime(data_new['Valutadatum'], format='%d.%m.%Y', errors='coerce')
# # no errors for empty cells

# # Replace , with . for values
print("before")
print(data_new['Betrag'])
data_new['Betrag'] = data_new['Betrag'].str.replace(',', '.')
print("after")
print(data_new['Betrag'])
# pd.to_numeric(data_new['Betrag'], errors='coerce')
data_new['Saldo nach Buchung'] = data_new['Saldo nach Buchung'].str.replace(',', '.')
# pd.to_numeric(data_new['Saldo nach Buchung'], errors='coerce')

# Add new data to existing data
# # backup existing data
# shutil.copyfile("data/test_output/data_all.csv", "data/test_output/data_all_backup.csv")
# index_col: read first column as index column
data_all = pd.read_csv("data/test_output/data_all.csv",
                       index_col=0, parse_dates=['Valutadatum'])
data_tmp = pd.concat([data_all, data_new], axis=0, ignore_index=True)
# # axis=0 is default = combine rows of input tables
# # ignore_index=True: ignore existing index, set new index for all

data_all = data_tmp.drop_duplicates()

data_all.to_csv("data/test_output/data_all.csv")  # index=False: not writing unnamed first column

print(data_all)

# tray.print_sum(data_new)
