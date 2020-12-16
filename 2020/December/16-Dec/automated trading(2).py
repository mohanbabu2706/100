In[6]:
    mt = MomentumTrader(momentum=12,environment='practice',
                        access_token=config['oanda']['access_token'])
    mt.rates(account_id=config['oands']['account_id'],
             instruments=['DE30_EUR'],ignore_heartbeat=True)
