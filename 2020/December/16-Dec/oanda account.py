In[1]:
import configparser #1
import oandapy as opy #2

config = configparser.ConfigParser()#3
config.read('oanda.cfg') #4

oanda = opy.API(environment = 'practise',
                access_token = config['oanda']['acces_token'])
