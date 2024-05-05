from data_import import *
import eval
from acc_data import *
import pandas as pd
import matplotlib.pyplot as plt

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
        report_all = eval.create_acc_report(dates['min'].year, dates['max'].year)
        report_all_only = eval.select_account(report_all, [ACC_A])

        print(report_all)
        print(report_all_only)

        report_all_only.plot()
        plt.show()

    else:
        prg_run = False
