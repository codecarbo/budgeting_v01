import pandas as pd


RELEVANT_COLS = ['IBAN Auftragskonto',
                 'Valutadatum',
                 'Name Zahlungsbeteiligter',
                 'Verwendungszweck',
                 'Betrag',
                 'Saldo nach Buchung']

PATH_DATA_ALL = 'data/output/data_all.csv'


def import_banking_csv(path):
    '''
    Import csv file from online banking, cleanup, remove duplicates and add to data_all.csv
    '''
    data_import = pd.read_csv(path, sep=';', on_bad_lines='warn')
    
    # Drop irrelevant columns
    # # data_new = data_import[relevant_cols] is only a selection!
    data_new = data_import.drop(data_import.columns.difference(RELEVANT_COLS), axis=1)  # axis=1 means columns

    count_rows_imported = len(data_new.index)

    # Format date
    data_new['Valutadatum'] = pd.to_datetime(data_new['Valutadatum'], format='%d.%m.%Y', errors='coerce')
    # # 'coerce': no errors for empty cells

    data_all = pd.read_csv(PATH_DATA_ALL, index_col=0, parse_dates=['Valutadatum'])
    # # index_col = 0: read first column as index column

    count_rows_existing = len(data_all.index)

    # Create temporary concatination
    data_tmp = pd.concat([data_all, data_new], axis=0, ignore_index=True)
    # # axis=0 (along rows) is default = combine rows of input tables
    # # ignore_index=True: ignore existing index, set new index for all

    count_rows_tmp = len(data_tmp.index)

    data_all = data_tmp.drop_duplicates()

    count_rows_all = len(data_all.index)

    count_rows_dropped = count_rows_tmp - count_rows_all

    count_rows_new = count_rows_imported - count_rows_dropped

    # Sort by date, newest first
    data_all = data_all.sort_values(by='Valutadatum', ascending=False)

    data_all = data_all.reset_index(drop=True)

    data_all.to_csv("data/output/data_all.csv")  # index=False: not writing unnamed first column

    # Count information to return
    row_counts = {
        'existing': count_rows_existing,
        'imported': count_rows_imported,
        'tmp': count_rows_tmp,
        'dropped': count_rows_dropped,
        'new': count_rows_new,
        'all': count_rows_all
    }

    return row_counts

def read_data_all():
    '''
    Returns dataframe from data_all.csv
    '''
    data_all = pd.read_csv(PATH_DATA_ALL, index_col=0, parse_dates=['Valutadatum'])

    return data_all
