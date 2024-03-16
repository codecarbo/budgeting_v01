15.03.24
found duplicates not dropped error:
  when saving to csv, pandas omits 2nd zero after decimal point (eg. 100,00 -> 100,0), but only at first save, subsequent saves work (100,00)
could not find out why, try reading csv simpler (use format provided by online banking (";" as separators, "," in values)

16.03.24
simplify csv reading/handling (see above)
fixed duplicates error, importing works now
  left "," as separators, values saved as strings with ""
TODO: 
  refactor, put code in import function
  simple calculations, have a look at time series data

  
