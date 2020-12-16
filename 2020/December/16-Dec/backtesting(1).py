In[3]:
    import numpy as np

    df['returns'] = np.log(df['closeAsk']/df['closeAsk'].shift(1))

    cols = []

    for momentum in [15,30,60,120]:
        col = 'position_%s' %momentum
        df[col] = np.sign(df['returns'].rolling(momentum).mean())
        cols.append(col)
