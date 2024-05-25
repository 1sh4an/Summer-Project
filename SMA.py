import numpy as np

def simple_moving_average(prices, period):
    sma = np.zeros(len(prices))
    for i in range(period - 1, len(prices)):
        sma[i] = np.mean(prices[i - period + 1:i + 1])
    return sma

prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
period = 5

sma = simple_moving_average(prices, period)
print(sma)