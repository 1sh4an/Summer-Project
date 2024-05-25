import numpy as np

def ema(prices,period, weighting_factor):
    e=np.zeros(len(prices))
    sma=np.mean(prices[:period])
    e[period-1]=sma
    for i in range(period,len(prices)):
        e[i]=(prices[i]*weighting_factor+e[i-1]*(1-weighting_factor))
    
    return e

prices=[100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
period=5
weighting_factor=0.2

lmao=ema(prices,period,weighting_factor)

print(lmao)