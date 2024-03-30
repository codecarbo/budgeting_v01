from data_import import *
import eval
from acc_data import *
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
# no depreciated warning

prg_run = True

while prg_run:

    user_input = input('import/eval/exit: ')

    if user_input == 'import':
        path = input('File path: ')
        import_info = import_banking_csv(path)
        print(import_info)

    elif user_input == 'eval':
        df_all = read_data_all()
        dates = eval.get_date_info(df_all)
        # print(dates['min'].year)
        report = eval.create_acc_report(dates['min'].year, dates['max'].year)
        print(report)

    else:
        prg_run = False
