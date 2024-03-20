from data_import import *
import eval
# import pandas as pd

# import_path = input("File path: ")
# import_info = import_banking_csv(import_path)
# print(import_info)

date_info = eval.get_date_info(PATH_DATA_ALL)
print(date_info)


# data_all = pd.read_csv(PATH_DATA_ALL, index_col=0, parse_dates=['Valutadatum'])
