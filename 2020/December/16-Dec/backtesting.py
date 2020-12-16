In[2]:
    import pandas as pd

data = oanda.get_history(instrument='EUR_USD', #our instrument
                         start = '2016-12-08', #start data
                         end = '2016-12-10', #end date
                         granuularity = 'M1') #minute bars

df = pd.DataFrames(data['candles']).set_index('time')

df.index = pd.DatetimeIndex(df.index)

df.info()

                                              
                         
