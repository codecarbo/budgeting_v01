15.03.24
found duplicates not dropped error:
  when saving to csv, pandas omits 2nd zero after decimal point (eg. 100,00 -> 100,0), but only at first save, subsequent saves work (100,00)
could not find out why, try reading csv simpler, use format provided by online banking (";" as separators, "," in values)

16.03.24
simplify csv reading/handling (see above)
fixed duplicates error, importing works now
  left "," as separators, values saved as strings with ""
TODO: 
  refactor, put code in import function
  simple calculations, have a look at time series data

20.03.24
create import function (refactor code, put into function)
create basic evaluation functions (e.g. expenses for given month or within time frame)
TODO: 
  put evaluation in function
  add Haushaltskonto to data
  import all of last year

28.03.24
Added date range function
Added income, expenses, total eval function
Separate read (from data_all.csv), evaluate (dataframe from csv) and export (back to csv)
What to evaluate next?
  inc/exp/total for every month for every account and all accounts
    generate list (dataframe and csv) and export/save
    plot diagrams
  implement categories for income/expenses regarding 'Zahlungsempfänger', 'Verwendungszweck'