from data_import import *
import eval
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