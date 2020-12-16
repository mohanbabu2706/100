In[4]:
    %matplotlib inline
    import seaborn as sns; sns.set()

    strats = ['returns']

    for col in cols:
        strat = 'strategy_%s' % col.split('_')[1]
        df[start] = df[col].shift(1) *df['returns']
        strats.append(start)

    df[strats].dropna().cumsum().apply(np.exp).plot()
