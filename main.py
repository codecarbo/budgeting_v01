from data_import import *
# import pandas as pd

path = input("File path: ")

import_info = import_banking_csv(path)
print(import_info)
